#!/bin/bash

#Checking User Account
echo -e  "Logged in as: $USER\n"

#Check Building Number
echo -e "What Building In MPK is your printer located in?"
read mpknum
#Check Zone
if [ $mpknum == '21' ]
then echo "What zone is your printer located in?"
    read mpkzone
fi

if [ $mpkzone == '9' ]
then
    echo -e "Please type the corresponding letter for the printer name you want to install drivers for:"
    echo -e "A) Villian_Pub"
    echo -e "B) Lobby9_Floor1"
    echo -e "C) Lobby9_Floor2"
    echo -e "D) Lobby9_Floor2"
    echo -e "E) Weasleys_Wizard_Wheezes"
    echo -e "F) Ursulas_Grotto"
    echo -e "G) Twilfitt_And_Tattings"
    echo -e "H) Vault_101"
    echo -e "I) Wily_Fortress"
    echo -e "J) Victory_Road"
    echo -e "K) Yoshis_Island"
    echo -e "L) Blue_Fish"
    echo -e "M) Local_39"
    echo -e "N) Jackal"
    echo -e "O) Ship_Happens"
    echo -e "P) Satoshi"
    echo -e "Q) War_Heads"
    echo -e "R) Stilton"

    echo -e "\n Press Enter when done \n"

    read printername
fi





if [ $printername == 'A' ]
then
    #PRINTER INSTALL: MPK21z9 - Villain_Pub

    #DOWNLOAD
    echo -e "Starting printer driver download process for 'Villain_Pub'\n"
    echo -e "Location: MPK21-09-N \n Model: Canon iR-ADV C5550i \n Function: Copy, Print, Scan\n Paper: Letter, Legal, 11x17 \n"
    echo -e "Beginning Download"

    #OPENING AUTO DOWNLOAD URL
    open 'https://l.facebook.com/l.php?u=https%3A%2F%2Fprinter.glb.thefacebook.com%2Fprinters%2FMPK21-09-N-Villain_Pub.zip&h=AT1s-uKqulQ0mYr8VDuc7zKz5J9PFvMnxUcYj7ksuqtB1j8QpUVf8EE9GHzUR0X38KE0izhFRjjwmMQERCKCxcNsT6Srfe5qmgEzC8Z-_-id0bcGCvPvqJ5kuTQKZtT9kFhgYh9Xb-2wTZOVQbKes5x2YDg'
    echo -e "Download completed\nStarting Install..."
    echo -e "Moving to user downloads folder..."
    cd /Users/$USER/Downloads

    #OPEN ZIP
    echo -e "Opening zip"
    open /Users/$USER/Downloads/MPK21-09-N-Villain_Pub.zip

    #OPEN APP FILE
    echo -e "Unzipping file"
    open /Users/$USER/Downloads/MPK21-09-N-Villain_Pub.app

    #OPENING SECURITY PREFERENCES
    echo -e "Opening Security Preferences"
    open -b com.apple.systempreferences /System/Library/PreferencePanes/Security.prefPane

    #USER COMPLETES PROCESS

fi
