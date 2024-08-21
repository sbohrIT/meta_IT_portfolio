#Login Certification Renewal Assistant
#Created by Scott Bohr - Enterprise Support Tech

import os
import subprocess
import platform
import socket
import sys
import webbrowser
import getpass
import tkinter
from tkinter import *
from datetime import datetime


###Security Commands###

#list-keychains - Display or manipulate the keychain search list
#login-keychain - Display or set the login keychain
#delete-keychain - Delete keychains and remove them from the search list
#find-certificate - Find a certificate item
#delete-certificate - Delete a certificate from a keychain
#find-identity - Find an identity (certificate + private key)
#delete-identity - Delete an identity (certificate + private key)

#security find-identity OUTPUT:
#
# Policy: X.509 Basic
#  Matching identities
#  1) 68F6E016726F5D1E9ECEAF255F7EB0A2E1869B91 "sbohr"
#  2) 5E278E5A7D6956FF44E0369E17D3D83829F7CFC6 "MicroMDM Identity (sbohr-#mbp)" (CSSMERR_TP_NOT_TRUSTED)
#  3) EBA08840ACE2A0EC4766A0C115F96A6E791E5CAD "c02z81mvlvdl$"
#     3 identities found
#
# Valid identities only
#  1) 68F6E016726F5D1E9ECEAF255F7EB0A2E1869B91 "sbohr
#  2) EBA08840ACE2A0EC4766A0C115F96A6E791E5CAD "c02z81mvlvdl$"
#     2 valid identities found

#USE GREP TO FILTER THIS OUTPUT
#security find-identity | grep -m 1 sbohr OUTPUT:
#
#  1) 68F6E016726F5D1E9ECEAF255F7EB0A2E1869B91 "sbohr"


#DELETING CURRENT CERTIFICATE
# security delete-identity -c unixname (SUCCESSFULLY DELETES CERT)

################################ START OF CODE ##################################################


#Get Current Time



now = datetime.now()

current_time = now.strftime("%H:%M:%S")
print("Current Time =", current_time)

#Store Unixname in variable
user = getpass.getuser()
print("The user currently logged in is: " + user)

#Check if login cert exists for user

command = "security find-identity | grep -o -m 1 " + user

os.system(command + " > /dev/null")

if os.system(command) == 0:
    print(user + " has a valid login cert")

else: print("No login cert found for " + user)


###################### Check to see if Cisco AnyConnect is running ##############################

process_name= "Cisco AnyConnect Secure Mobility Client" # process variable

process_list = os.popen("ps -Af").read()

if process_name not in process_list[:]:
    
    print("Cisco AnyConnect VPN is not running..")

else: print("Cisco AnyConnect is running..")


#Check VPN State 

os.system("/opt/cisco/anyconnect/bin/vpn state")




#Checks Log Files for Clues of Certificate Validation Failures

#output = os.popen(cmd).read()
#cvf = os.popen(sudo log show --predicate '(eventMessage CONTAINS "cisco")' --predicate '(messageType == "Error")' --last 30 | grep -o -m 1 "deny(1) system-privilege 10006").read()
#print(cvf)

#output = subprocess.check_output("cat syscall_list.txt | grep f89e7000 | awk '{print $2}'", shell=True)
#output = subprocess.run(["sudo", "log", "show", "--predicate", "(eventMessage CONTAINS 'com.cisco.anycon(14233) deny(1) system-privilege 10006')", "--last", "30"])
#print(output.returncode)



######################### Check for Certificate Validation Errors in System Logs ###############################

#Looking at Log Files for Cisco AnyConnect related Errors

#### THIS WORKS!############################
#Sudo not needed to run "log show"
log_scan = "log show --predicate 'eventMessage CONTAINS \"Certificate Validation Failure\" && subsystem CONTAINS \"com.cisco.anyconnect.vpn\" && process CONTAINS \"Cisco AnyConnect Secure Mobility Client\"' --last 2m"
#print(log_scan)
result = subprocess.run(log_scan, shell=True, capture_output=True, text =True)
#print(result)
#stdout now holds the output needed
#Contains filtered log information with "Certificate Validation Error"
log_filter = str(result.stdout) 
print(log_filter)

cvf = "0"
cvf = log_filter.find("Certificate Validation Failure")

print(cvf)


############################# START OF IF:ELSE FOR GUI #################################################################
#If statement to detect if "Certificate Validation Failure" was found in recent logs

if cvf == -1:
    print("No Certificate Validation Errors Detected")
else:
    print("Certificate Validation Error Detected... Launching Help@ Assistant")

    
########################## HELP@ ASSISTANT GUI ############################################
    #Initializing GUI
    root = Tk()

    #Global Labels
    instructions = Label(root)
    follow = Label(root)
    step1 = Label(root)
    step2 = Label(root)
    step3 = Label(root)
    step4 = Label(root)
    step5 = Label(root)
    step6 = Label(root)

    var = IntVar()
    root.title("Help@ Cert Assistant")
    f1=Frame(root, height=50, width=250)
    root.resizable(width=False, height=False)
    f1.pack()

    def sel():
       selection = "You selected the option " + str(var.get())
       label.config(text = selection)

    def steps():
        #instructions.config(text = "\n \n To resolve this issue please follow these steps: \n \n 1: Open the F-Menu \n \n 2: Click Actions -> Renew Lighthouse Cert \n \n 3: Authenticate to Internal Facebook Authentication Page \n \n 4: Please open a web browser such as safari or chrome on your other device and go to this URL: fburl.com/token \n \n 5:Enter Token from device on the mobile device management authentication page \n \n 6: If Successful, Test your VPN connection")
        #instructions.pack()
        F1 = "\n \n To resolve this issue please follow these steps: \n \n"
        follow.config(text = F1)
        s1 = "1: Open the F-Menu \n \n"
        step1.config(text = s1)
        s2 = "2: Click Actions -> Renew Lighthouse Cert \n \n"
        step2.config(text = s2)
        s3 = "3: Authenticate to Internal Facebook Authentication Page \n \n"
        step3.config(text = s3)
        s4 = "4: Please open a web browser such as safari or chrome on your other device and go to this URL: fburl.com/token \n \n"
        step4.config(text = s4)
        s5 = "5: Enter Token from device on the mobile device management authentication page \n \n"
        step5.config(text = s5)
        s6 = "6: If Successful, Test your VPN connection \n \n"
        step6.config(text = s6)

        follow.pack()
        step1.pack()
        step2.pack()
        step3.pack()
        step4.pack()
        step5.pack()
        step6.pack()

        #Resetting Labels for "No" response
        instructions.config(text = "")
        instructions.pack()
        
    
    
    def helpme():
        instructions.config(text = "\n \n Please Contact the Help@ team to resolve this issue")
        instructions.pack()

        #Resetting Labels for "Yes" response
        F1 = ""
        follow.config(text = F1)
        s1 = ""
        step1.config(text = s1)
        s2 = ""
        step2.config(text = s2)
        s3 = ""
        step3.config(text = s3)
        s4 = ""
        step4.config(text = s4)
        s5 = ""
        step5.config(text = s5)
        s6 = ""
        step6.config(text = s6)
    
   

#root = Tk()
#var = IntVar()
#root.title("Help@ Cert Assistant")
#f1=Frame(root, height=50, width=250)
#root.resizable(width=False, height=False)
#f1.pack()


    ask = Label(root)
    ask.config(text = "You are experiencing an issue with your login cert which is preventing you from connecting to VPN. \n \n Good news is, you may be able to fix this issue using our self service tools. \n \n \n Do you have a work phone or another work device with internal access? \n \n")
    ask.pack()

    R1 = Radiobutton(root, text="YES", variable=var, value=1,
                      command=steps)
    R1.pack(anchor = CENTER)


    R2 = Radiobutton(root, text="NO", variable=var, value=2,
                      command=helpme)
    R2.pack(anchor = CENTER)

    label = Label(root)
    label.pack()


#If Yes was selected, continue with instructions


    root.mainloop()
################################### END OF GUI ###############################################################
################################## END OF IF:ELSE FOR GUI ###########################################################





################################## AUTOMATION ##############################################################################
#Use Built in Mac OS Automater App to create Application that will Run this Python Script every time Cisco is launched

