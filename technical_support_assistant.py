#Technical Support Assistant Program
#Created by Scott Bohr - Enterprise Support Tech 

import os
import platform
import sys
import subprocess
import webbrowser






OS = "N/A"
selection = "N/A"

while selection != "exit":

    print("\n\n\n")
    print("#########################################")
    print("IT Technical Support Guide")
    print("#########################################")
    print("\n")

    print("Operating System: ")
    OS = platform.system()

    if(OS == "Darwin"):
        print("Mac OS X")
        print('\nNOTE: If you are running this program on the Mac Terminal, all input must be in quotations. Example: "A" ')

    elif(OS == "Windows"):
        print("Windows")
    elif(OS == "Linux"):
        print("Linux")

    print ("\n")



    print("Please select an option below that best fits your needs (1-15) \n")
    print("Type 'exit' to quit \n")
    print("1. Create a ticket for help")
    print("2. Device Upgrade/Asset Dispute")
    print("3. Buy@")
    print("4. Contact Remote Support") #Help@ intern Page & Bomgar Launch
    print("5. Reset AD Password")
    print("6. Re-new certificates") #Temp Cert & Chef
    print("7. 2fac")
    print("8. Mobile Phones") #Reset Passcode\Wipe, Corporate Enrollment, Int Data, Line Release
    print("9. E-mail & Calendar") #Calendar Tool, Corporate E-mail Requests, DL Maintainer Tool
    print("10. Request a DevServer") #DevServer
    print("11. Request a Utility or Admin Account") #Utility/Admin Account
    print("12. Request Software") #Software
    print("13. Add a Printer")
    print("14. Personal Account Issues (Oops)") #Oops (personal account troubleshooting")
    print("15. Search Internal Wiki \n")

    print("Select an option, then press Enter")

    selection = input()

    if selection == "exit":
        print("\n\nEnding Session...")
        sys.exit()

    #Create a Task
    if selection == "1":

        a_website = "https://our.internmc.facebook.com/intern/tasks"

        # Open url in a new window of the default browser, if possible
        os.system("open /Applications/'Google Chrome.app'")
        webbrowser.get('chrome').open_new(a_website)

        #Devices & Assets
    if selection == "2":

        a_website = "https://our.internmc.facebook.com/intern/profile/devices/assets"

        # Open url in a new window of the default browser, if possible
        os.system("open /Applications/'Google Chrome.app'")
        webbrowser.get('chrome').open_new(a_website)

    #Buy@
    if selection == "3":
        a_website = "https://our.internmc.facebook.com/intern/buy/store/"

        # Open url in a new window of the default browser, if possible
        os.system("open /Applications/'Google Chrome.app'")
        webbrowser.get('chrome').open_new(a_website)

    #Help@
    if selection == "4":
        os.system("open /Applications/'IT Technical Support.app'")
        a_website = "https://our.internmc.facebook.com/intern/help/portal/"
        os.system("open /Applications/'Google Chrome.app'")
        webbrowser.get('chrome').open_new(a_website)


        #Reset Password
    if selection == "5":
        a_website = "https://our.internmc.facebook.com/intern/password"
        os.system("open /Applications/'Google Chrome.app'")
        webbrowser.get('chrome').open_new(a_website)

        #Certificates
    if selection == "6":

        print("\n\nSelection a certificate option that best fits your needs:")
        print("\nA. Request a Temporary Certificate")
        print("\nB. Fix Certificate Issues (Run Chef)\n")
        print("Please select an option (A-B): ")
        choice = input()

        #Prompt to choose between Temp Cert & Running Chef
        if choice == "exit":
            print("\n\nEnding Session...")
            sys.exit()

        #Temp Cert
        if choice == "A":
            a_website = "https://our.intern.facebook.com/intern/security/cert_management"
            os.system("open /Applications/'Google Chrome.app'")
            webbrowser.get('chrome').open_new(a_website)

        #RUN CHEF
        if choice == "B":

            print("\nChecking lighthouse connection...")

            #Runs Airport Command looking for 'SSID: lighthouse'
            #SSID == 0 if run is successful (ON LIGHTHOUSE)
            #SSID != 0 if run fails (NOT ON LIGHTHOUSE)
            SSID = os.system('airport -I | grep "SSID: lighthouse"')
            #print(SSID)


            #Success
            if(SSID == 0):

                print("If prompted, please enter your password to allow Chef to run\n")
                os.system("sudo kdestroy -a")
                print("Pulling new Kerberos Ticket...\n\n")
                os.system("sudo kinit")
                print("Starting Chef")
                os.system("sudo chefctl -ic")


            #Fail
            elif(SSID != 0):
                print("\n\nYou are not connected to LightHouse. Please connect to LightHouse before renewing certificates\n")


    #2Fac
    if selection == "7":

        a_website = "https://our.internmc.facebook.com/intern/2fac/"
        os.system("open /Applications/'Google Chrome.app'")
        webbrowser.get('chrome').open_new(a_website)


    #Mobile Phones
    if selection == "8":

        print("\n\n\n")
        print("#########################################")
        print("Mobile Phones")
        print("#########################################")

        print("\nWhich Mobile Phone option best fits your needs? \n\n")
        print("A. Reset Passcode/Wipe Device")
        print("B. Corporate Enrollment")
        print("C. Internation Data/Tethering")
        print("D. Line Release\n")
        print("Please select an option (A-D): ")
        choice = input()

        if choice == "exit":
            print("\n\nEnding Session...")
            sys.exit()

        #Reset Passcode & Wipe
        if choice == "A":
            a_website = "https://our.internmc.facebook.com/intern/mdm/"
            os.system("open /Applications/'Google Chrome.app'")
            webbrowser.get('chrome').open_new(a_website)


        #Corporate Enrollment
        if choice == "B":
            a_website = "https://www.intern.facebook.com/help/contact/152971078236732"
            os.system("open /Applications/'Google Chrome.app'")
            webbrowser.get('chrome').open_new(a_website)

        #International Data & Tethering
        if choice == "C":
            a_website = "https://www.intern.facebook.com/help/contact/451460935289722"
            os.system("open /Applications/'Google Chrome.app'")
            webbrowser.get('chrome').open_new(a_website)

        #Line Release
        if choice == "D":
            a_website = "https://www.intern.facebook.com/help/contact/200041487097888"
            os.system("open /Applications/'Google Chrome.app'")
            webbrowser.get('chrome').open_new(a_website)




    #E-mail & Calendar
    if selection == "9":
        print("\n\n\n")
        print("#########################################")
        print("E-mail & Calendar")
        print("#########################################")



        print("\nWhich E-mail/Calendar option best fits your needs? \n\n")
        print("A. Book a Meeting (Calendar Tool)")
        print("B. Corporate E-mail Request")
        print("C. Make Changes to Distribution List\n")
        print("Please select an option (A-C): ")
        choice = input()

        if choice == "exit":
            print("\n\nEnding Session...")
            sys.exit()

        #Book Meeting
        if choice == "A":
            a_website = "https://our.internmc.facebook.com/intern/meeting/"
            os.system("open /Applications/'Google Chrome.app'")
            webbrowser.get('chrome').open_new(a_website)


        #Corporate E-mail Request
        if choice == "B":
            a_website = "https://www.intern.facebook.com/help/contact/395115997694383"
            os.system("open /Applications/'Google Chrome.app'")
            webbrowser.get('chrome').open_new(a_website)

        #DL Maintainer Tool
        if choice == "C":
            a_website = "https://our.dev.facebook.com/intern/lists/"
            os.system("open /Applications/'Google Chrome.app'")
            webbrowser.get('chrome').open_new(a_website)



    #Request a DevServer
    if selection == "10":
        a_website = "https://www.internalfb.com/devservers/"
        os.system("open /Applications/'Google Chrome.app'")
        webbrowser.get('chrome').open_new(a_website)

    #Request a Utility or Admin Account
    if selection == "11":
        a_website = "https://our.internmc.facebook.com/intern/security/secondary_accounts"
        os.system("open /Applications/'Google Chrome.app'")
        webbrowser.get('chrome').open_new(a_website)

    #Request Software
    if selection == "12":
        a_website = "https://our.internmc.facebook.com/intern/buy/store/software/all"
        os.system("open /Applications/'Google Chrome.app'")
        webbrowser.get('chrome').open_new(a_website)

    #Adding Printers
    if selection == "13":
        print("\n\n\n")
        print("#########################################")
        print("Add a Printer (Work In Progress)")
        print("#########################################")
        print("\n")
        print("Select a Region (A-F):")
        print("\nA. San Francisco Bay Area")
        print("\nB. Midwest - Illinois/Iowa/Michigan/Nebraska")
        print("\nC. West - California/Colorado/Oregon/Washington/Utah")
        print("\nD. Southwest - New Mexico/Texas")
        print("\nE. Northeast - Massachusetts/New York/Pennsylvania/Washington D.C")
        print("\nF. Southeast - Florida/North Carolina/Georgia/Virginia20")
        print("\nRegion: ")



        choice = input()

        if choice == "exit":
            print("\n\nEnding Session")
            sys.exit()

        if choice == "A":

            print("\n\nSelect an Office (a-h):")
            print("\na. Fremont")
            print("\nb. Menlo Park")
            print("\nc. Mountain View")
            print("\nd. San Francisco")
            print("\ne. Santa Clara")
            print("\nf. AR/VR Sausalito")
            print("\ng. Sunnyvale")
            print("\nh. Newark Transportation Hub\n")

            print("Select an option:")
            office = input()


            if(office == "exit"):
                print("\n\nEnding Session...")
                sys.exit()

            if(office == "a"):
                a_website = "https://our.internmc.facebook.com/intern/wiki/IT_Technical_Help/Printers/Fremont/"
                os.system("open /Applications/'Google Chrome.app'")
                webbrowser.get('chrome').open_new(a_website)

            if(office == "b"):
                a_website = "https://our.internmc.facebook.com/intern/wiki/IT_Technical_Help/Printers/Menlo_Park/"
                os.system("open /Applications/'Google Chrome.app'")
                webbrowser.get('chrome').open_new(a_website)

            if(office == "c"):
                a_website = "https://our.internmc.facebook.com/intern/wiki/IT_Technical_Help/Printers/Mountain_View/"
                os.system("open /Applications/'Google Chrome.app'")
                webbrowser.get('chrome').open_new(a_website)

            if(office == "d"):
                a_website = "https://our.internmc.facebook.com/intern/wiki/IT_Technical_Help/Printers/San_Francisco/"
                os.system("open /Applications/'Google Chrome.app'")
                webbrowser.get('chrome').open_new(a_website)

            if(office == "e"):
                a_website = "https://our.internmc.facebook.com/intern/wiki/IT_Technical_Help/Printers/SNC1/"
                os.system("open /Applications/'Google Chrome.app'")
                webbrowser.get('chrome').open_new(a_website)

            if(office == "f"):
                a_website = "https://our.internmc.facebook.com/intern/wiki/IT_Technical_Help/Printers/Oculus_Sausalito/"
                os.system("open /Applications/'Google Chrome.app'")
                webbrowser.get('chrome').open_new(a_website)

            if(office == "g"):
                a_website = "https://our.internmc.facebook.com/intern/wiki/IT_Technical_Help/Printers/Sunnyvale/x "
                os.system("open /Applications/'Google Chrome.app'")
                webbrowser.get('chrome').open_new(a_website)

            if(office == "h"):
                a_website = "https://our.internmc.facebook.com/intern/wiki/IT_Technical_Help/Printers/NWK/"
                os.system("open /Applications/'Google Chrome.app'")
                webbrowser.get('chrome').open_new(a_website)



        if choice == "B":
            a_website = "https://www.intern.facebook.com/help/contact/395115997694383"
            os.system("open /Applications/'Google Chrome.app'")
            webbrowser.get('chrome').open_new(a_website)

        if choice == "C":
            a_website = "https://www.intern.facebook.com/help/contact/395115997694383"
            os.system("open /Applications/'Google Chrome.app'")
            webbrowser.get('chrome').open_new(a_website)

        if choice == "D":
            a_website = "https://www.intern.facebook.com/help/contact/395115997694383"
            os.system("open /Applications/'Google Chrome.app'")
            webbrowser.get('chrome').open_new(a_website)

        if choice == "E":
            a_website = "https://www.intern.facebook.com/help/contact/395115997694383"
            os.system("open /Applications/'Google Chrome.app'")
            webbrowser.get('chrome').open_new(a_website)

        if choice == "F":
            a_website = "https://www.intern.facebook.com/help/contact/395115997694383"
            os.system("open /Applications/'Google Chrome.app'")
            webbrowser.get('chrome').open_new(a_website)


    #Personal Account (Oops)
    if selection == "14":
        a_website = "https://www.facebook.com/help/contact/1136068366599070"
        os.system("open /Applications/'Google Chrome.app'")
        webbrowser.get('chrome').open_new(a_website)



    #Intern Search
    if selection == "15":

        print("\n\n\n")
        print("#########################################")
        print("\nFacebook Internal Search")
        print("#########################################")
        print("\n")
        print("What would you like to search?")
        print("Enter 'exit' to quit")

        search = input()

        if(search == "exit"):
            print("\n\nEnding Session")
            sys.exit()
        else:
            a_website = "https://our.internmc.facebook.com/intern/search/?query=" + search
            os.system("open /Applications/'Google Chrome.app'")
            webbrowser.get('chrome').open_new(a_website)
