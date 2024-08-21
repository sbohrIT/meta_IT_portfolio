import os
import subprocess
import platform
import socket
import sys
import webbrowser
import getpass

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




###################### Check to see if Cisco AnyConnect is running ##############################

process_name= "Cisco AnyConnect Secure Mobility Client" # process variable

process_list = os.popen("ps -Af").read()

if process_name not in process_list[:]:
    
    print("Cisco AnyConnect VPN is not running..")

else: print("Cisco AnyConnect is running..")


#Check VPN State 

os.system("/opt/cisco/anyconnect/bin/vpn state")


#Store Unixname in variable
user = getpass.getuser()
print("The user currently logged in is: " + user)

#Check if login cert exists for user

command = "security find-identity | grep -o -m 1 " + user

os.system(command + " > /dev/null")

if os.system(command) == 0:
    print(user + " has a valid login cert")

else: print("No login cert found for " + user)








######################### Check to see if VPN Processes are running ###############################
  
#Checking for SubProcess Error

#Running the VPN Process
p = subprocess.run(['/opt/cisco/anyconnect/bin/vpnagentd'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

#Capturing Error Message
stdout = p.stdout # stdout = normal output
stderr = p.stderr # stderr = error output

#Check Process Return Code
if p.returncode != 0:
    print("Cisco AnyConnect had an error")

else: print("Cisco AnyConnect ran successfully")
