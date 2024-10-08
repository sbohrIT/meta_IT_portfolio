import os
import subprocess
import json
import platform
import socket
import sys
import webbrowser
import getpass
from datetime import datetime
import shlex
from shlex import quote

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



######################### Check to see if VPN Processes are running ###############################

#Looking at Log Files for Cisco AnyConnect related Errors

#### THIS WORKS!############################
log_scan = "sudo log show --predicate 'eventMessage CONTAINS \"Certificate Validation Failure\" && subsystem CONTAINS \"com.cisco.anyconnect.vpn\" && process CONTAINS \"Cisco AnyConnect Secure Mobility Client\"' --last 2m"
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

#If statement to detect if "Certificate Validation Failure" was found in recent logs

if cvf == "-1":
    print("No Certificate Validation Errors Detected")
else:
    print("Certificate Validation Error Detected... Launching Help@ Assistant")




########################## HELP@ ASSISTANT GUI ############################################







