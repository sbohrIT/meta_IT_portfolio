
#UFY Shell Script For Macs

#1. Receive unixname of current user = result of “whoami”

#2. Ask User if they are experiencing “Certificate Validation Error”
################################################
#osascript -e 'display dialog "Are you Experiencing Certificate Validation Errors when connecting to VPN?" buttons {"No", "Yes”}’

#Output = button returned:Yes (Continue with Script)
#Output = button returned:No (State “UFY Cert Tool Aborted”)
################################################
#3. Edit Keychain via Terminal = “security command”

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

#LAUNCHING UFY
# Run “open https://fburl.com/ufy”
# Prompt User to find device under “Request a temporary certificate” and click “Request Cert”.
# Complete 2Fac
# Run downloaded “tempcert” file
# Prompt user to enter “ufycert” password with “login”
# Check if temp cert is properly added

#LAUNCH VPN
#Prompt User to Connect

#After VPN connection is successful..
#DELETE TEMP CERT
#Run sudo soloctl -I or sudo chefctl -I

#Verify new cert is installed
#Prompt user to re-launch web browser and authenticate to prompt


##########################################---CODE-----###########################################
import os
import subprocess
import platform
import socket
import sys
import webbrowser


#user = os.system("whoami")
#user = subprocess.Popen("whoami", shell=True)
user = os.popen('whoami').read()
print(user)
ufy_page = "https://fburl.com/ufy"
internHost = "www.interngraph.intern.facebook.com"

needCert = input("Are you experiencing a 'Certificate Validation' Error? (Y/N): ")

if needCert == 'Y':
    print("\nBeginning Certificate Renewal...")
    print("\nWiping current login certificate entries...")


    #DELETING CURRENT CERTIFICATE
    certWipe = os.system("security delete-certificate -c" + user)
    if certWipe == 0:
        print("Login certificate deleted: " + user) #Success

    else:
        print("\n Error when attempting to delete login certificate") #Fail

    #Display UFY Process
    print("\nNEXT STEPS:\n")
    print("1) Go to https://fburl.com/ufy on any web browser \n")
    print("2) Click 'Request Cert' for the desired device \n")
    print("3) Authenticate to 2Fac Prompt (Duo or Yubikey) \n")
    print("4) Open up the downloaded file named temp_cert(password=ufycert).pfx \n")
    print("5) The downloaded file is password protected with password 'ufycert'. Provide that password to open up the file. Your certificate will be installed and show up in your login keychain \n")
    print("6) Connect to Cisco VPN\n\n")


    #Prompt if ready to move forward
    ufyready = input("Do you understand these instructions and are ready to move forward with UFY? (Y/N): ")

    if ufyready == 'Y':
        print("\nPreparing UFY...")

    else:
        while ufyready != 'Y':
            print("\n\nPlease re-read the instructions and type 'Y' when ready to continue")
            ufyready = input("Are you ready to continue? (Y/N) \n")


    #Launch UFY
    print("\nRe-directing to https://fburl.com/ufy now...\n\n")
    webbrowser.get('safari').open_new(ufy_page)

    #Prompt to continue after installing Temp Cert
    tempCheck = input("Have you successfully installed a UFY cert? (Y/N)")
    if tempCheck == 'Y':
        #Check for Temp Cert
        temp = os.system("security find-identity | grep -m 1 " + user)
        # Output ^^^ = 68F6E016726F5D1E9ECEAF255F7EB0A2E1869B91 "sbohr"
        #print(temp) #prints 0

        if temp == 0:
            print("\nLogin certificate exists")

        else:
            print("\nNo login certificate found for " + user)



        #Connect to VPN + VPN Check

        vpnCheck = os.system("ping -c 1 " + internHost)
        vpnStatus = False
        chefRun = 1
        #print(vpnCheck)
        if vpnCheck == 0:
            vpnStatus = True
            print("VPN/Intern connection Successful")
        else:
            vpnStatus = True
            print("Not connected to VPN")



        if vpnStatus == True:
            print("\n\nVPN Connection Verified...")
            print("\n\nWiping temporary UFY cert\n")
            certWipe = os.system("security delete-certificate -c" + user)
            print("\nRunning Chef...")
            print("\nPlease enter your login password to run Chef")
            chefRun = os.system("sudo soloctl -i")
            print(chefRun)


            if chefRun == 0:
                print("\n\nChef Ran Successfully...")
                print("\nChecking current login certificates...")
                perm = os.system("security find-identity | grep -m 1 " + user)

                if perm == 0:
                    print("\nNew login certificate exists!")
                    print("\nUFY Process COMPLETE!!\n")
                    sys.exit("Please check your intern access, Goodbye")

                else:
                    print("\nNo login certificate found for " + user)

    else:
        while tempCheck != 'Y':
            print("\n\nPlease install a UFY cert then type 'Y' and hit enter when ready to continue")
            tempCheck = input("Do you have a UFY cert and are ready to continue? (Y/N) \n")


        #Check for Temp Cert
        temp = os.system("security find-identity | grep -m 1 " + user)
        # Output ^^^ = 68F6E016726F5D1E9ECEAF255F7EB0A2E1869B91 "sbohr"
        #print(temp) #prints 0

        if temp == 0:
            print("\nLogin certificate exists")

        else:
            print("\nNo login certificate found for " + user)



        #Connect to VPN + VPN Check
        print("\n\nPlease connect to VPN (Cisco AnyConnect Secure Mobility Client)")
        onVPN = input("Are you connected to VPN? (Y/N)")
        if onVPN == 'Y':
            vpnCheck = os.system("ping -c 1 " + internHost)
            vpnStatus = False
            chefRun = 1
            #print(vpnCheck)
            if vpnCheck == 0:
                vpnStatus = True
                print("VPN connection Successful")
            else:
                vpnStatus = True
                print("Not connected to VPN")



            if vpnStatus == True:
                print("\n\nVPN Connection Verified...")
                print("\n\nWiping temporary UFY cert\n")
                certWipe = os.system("security delete-certificate -c" + user)
                print("\nRunning Chef...")
                print("\nPlease enter your login password to run Chef")
                chefRun = os.system("sudo soloctl -i")
                print(chefRun)


                if chefRun == 0:
                    print("\n\nChef Ran Successfully...")
                    print("\nChecking current login certificates...")
                    perm = os.system("security find-identity | grep -m 1 " + user)

                    if perm == 0:
                        print("\nNew login certificate exists!")
                        print("\nUFY Process COMPLETE!!\n")
                        sys.exit("Please check your intern access, Goodbye")

                    else:
                        print("\nNo login certificate found for " + user)

        else:
            while onVPN != 'Y':
                print("\n\nPlease connect to VPN before continuing...\n")
                onVPN = input("Are you connected to VPN? (Y/N)")

            vpnCheck = os.system("ping -c 1 " + internHost)
            vpnStatus = False
            chefRun = 1
            #print(vpnCheck)
            if vpnCheck == 0:
                vpnStatus = True
                print("VPN connection Successful")
            else:
                vpnStatus = True
                print("Not connected to VPN")



            if vpnStatus == True:
                print("\n\nVPN Connection Verified...")
                print("\n\nWiping temporary UFY cert\n")
                certWipe = os.system("security delete-certificate -c" + user)
                print("\nRunning Chef...")
                print("\nPlease enter your login password to run Chef")
                chefRun = os.system("sudo soloctl -i")
                print(chefRun)


                if chefRun == 0:
                    print("\n\nChef Ran Successfully...")
                    print("\nChecking current login certificates...")
                    perm = os.system("security find-identity | grep -m 1 " + user)

                    if perm == 0:
                        print("\nNew login certificate exists!")
                        print("\nUFY Process COMPLETE!!\n")
                        sys.exit("Please check your intern access, Goodbye")

                    else:
                        print("\nNo login certificate found for " + user)


else:
    print("\n\nAborting UFY Cert Tool...")
    print("\n\nPlease launch the IT Technical Support App to be connected with a Technician")
