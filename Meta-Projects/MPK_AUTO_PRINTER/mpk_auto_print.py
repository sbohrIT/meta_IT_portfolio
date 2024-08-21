#MPK Auto Printer Installer - BayFront Offices
#Created by Scott Bohr - Enterprise Support Tech

import os
from os import path
import webbrowser



class MPK_20_Printer():

    def __init__(self, building, zone, name):
        self.building = building
        self.zone = zone
        self.name = name

    def instructions(self):
        print("\n\n__________NEXT STEPS__________")
        print("1. Click on the printer driver zip file: MPK", self.building, "-", self.zone, "-", self.name, ".zip", " in your web browser downloads")
        print("2. This will unzip a .app file: MPK", self.building, "-", self.zone, "-", self.name, ".app")
        print("3. Click the .app file")
        print("4. You will see a message stating 'file can't be opened because Apple cannot check it for malicious software', click OK to continue")
        print("5. Open 'System Settings' app on your Mac and click 'Privacy & Security'")
        print("6. Scroll down to Security and you will see a message stating '.app was blocked from use because it is not from an identified developer'")
        print("7. Click 'Open Anyways")
        print("8. Enter your Mac password the click 'Open', then 'OK'")
        print("9. Enter your password once more")
        print("10. You will receive a message that your desired printer was added to your printer list")
        print("11. Try printing to the printer")


class MPK_21_Printer():

    def __init__(self, building, zone, name):
        self.building = building
        self.zone = zone
        self.name = name

    def instructions(self):
        print("\n\n__________NEXT STEPS__________")
        print("1. Click on the printer driver zip file: MPK", self.building, "-", self.zone, "-", self.name, ".zip", " in your web browser downloads")
        print("2. This will unzip a .app file: MPK", self.building, "-", self.zone, "-", self.name, ".app")
        print("3. Click the .app file")
        print("4. You will see a message stating 'file can't be opened because Apple cannot check it for malicious software', click OK to continue")
        print("5. Open 'System Settings' app on your Mac and click 'Privacy & Security'")
        print("6. Scroll down to Security and you will see a message stating '.app was blocked from use because it is not from an identified developer'")
        print("7. Click 'Open Anyways")
        print("8. Enter your Mac password the click 'Open', then 'OK'")
        print("9. Enter your password once more")
        print("10. You will receive a message that your desired printer was added to your printer list")
        print("11. Try printing to the printer")

class MPK_22_Printer():

    def __init__(self, building, floor, name):
        self.building = building
        self.floor = floor
        self.name = name

    def instructions(self):
        print("\n\n__________NEXT STEPS__________")
        print("1. Click on the printer driver zip file: MPK", self.building, "-", self.floor, "-", self.floor, ".zip", " in your web browser downloads")
        print("2. This will unzip a .app file: MPK", self.building, "-", self.floor, "-", self.name, ".app")
        print("3. Click the .app file")
        print("4. You will see a message stating 'file can't be opened because Apple cannot check it for malicious software', click OK to continue")
        print("5. Open 'System Settings' app on your Mac and click 'Privacy & Security'")
        print("6. Scroll down to Security and you will see a message stating '.app was blocked from use because it is not from an identified developer'")
        print("7. Click 'Open Anyways")
        print("8. Enter your Mac password the click 'Open', then 'OK'")
        print("9. Enter your password once more")
        print("10. You will receive a message that your desired printer was added to your printer list")
        print("11. Try printing to the printer")

class MPK_23_Printer():

    def __init__(self, building, zone, name):
        self.building = building
        self.zone = zone
        self.name = name

    def instructions(self):
        print("\n\n__________NEXT STEPS__________")
        print("1. Click on the printer driver zip file:", self.building, "-", self.zone, "-", self.name, ".zip", " in your web browser downloads")
        print("2. This will unzip a .app file:", self.building, "-", self.zone, "-", self.name, ".app")
        print("3. Click the .app file")
        print("4. You will see a message stating 'file can't be opened because Apple cannot check it for malicious software', click OK to continue")
        print("5. Open 'System Settings' app on your Mac and click 'Privacy & Security'")
        print("6. Scroll down to Security and you will see a message stating '.app was blocked from use because it is not from an identified developer")
        print("7. Click 'Open Anyways")
        print("8. Enter your Mac password the click 'Open', then 'OK'")
        print("9. Enter your password once more")
        print("10. You will receive a message that your desired printer was added to your printer list")
        print("11. Try printing to the printer")


#Dictionary of Printer Names

zone_list = {1:{"A": "Deadpool",
            "B": "Mod-ern_Girl",
            "C": "Potpourri",
            "D": "Big_Hero_6",
            "E": "The_Walking_Dead_or_Alive",
            "F": "Foie-Gras",
            "G": "Ship_Happens",
            "H": "Facilities"},

            2:{"A": "Con_Air",
            "B": "Jumpman",
            "C": "Snake_Eyes",
            "D": "Verdana",
            "E": "Marth",
            "F": "Tingle",
            "G": "Koopa_Kid"},

            3:{"A": "Abraham_Linker",
            "B": "BaRACK_Obama",
            "C": "Dagobah",
            "D": "Hunger_Game_Of_Thrones",
            "E": "Kamino",
            "F": "Mon_Calamari",
            "G": "Se7enth_Heaven",
            "H": "The_Dark_Knight_Rider",
            "I": "Warren_G_Harddrive",
            "J": "Hedwig"},

            4:{"A": "Sequential_Circus",
            "B": "Putting_the_USB_in_Backwards",
            "C": "Colonel_Meow",
            "D": "Nyan_Cat",
            "E": "Monorail_Cat",
            "F": "Battle_Cat",
            "G": "Bumbershoot",
            "H": "Kang_and_Kodos",
            "I": "Guy_Incognito",
            "J": "Maria_Meyer",
            "K": "Ceiling_Cat",
            "L": "Sutro"},

            5:{"A": "Curl-Up",
            "B": "Get_back_witch",
            "C": "Biaviians",
            "D": "Circle_Limit_IV",
            "E": "Kason",
            "F": "Changelings",
            "G": "Ponyo",
            "H": "SnakeHole",
            "I": "NarcBark",
            "J": "Variable"},

            6:{"A": "This_Buildings_Number",
            "B": "The_New_Internet",
            "C": "Three_Comma_Club"},

            7:{"A": "Zyzzyva",
            "B": "Will_It_Blend",
            "C": "Press",
            "D": "Rock_Star",
            "E": "Unknown",
            "F": "Youre_Frozen",
            "G": "Zurg",
            "H": "Were_Being_Kicked_Out",
            "I": "SEViche",
            "J": "Tea_CP",
            "K": "Ursula"},

            8:{"A": "CommuteFB",
            "B": "Yoko_Ono",
            "C": "Spock",
            "D": "Sulu",
            "E": "Uhura",
            "F": "CJ_Cregg",
            "G": "TurnCreativityIntoCommunity",
            "H": "Yes_Definitely"},

            9:{"A": "Villain_Pub",
            "B": "Weasley_Wizard_Wheezes",
            "C": "Ursulas_Grotto",
            "D": "Twilfitt_And_Tattings",
            "E": "Vault_101",
            "F": "Wily_Fortress",
            "G": "Victory_Road",
            "H": "Yoshis_Island",
            "I": "Blue_Fish",
            "J": "Local_39",
            "K": "Jackal",
            "L": "Ship_Happens",
            "M": "Judith-Love-Cohen",
            "N": "Satoshi",
            "O": "War_Heads",
            "P": "Stilton"}
}

floor_list = {1:{"A": "Pidgeot",
            "B": "Raticate",
            "C": "Beets_of_Burden",
            "D": "Arbok",
            "E": "Nidoqueen",
            "F": "Psyduck",
            "G": "Butterfree",
            "H": "Peaches"},

            2:{"A": "Lithium",
            "B": "Chlorine",
            "C": "Helium",
            "D": "Magnesium",
            "E": "Potassium",
            "F": "Shrimp_Tempura",
            "G": "California_Roll"},

            3:{"A": "Hollyhock",
            "B": "Animalia",
            "C": "Go_Dog_Go",
            "D": "If_You_Give_a_Mouse_a_Cookie",
            "E": "Miss_Rumphius",
            "F": "Disagree_with_The_Characterization",
            "G": "What_Problem_Are_We_Trying_To_Solve",
            "H": "Countess_of_Grantham"},

            4:{"A": "Daisy_Mason",
            "B": "Dr_Clarkson",
            "C": "Lady_Edith",
            "D": "Lavinia_Swire",
            "E": "M_and_A_Team",
            "F": "Molesley",
            "G": "Mr_Carson",
            "H": "Mrs_Hughes",
            "I": "Mrs_Patmore",
            "J": "Sir_Richard_Carlisle"}
}

mpk23_zones = {1:{"A": "Atticus_Finch",
            "B": "Be_the_Nerd",
            "C": "Diplomacy",
            "D": "Duke_Nukem",
            "E": "Mall_Madness",
            "F": "Metal_Gear",
            "G": "Michael_Clayton",
            "H": "Oregon_Trail",
            "I": "Othello",
            "J": "Scotland_Yard",
            "K": "SkiFree",
            "L": "The_Precious"},

            2:{"A": "Asks",
            "B": "At_the_End_of_the_Day",
            "C": "Cafe300_Dock",
            "D": "Candy_Colored_Clown",
            "E": "Fusilli_Jerry",
            "F": "Galactica",
            "G": "Inside_Out",
            "H": "JPeterman",
            "I": "Pegasus",
            "J": "Sherbet_Lemon",
            "K": "Taking_it_One_Day_at_a_Time",
            "L": "Treacle_Tart",
            "M": "Virginia_Woolf",
            "N": "Wizochoc"}

}

printer_type = {"M680": "HP Color LaserJet MFP \nFunctionality: Copy/Print/Scan/Fax",
                "M651": "HP Color LaserJet M651 \nFunctionality: Color Printer",
                "C5250": "Canon iR-ADV C5250 Copier \nFunctionality: Copy/Print/Scan",
                "E58650": "HP PageWide Color Flow E58650 \nFunctionality: Copy/Print/Scan",
                "CM4540": "HP Color LaserJet CM4540 \nFunctionality: Copy/Print/Scan/Fax",
                "CP4025dn": "HP Color LaserJet CP4025dn \nFunctionality: Color Printer",
                "CP4025": "HP Color LaserJet CP4025 \nFunctionality: Color Printer",
                "M130": "HP LaserJet Pro MFP M130 \nFunctionality: Copy/Print/Scan",
                "C5550i": "Canon iR-ADV C5550i \nFunctionality: Copy/Print/Scan",
                "M653": "HP Color LaserJet M653 \nFunctionality: Color Printer",
                "M577": "HP Color LaserJet MFP M577 \nFunctionality: Copy/Print/Scan/Fax",
                "E77650": "HP PageWide Color Flow E77650 \nFunctionality: Copy/Print/Scan/Fax",
                "M553": "HP Color LaserJet Enterprise MFP M553 \nFunctionality: Color Printer"
}


def print_type(model):

    print("\n\nPrinter Model: ", printer_type[model])



print("\n********** Mac OS MPK Auto Printer Installer **********")
print("\nPLEASE NOTE: You MUST be on lighthouse or VPN in order to connect to our printer server")
building = input("\n\nWhat Menlo Park (MPK) campus building is your desired printer located (20-23)? ")
building = int(building)
while building != 20 and building != 21 and building != 22 and building != 23:
    print("Non supported building number entered...")
    building = input("Please select a building between 20-23:   ")
    building = int(building)



#MPK 20
if building == 20:
    zone = input("\nWhat zone in building 20 (1-5)? ")
    zone = int(zone)
    while int(zone) < 1 or int(zone) > 5:
        print("Please enter a valid zone for MPK 20 (1-5): ")
        zone = input("\nWhat zone in building 20 (1-5)? ")
        zone == int(zone)
    if zone == 1:
        print("\n\nMPK 20 - Zone 1 Printers:")
        print("----------------------------")
        print("A) Deadpool")
        print("B) Mod-ern_Girl")
        print("C) Potpourri")
        print("D) Big_Hero_6")
        print("E) The_Walking_Dead_or_Alive")
        print("F) Foie-Gras")
        print("G) Ship_Happens")
        print("H) Facilities")
        name = input("\nPlease select a printer by entering its associated letter: ")
        pr = MPK_20_Printer(building, zone, zone_list[zone][name])
        print("\n___You Chose___")
        print("Building: ", pr.building)
        print("Floor: ", pr.zone)
        print("Name: ", pr.name)
        print("\nDownloading", pr.name, "printer driver...")
        pr.instructions()


        if pr.name == "Deadpool":
            webbrowser.open("https://l.facebook.com/l.php?u=https%3A%2F%2Fprinter.glb.thefacebook.com%2Fprinters%2FMPK20-Deadpool.zip&h=AT2f_lzhaF56dWxdZImpzooJxyBNShROlGOSG1AVYi30WQnSofRN4apeCuZ7I6QQDheUiENmgJJXDzcjkNTWqNkXRYB2RhR44XGbamZaZMrlX9t05_Evl3yXgMZiKK58QiSzFXpHSa40268rx0tZT8tCv2o")

        elif pr.name == "Mod-ern_Girl":
            webbrowser.open("https://l.facebook.com/l.php?u=https%3A%2F%2Fprinter.glb.thefacebook.com%2Fprinters%2FMPK20-Mod-ern_Girl.zip&h=AT3oYkTMCkxJ_yLvgx0Y0YyXmcnHsQYZKh3QTwtuWYDtSkg2uyGLuKjBW4_MrecP5HViFU-_RzGVJPhkj288lsDAQwBku-dX6wFhOMLS0cFnbe2y5NDE43bwkR3nwMPOH7JJofXNGbQuAcQsQawz2oQ4VKI")

        elif pr.name == "Potpourri":
            webbrowser.open("https://l.facebook.com/l.php?u=https%3A%2F%2Fprinter.glb.thefacebook.com%2Fprinters%2FMPK20-Potpourri.zip&h=AT1tZbeKNB5kg2C9FyYkqq7bYj-PT9i0D3k9vzcZJ4J9PoQl3O6Pbd6-EiYQHCTeZ-jcl1yqRuU9SnJxdn8hAk8BrdSMqx7YzmQxnuebx1crUOOmTHYw5UXEeYz_SFrUzLm1PahXQiocBZfFE5xOFB5LhDo")

        elif pr.name == "Big_Hero_6":
            webbrowser.open("https://l.facebook.com/l.php?u=https%3A%2F%2Fprinter.glb.thefacebook.com%2Fprinters%2FMPK20-Big_Hero_6.zip&h=AT2CtMPakEmHkAdT9P02TphZ9Hhkem8M8hhE87C3RW5UYfavHIifN3K9ZqbKceOenEZaOF2X2tMPRi0dkumvFJ90fAbhh6EczTChcT8rEYcR44jk6r3mA_e5HPs8sXuX-zmiAsaaIcxDoPXTixQUl5uPpwo")

        elif pr.name == "The_Walking_Dead_or_Alive":
            webbrowser.open("https://l.facebook.com/l.php?u=https%3A%2F%2Fprinter.glb.thefacebook.com%2Fprinters%2FMPK20-The_Walking_Dead_or_Alive.zip&h=AT3nni0uzthSDI_3ulj94VBd26W4HvLTT-UJPZxHsTWJworuDUwUsn_gC5odlE9JtytE8hunm5qRK2_yY0SjPEqH8L2M2ItCdGy955tjcYyTKWOqD3K25ItDWJAseh8UGm4GNT6CcB86pv0IavR_ZBPIVts")

        elif pr.name == "Foie-Gras":
            webbrowser.open("https://l.facebook.com/l.php?u=https%3A%2F%2Fprinter.glb.thefacebook.com%2Fprinters%2FMPK20-Foie_Gras.zip&h=AT2QtPvx78VLdi_7LEjHb0cZoe0QuPbKJKZ6O9gshW3K1KL5ngprB5yWTywxmaiTPwgCRZ4QylziHDa7CtsYcow2mB4RUSlJT1bs2Ef8_o2gJupn1yxEqGoVUS0Mts-1RVlS9tKkBjf2a4BrS0b7Pr84pEY")

        elif pr.name == "Ship_Happens":
            webbrowser.open("https://l.facebook.com/l.php?u=https%3A%2F%2Fprinter.glb.thefacebook.com%2Fprinters%2FMPK20-Ship_Happens.zip&h=AT0DabfHPgb53VMGcGYO3vCvaqGy71chWg-s7EizOPuuqp1ZHFpwhsqtcvGWGmIUJWusY8c-qKKplygO8PBaNNB0MCDgMnwJjeilxFTQvqj1VGw283C4usd2qdIkcl7TTKAa6ozMQe1TXgyKKjoVat92AuQ")

        elif pr.name == "Facilities":
            webbrowser.open("https://l.facebook.com/l.php?u=https%3A%2F%2Fprinter.glb.thefacebook.com%2Fprinters%2FMPK20-Facilities.zip&h=AT3WwY7AZLSryp8lohEIcYGx2JYS2RNLucqRhX43Db-V5hRGeAjKzqLNPHzsAt_vw6Rp4-Ujje4SV94aqpisF2MQOiV8S1VD_SnMM0UhHtIIQR3XVZrsVRWSIIzJUaqZgWJOOhHGQSlaG0V54tjUJ4mK-a4")

    elif zone == 2:
        print("\n\nMPK 20 - Zone 2 Printers:")
        print("----------------------------")
        print("A) Con_Air")
        print("B) Jumpman")
        print("C) Snake_Eyes")
        print("D) Verdana")
        print("E) Marth")
        print("F) Tingle")
        print("G) Koopa_Kid")
        name = input("\nPlease select a printer by entering its associated letter: ")
        pr = MPK_20_Printer(building, zone, zone_list[zone][name])
        print("\n___You Chose___")
        print("Building: ", pr.building)
        print("Floor: ", pr.zone)
        print("Name: ", pr.name)
        print("\nDownloading", pr.name, "printer driver...")
        pr.instructions()

        if pr.name == "Con_Air":
            webbrowser.open("https://l.facebook.com/l.php?u=https%3A%2F%2Fprinter.glb.thefacebook.com%2Fprinters%2FMPK20-Con_Air.zip&h=AT2Mr7W8qakXtbt11Xj0EmEYBnuLdEHP3S6K41t8VxahyTCpGU-L1ljptxPSKw4YnPPalIXulKtFagjKgbOPm6mOJAn-ngJrrclzFKq9vWpZ2omzsn9y-Mk5DMk2Pfyh0aLnMJEd2ah-jCffjCIevbZOr-g")

        elif pr.name == "Jumpman":
            webbrowser.open("https://l.facebook.com/l.php?u=https%3A%2F%2Fprinter.glb.thefacebook.com%2Fprinters%2FMPK20-Jumpman.zip&h=AT1YmJgVwavgvrxn2gknP-4xvCXa6BDd3NaiUvJ6VBGYR1LfMAu1dLTZCa-2uVueQ1IxZxFuPD99t7ZfwLJw-8aXjXavWMyFomj5olyVaOR_25LjnNwwYnnuwwvfCF7KHeX4D-iRI9hp9MVKIMSMYjmuYjk")

        elif pr.name == "Snake_Eyes":
            webbrowser.open("https://l.facebook.com/l.php?u=https%3A%2F%2Fprinter.glb.thefacebook.com%2Fprinters%2FMPK20-Snake_Eyes.zip&h=AT0tGQLr_EGQKKdqE3-ukZGjDSL38BoP3Mb19Q-ARAQrz4Y3qstbsCcUFRnC8W1DPlbd9Aw3fFz0gh_5WZWRjsSGs021K0rpF1uuSiqPUTDUnG3NzL9TwKzFjlc9_WKpP1YB1GZCyWKD67MwIU0m2GX6Bd8")

        elif pr.name == "Verdana":
            webbrowser.open("https://l.facebook.com/l.php?u=https%3A%2F%2Fprinter.glb.thefacebook.com%2Fprinters%2FMPK20-Verdana.zip&h=AT2nv3B8LOxRPFatzaQewUNV-1uoCz0qNThH5-Q1Ad_32Xiw3jUDGULkoxiP9ceHaai_IltfMebr2cIEutnle-Wrtrs1qsItHw03ET1Y7BfAaB2Q7iwOu858JNmeK1GT5SsQEZ-hjkG_lWo01O3SM62JStw")

        elif pr.name == "Marth":
            webbrowser.open("https://l.facebook.com/l.php?u=https%3A%2F%2Fprinter.glb.thefacebook.com%2Fprinters%2FMPK20-Marth.zip&h=AT3V4kO9ZPDUqC4V8p35s_UZ8eHdQA9Vpj0tLzIgdpKneUrfpl1jMd8i2GXogLGizny_PP978faK2rfeV0OQTIR8pcK7Q6kAJv_-LHwpQ-ZIMmc887qGLUcSG_VPmGgu_Lzqyd5AJjrSsKtaHdM4GND6xn4")

        elif pr.name == "Tingle":
            webbrowser.open("https://l.facebook.com/l.php?u=https%3A%2F%2Fprinter.glb.thefacebook.com%2Fprinters%2FMPK20-Tingle.zip&h=AT2vmzNnUco_GRnp5u9S-zSz9EasrA5KbveHnpOfhZ39vP-YsC6lS0kj312aFS-t2jObfwXbHjls_7mlnSJTAHcez2oMQ2zhe6he3tFlIiNnnzaQZ47kgsLtq_V7YXLTx9TKZXybCyEMWF1xv6mVPM_61Us")

        elif pr.name == "Koopa_Kid":
            webbrowser.open("https://l.facebook.com/l.php?u=https%3A%2F%2Fprinter.glb.thefacebook.com%2Fprinters%2FMPK20-Koopa_Kid.zip&h=AT1tC_QchP0bctYMi7ZkCW9hUvDpooYGGQiL2iBFsP1dztihuANopHVEchOmT_qRQxAI-P4D_PRxDsu6YXekSgW0caiFiGt6yfbl4vIa_1LGu3BTFecRj2KYGNSIQnSe_SwU2vTgnBVhS2ct9S-3QOQG3FE")


    elif zone == 3:
        print("\n\nMPK 20 - Zone 3 Printers:")
        print("----------------------------")
        print("A) Abraham_Linker")
        print("B) BaRACK_Obama")
        print("C) Dagobah")
        print("D) Hunger_Game_Of_Thrones")
        print("E) Kamino")
        print("F) Mon_Calamari")
        print("G) Se7enth_Heaven")
        print("H) The_Dark_Knight_Rider")
        print("I) Warren_G_Harddrive")
        print("J) Hedwig")
        name = input("\nPlease select a printer by entering its associated letter: ")
        pr = MPK_20_Printer(building, zone, zone_list[zone][name])
        print("\n___You Chose___")
        print("Building: ", pr.building)
        print("Floor: ", pr.zone)
        print("Name: ", pr.name)
        print("\nDownloading", pr.name, "printer driver...")
        pr.instructions()

        if pr.name == "Abraham_Linker":
            webbrowser.open("https://l.facebook.com/l.php?u=https%3A%2F%2Fprinter.glb.thefacebook.com%2Fprinters%2FMPK20-Abraham_Linker.zip&h=AT0F6r49O35f9Ov409-xpgnUOPPeFt5c1h4Wk1Ytmb_j-TvqrncJ8yvCC1pEjErrcnVQ_erHd97vcSquQbMkgs_8uMAQXQgl0N6wftjanFFHWd2RVsWEfoO5-tJYtiz38kJ8BPWHs1Mk1-vgVmrpmOuIMhQ")

        elif pr.name == "BaRACK_Obama":
            webbrowser.open("https://l.facebook.com/l.php?u=https%3A%2F%2Fprinter.glb.thefacebook.com%2Fprinters%2FMPK20-BaRACK_Obama.zip&h=AT24s1I9aqBnF74rb2N1hebAj-tqJvl1CkoECKUz9mV04Omoc-cSLWwJo1sb-1jeTa5jVfyoPyK3ZR5QhG9ovHu7tJ5Q6CNKfrVPcM-1LdzlT6zqxYdMplgtHPWjmByACI9ZCVAPJZpef4D8GmecyxzLFas")

        elif pr.name == "":
            webbrowser.open("")

        elif pr.name == "Hunger_Game_Of_Thrones":
            webbrowser.open("https://l.facebook.com/l.php?u=https%3A%2F%2Fprinter.glb.thefacebook.com%2Fprinters%2FMPK20-Hunger_Game_Of_Thrones.zip&h=AT1nOz3k98uitrdrl-8ZQ07OuFC7bbQMCVFMX5XwgVr7HK16fPy9M9vsflPIDFiaFzxUZqyKrdcAFt9nZRhalkiap-B0I0GRbHwHCTa7x90ZbHREyEYeIDPxMNntYdFfLqFGnh2TprSqY9ync-qWq2Fpvhw")

        elif pr.name == "Kamino":
            webbrowser.open("https://l.facebook.com/l.php?u=https%3A%2F%2Fprinter.glb.thefacebook.com%2Fprinters%2FMPK20-Kamino.zip&h=AT3HFzsVqfBDC6-hdvhya4O-xJ--Rf-FyoB98x4RV6dowh4pTHOE9WR5q4E_DiU41rmYr-dF0wz3UYb9hUix7SaX-bGs6Ngb59gVrf_YrNH-DtoMH1qzHY78ucYvcaRh6m0E7Vle4BqaA47u8NNldQSmDgo")

        elif pr.name == "Mon_Calamari":
            webbrowser.open("https://l.facebook.com/l.php?u=https%3A%2F%2Fprinter.glb.thefacebook.com%2Fprinters%2FMPK20-Mon_Calamari.zip&h=AT1dQhQ8CRMPzB7sSI5U56YOHETUvCGIgOQO8lG04oVzHgg4GbNSzPZ1oQLIfe5lx7OI6_4yFFjMsy_yE8CV2kc6J1g-HphOm-YLxeEuyxw_S8vC0xRoBw-444pIxhfttZviUz959kY5AbtTRdM4i3lBMKI")

        elif pr.name == "Se7enth_Heaven":
            webbrowser.open("https://l.facebook.com/l.php?u=https%3A%2F%2Fprinter.glb.thefacebook.com%2Fprinters%2FMPK20-Se7enth_Heaven.zip&h=AT0fqtfV_OiJC5SRdepbmbm8wt3Or9ZQSOSgc_hsNF1vvy5x4bLn6G4sfGFdObhz3NR049C7XEr-bzhIFIE6WV-GA8YhjU-n0OuwXK2R_CIT-cOIW_y_Mg7FNUukiu9uG5-eVWHW846TuYmt8Jy4C_D1uJE")

        elif pr.name == "The_Dark_Knight_Rider":
            webbrowser.open("https://l.facebook.com/l.php?u=https%3A%2F%2Fprinter.glb.thefacebook.com%2Fprinters%2FMPK20-The_Dark_Knight_Rider.zip&h=AT0_ry0gk1EE9cSdOUnwKfT-iyL7ld29eNhVSQtm5eMqk6erEWbE0NhKS3WJyowGHkw7teE92rL4-bkmhZKfTzRF3MaiTrONWpGdIAZhgGTU3FiCdycqHNp1KPxsFBfVSBoqM-lSrYpx7RfkdVALFarwk-g")

        elif pr.name == "Warren_G_Harddrive":
            webbrowser.open("https://l.facebook.com/l.php?u=https%3A%2F%2Fprinter.glb.thefacebook.com%2Fprinters%2FMPK20-Warren_G_Harddrive.zip&h=AT2V-xgdqzxQQmCsYo5R_I4a1SN-qPohf5ChV-W-jpxMFWHmM5xZU4rJWK5aMMccb1G4SnjgzJh4_4A271tcq8oSxl0RTcgsJ7-WpNY_lnkXaqrg0b_XnuU64dBLt9EoCGmj_QP40d6x4KvLuAdXfrY3K_Y")

        elif pr.name == "Hedwig":
            webbrowser.open("https://l.facebook.com/l.php?u=https%3A%2F%2Fprinter.glb.thefacebook.com%2Fprinters%2FMPK20-Hedwig.zip&h=AT3GjXklw2roGduMLe7GPxQxAgiy9ld8VJkATjgXlsRt14fssUDjEF11UC6YjPkFCdmK_hgF9W835ETAEW3M2ncJcB2W_63EBauq-zHlHGb_dZwW7eMcMkHOKaJmeAXANpFUmawwVr9hd_lQJebCXERzu-s")



    elif zone == 4:
        print("\n\nMPK 20 - Zone 4 Printers:")
        print("----------------------------")
        print("A) Sequential_Circus")
        print("B) Putting_the_USB_in_Backwards")
        print("C) Colonel_Meow")
        print("D) Nyan_Cat")
        print("E) Monorail_Cat")
        print("F) Battle_Cat")
        print("G) Bumbershoot")
        print("H) Kang_and_Kodos")
        print("I) Guy_Incognito")
        print("J) Maria_Meyer")
        print("K) Ceiling_Cat")
        print("L) Sutro")
        name = input("\nPlease select a printer by entering its associated letter: ")
        pr = MPK_20_Printer(building, zone, zone_list[zone][name])
        print("\n___You Chose___")
        print("Building: ", pr.building)
        print("Floor: ", pr.zone)
        print("Name: ", pr.name)
        print("\nDownloading", pr.name, "printer driver...")
        pr.instructions()

        if pr.name == "Sequential_Circus":
            webbrowser.open("https://l.facebook.com/l.php?u=https%3A%2F%2Fprinter.glb.thefacebook.com%2Fprinters%2FMPK20-Sequential_Circus.zip&h=AT0mhmd7k7ocJUyLSlvhlRmR6Pzue83vJNiZLHmv9tDA-j-_VZjE0nKeHhxmXBWW7je6U8ri07b10rwL5Ny54Cj5QD8WhvSGe2PZZr0h68ZCEuw74n0S5DOfk-RsEo8sdkqukmU-aA09dgYqDPHB-lNewWo")

        elif pr.name == "Putting_the_USB_in_Backwards":
            webbrowser.open("https://l.facebook.com/l.php?u=https%3A%2F%2Fprinter.glb.thefacebook.com%2Fprinters%2FMPK20-Putting_the_USB_in_Backwards.zip&h=AT2iIIQWeeO0TBfr9eE528no357KagPKZBxrHosXsKFAGM7qUR97O4RjYjqNos7VIbz1kBLynUFjFspIsCG9_Frk0iJD15wPVHeHpFJxDmkVOxGnGgTQOo2Y_AsI7HfzFI_sDTPDMS5fe3kJWnQw5680o1Q")

        elif pr.name == "Colonel_Meow":
            webbrowser.open("https://l.facebook.com/l.php?u=https%3A%2F%2Fprinter.glb.thefacebook.com%2Fprinters%2FMPK20-Colonel_Meow.zip&h=AT2LEWjqth5zTUQxOE7tyiRCe-VOOHvXdJ3RT9QaWPY9BjZ0Y5Vy3U_nDsQDS9qXvcMxgDLbQrRuzYtPh-n4x5ep5jc-uE3n8aw73UGctztTAqlEcNsNp8a_sBn1RZppaPCTnYU7hlW8JTLY1poyujRyOdc")

        elif pr.name == "Nyan_Cat":
            webbrowser.open("https://l.facebook.com/l.php?u=https%3A%2F%2Fprinter.glb.thefacebook.com%2Fprinters%2FMPK20-Nyan_Cat.zip&h=AT1xBLJ4w9ocbIzQqOgCUf6lpQrT53ESG88FRnqMPKHudiCpYiNZMqw618nNQ3_34YWv7DSlCDvcefB67pX-gStm7odyu6auUY13RKbpDkoTeXlYZmUNYb7RkQeyTojUO6QzH_cNmA5H72Dtwa7pfayEEek")

        elif pr.name == "Monorail_Cat":
            webbrowser.open("https://l.facebook.com/l.php?u=https%3A%2F%2Fprinter.glb.thefacebook.com%2Fprinters%2FMPK20-Monorail_Cat.zip&h=AT09s2eQgoDVh1QZUNgHIlDOgli0TsolH0Fd5htlAhCaaVgxNZ8yuwIPYwnmjsj54FM2KxOQBtdkiNXhu1X4oQ1rYtnX7ePwGgQ1hT6W_qE_PIcKVdUctZu55S7RC-mEv8C5LD0kQoASHobyXDLHgS1To3AWdO-hiWF7mV5C")

        elif pr.name == "Battle_Cat":
            webbrowser.open("https://l.facebook.com/l.php?u=https%3A%2F%2Fprinter.glb.thefacebook.com%2Fprinters%2FMPK20-Battle_Cat.zip&h=AT3BdI0Sr7moPFrLf5YDupfIKUMN-vAXcDEuJxw0Z83LdKeQSBanCHuJlOFOp_riubAOx5esfMVNgPRMM0EU3N51d4f4hFN1I9_gIGS1zDkAS-GzLQjeCgpfGFoRPWDHGmuDAJgDcRO-O4FQrqda3a1QJL0XXE5t832AEoYG")

        elif pr.name == "Kang_and_Kodos":
            webbrowser.open("https://l.facebook.com/l.php?u=https%3A%2F%2Fprinter.glb.thefacebook.com%2Fprinters%2FMPK20-Kang_and_Kodos.zip&h=AT3B35gy9-ebLJDaPAr0pCU6Ut5PTyfVYdDKy8hxgAzg098Un-oyq8aR3doMycrMHv9-z08KybjaV78ntDJGqpTRLdvrJJAS22PXhjvMQjOH6aBCq7QW0MiBS-TLaWlWQlGKjLIVltqh0JwfLvRsSo1WwZE")

        elif pr.name == "Guy_Incognito":
            webbrowser.open("https://l.facebook.com/l.php?u=https%3A%2F%2Fprinter.glb.thefacebook.com%2Fprinters%2FMPK20-Guy_Incognito.zip&h=AT3zyhtEkeXXDstGaz47YRYZuDTfk3a_iyInTQxzeJv_nC9xYM6-fv5DAmQry5i2_-Ced3Bn0BE_F7CtjGneCK8q4DJj1Bx5-_pVoO5HCMRWhV3SPo8WDoAzHUlUCv6sfVmDQjyTFH0Tk8G7icNKRjj2sDw")

        elif pr.name == "Maria_Meyer":
            webbrowser.open("https://l.facebook.com/l.php?u=https%3A%2F%2Fprinter.thefacebook.com%2Fprinters%2FMPK20-Maria_Meyer.zip&h=AT2LdwjmEhFxQaT66netXEEdV5cYz7zBVFtJKuXwQz4s80nwUkiP1UAgcqQvKFXSV5PP0xp2vahSkglNZYkZIM4AR6yqbIB792sjNOnp1-foGKbLN7nxivY8JosrnxFUBxTjssYURxx_VDHQSpWj6-KVq04")

        elif pr.name == "Ceiling_Cat":
            webbrowser.open("https://l.facebook.com/l.php?u=https%3A%2F%2Fprinter.glb.thefacebook.com%2Fprinters%2FMPK20-Ceiling_Cat.zip&h=AT0GYf2RJX2MJ_UDsPtNilJijPTpqaGGQhtv7_95EDu37Hp8n_7R8LkrEhcb2g-EcMc3TCgDTJ7J-VDgQkElfmGUl2agw57UdCa8JX-ydGkfoyj8A1bMlSDLiKQZDi5o2wiylDrEOg2Ya3kxqIL56g3VA9w")

        elif pr.name == "Sutro":
            webbrowser.open("https://l.facebook.com/l.php?u=https%3A%2F%2Fprinter.glb.thefacebook.com%2Fprinters%2FMPK20-Sutro.zip&h=AT1HQNe3VnkApxMqYO0BkzV_ergr4iPfIrWF2pWJddrw2zcjRSQAPEA17vtxHmYYamfpyOlsqMpOrYzn3MVPMrZGu_jCohr0BiAvPOSY17hIRK_S0_0U5e2WHTLHCa5BF9S3MoVQYRsf8EKjpQHUJIZpmPM")

    elif zone == 5:
        print("\n\nMPK 20 - Zone 5 Printers:")
        print("----------------------------")
        print("A) Curl-Up")
        print("B) Get_back_witch")
        print("C) Biaviians")
        print("D) Circle_Limit_IV")
        print("E) Kason")
        print("F) Changelings")
        print("G) Ponyo")
        print("H) SnakeHole")
        print("I) NarcBark")
        print("J) Variable")
        name = input("\nPlease select a printer by entering its associated letter: ")
        pr = MPK_20_Printer(building, zone, zone_list[zone][name])
        print("\n___You Chose___")
        print("Building: ", pr.building)
        print("Floor: ", pr.zone)
        print("Name: ", pr.name)
        print("\nDownloading", pr.name, "printer driver...")
        pr.instructions()

        if pr.name == "Curl-Up":
            webbrowser.open("https://l.facebook.com/l.php?u=https%3A%2F%2Fprinter.glb.thefacebook.com%2Fprinters%2FMPK20-Curl-Up.zip&h=AT01Ahw2TZ9c_n1xo9WVI84MYk0wi79ujokc4HqVwj9R8nktEhnk3yeGr_OBZ8f5IPBkXdOk5ZS0lqNggT2-o3QJ1RiRMWBr9QzskDSaRGJvZiJcctQ8I1_tAGYVcj9-auhZCEmsxoyca7wWP-lJmt6kadM")

        elif pr.name == "Get_back_witch":
            webbrowser.open("https://l.facebook.com/l.php?u=https%3A%2F%2Fprinter.glb.thefacebook.com%2Fprinters%2FMPK20-Get_back_witch.zip&h=AT1218qrdrrQDWPJTNqwN11kSoyoC9EPk_U3xk1eenqQOBi6Srpn7a0YYxUhb_ThhX9Zn5S_O9tp01GzkBDv2LpcCpKkCtLmmVIy5e5HHmwmFu0EMN5OmV4pu5rDLobt3BGCiHXDKJ7peUiQ45SLWOGtTXk")

        elif pr.name == "Biaviians":
            webbrowser.open("https://l.facebook.com/l.php?u=https%3A%2F%2Fprinter.glb.thefacebook.com%2Fprinters%2FMPK20-Biaviians.zip&h=AT15EeMQ_re8wJWx64L5ryunq7tWq0jdghiRvyaK75LJNdGUlLFhqRnMizTnK8qnNww9JWci2Ek8AArVfehxfhzoyOpsBeyDBkmOM6SDN5UWvKp9c2ktS-Yh9ljKj5RrVeKVniv6sq6DaYq6o8aes67Zycg")

        elif pr.name == "Circle_Limit_IV":
            webbrowser.open("https://l.facebook.com/l.php?u=https%3A%2F%2Fprinter.glb.thefacebook.com%2Fprinters%2FMPK20-Circle_Limit_IV.zip&h=AT0sDcXcWgRgyKboO_a-4dBopLztfxOaSplOfESOY5I6bwWkYE1FlKuQ8hzPWyXfM_U1lv9fal9y-JUIbz-jR-Bjqc-bvL5Qifkthxf9uGo1FO67aqWD0mxeNmx2EWKRc_V7KGbO8OlbeUWa-TV0jFE6e9s")

        elif pr.name == "Kason":
            webbrowser.open("https://l.facebook.com/l.php?u=https%3A%2F%2Fprinter.glb.thefacebook.com%2Fprinters%2FMPK20-Kason.zip&h=AT0ku3R5ouVw3MuQz2PefzRC9fbk-BcICL54H_1_E48xBSa2Ab2snOULrzOqUxJOFm22BaDSwDVnQKbUyuTdSulElXHeQ5a3lGuILH5vQl0Jsa9zpt8zdtag3Mfkhc6Vlo4napZP0v6Gpf_v90tSO--b7QQ")

        elif pr.name == "Changelings":
            webbrowser.open("https://l.facebook.com/l.php?u=https%3A%2F%2Fprinter.glb.thefacebook.com%2Fprinters%2FMPK20-Changelings.zip&h=AT083xiQfI46hOI7E_Kp7AV7ehT4rvgEiQdyuStRz-Xc9OjfKvDYjhEC1WyLtnpbVft6yBOg0PzIPpJr2etI0lMgmBZaKBkmndOwPHTJLqxSuDRiJN12lM52wlrK9MPgffZSitRd0IOubHLM3r2M2VXX_og")

        elif pr.name == "Ponyo":
            webbrowser.open("https://l.facebook.com/l.php?u=https%3A%2F%2Fprinter.glb.thefacebook.com%2Fprinters%2FMPK20-Ponyo.zip&h=AT2RvPopu3fd14TsnAq0LdSHgvetVKXvQlHt8n7zk-4EYUz93zDY47b56iPi-ohb6Ru9zyeW1Znqq5hLw5Era0Ml2CVSwrssbms4DKPUfcz7FWTvSGUhd7Wzs5541Mv96NUyiEW-Si-xqVnUs2MZBpkxPU4")

        elif pr.name == "SnakeHole":
            webbrowser.open("https://l.facebook.com/l.php?u=https%3A%2F%2Fprinter.glb.thefacebook.com%2Fprinters%2FMPK20-SnakeHole.zip&h=AT29u3ufM6FeCj_oWn0oWQqE4KQGPcFOffYlSq0EvGhkGuzBksTlefFnkDoz31-eWGvX-gd74iJwFo2QsW_VsBJ1ILfs70lxdVOezgpZE_NDZGeh78aJLtYkMv2k1vf_5ci2_niLkNo4opm-DqNf2zPkcVU")

        elif pr.name == "NarcBark":
            webbrowser.open("https://l.facebook.com/l.php?u=https%3A%2F%2Fprinter.glb.thefacebook.com%2Fprinters%2FMPK20-NarcBark.zip&h=AT2kE4CUdoAfAmeCJjJGfIvDNuEkbF43-qcS9iwSgcM5YT2Z7la3eOCmCpNT0vbOhS9NeliiTVQnPPbabSY9VJYgfZabqcaXbV7fAGoMy0qqfc4NeLsoWXVWF1Vou47XRpC7-cB3TNRt7XgThzC5dR7P5i0")

        elif pr.name == "Variable":
            webbrowser.open("https://l.facebook.com/l.php?u=https%3A%2F%2Fprinter.glb.thefacebook.com%2Fprinters%2FMPK20-Variable.zip&h=AT0IbFhLVc6gKkuKbvSYCFV9I9w-01wRddnyby0xmi-oltk40lPz0hJZfneMMdO6rg0rZmywA9AEsdyIJ_XQknqZiMUbxN1Gmb0a41H3xngpcjD9zqvsMnJQ6dLp6pzaWs6IkSpGOI1XoyR0UNMVXo7fEe8")





####################################### END OF MPK 20 ###########################################################################



#MPK 21
elif building == 21:
    zone = input("\nWhat zone in building 21 (6-9)? ")
    zone = int(zone)
    while int(zone) < 6 or int(zone) > 9:
        print("Please enter a valid zone for MPK 21 (6-9): ")
        zone = input("\nWhat zone in building 21 (6-9)? ")
        zone == int(zone)
    if zone == 6:
        print("\n\nMPK 21 - Zone 6 Printers:")
        print("----------------------------")
        print("A) This_Buildings_Number")
        print("B) The_New_Internet")
        print("C) Three_Comma_Club")
        name = input("\nPlease select a printer by entering its associated letter: ")
        pr = MPK_21_Printer(building, zone, zone_list[zone][name])
        print("\n___You Chose___")
        print("Building: ", pr.building)
        print("Floor: ", pr.zone)
        print("Name: ", pr.name)
        print("\nDownloading", pr.name, "printer driver...")
        pr.instructions()

        if pr.name == "This_Buildings_Number":
            webbrowser.open("https://l.facebook.com/l.php?u=https%3A%2F%2Fprinter.glb.thefacebook.com%2Fprinters%2FMPK21-06-A-This_Buildings_Number.zip&h=AT1J43at26XXN8h8cAGyHH-Y6HJntR422xW2fXP8Kv-8EXsRlTD-PLgmSsDtmWzyW-tjRpl8Yz_-gW0AMn2lhKoMpbjDBNMER_vAzKxk8vK8bASa8z_lC5Pz4Z0O2khRC8jZoDlXnlp_rjanJ5JEEkXyRLM")

        elif pr.name == "The_New_Internet":
            webbrowser.open("https://l.facebook.com/l.php?u=https%3A%2F%2Fprinter.glb.thefacebook.com%2Fprinters%2FMPK21-06-A-The_New_Internet.zip&h=AT29kwyaR63tKMcPgzj0Ap0M5Oou-5GOkVRgMg6ehnLj5Se1OVpgXu0bh9dkxbyjuLpglsIC8iUxpqIRA8rowGY9zHyL_r3Rpu6MHw4hk3xSnX_UsLXESVuFoJbaj3yb6fIGbpQQjTEVCYpW05irg3YNxZA")

        elif pr.name == "Three_Comma_Club":
            webbrowser.open("https://l.facebook.com/l.php?u=https%3A%2F%2Fprinter.glb.thefacebook.com%2Fprinters%2FMPK21-06-A-Three_Comma_Club.zip&h=AT0e8FveV6qjeRnyR_CtZR3oEx86epHFYnFKhQ5krMdPMmXLdxD-gEv54_Es1K8jlcmK1w7SVRerUTxyKSA-nzozAEcTr1XjHp2Kqxj0QfInWfsEz4f8YxR_Hwz7xUsy5PaO0Qpe76XiG7eyxt_3VVSOL2E")


    elif zone == 7:
        print("\n\nMPK 21 - Zone 7 Printers:")
        print("----------------------------")
        print("A) Zyzzyva")
        print("B) Will_It_Blend")
        print("C) Press")
        print("D) Rock_Star")
        print("E) Unknown")
        print("F) Youre_Frozen")
        print("G) Zurg")
        print("H) Were_Being_Kicked_Out")
        print("I) SEViche")
        print("J) Tea_CP")
        print("K) Ursula")
        name = input("\nPlease select a printer by entering its associated letter: ")
        pr = MPK_21_Printer(building, zone, zone_list[zone][name])
        print("\n___You Chose___")
        print("Building: ", pr.building)
        print("Floor: ", pr.zone)
        print("Name: ", pr.name)
        print("\nDownloading", pr.name, "printer driver...")
        pr.instructions()

        if pr.name == "Zyzzyva":
            webbrowser.open("https://l.facebook.com/l.php?u=https%3A%2F%2Fprinter.glb.thefacebook.com%2Fprinters%2FMPK21-07-D-Zyzzyva.zip&h=AT3nnJZtaJ6QYJATCrD23PmMo95RZV6CapDLODNrx0iCcHwz-SBudaco9BneG-OnrLnL34bRWA6pEzcq-ESmAAmHDbCbKWnUjvHvDh4HduDjPkMLj-5evNXAVaywINFxbo_1qhCgfrR9iMsZMaQ_NslhACE")

        elif pr.name == "Will_It_Blend":
            webbrowser.open("https://l.facebook.com/l.php?u=https%3A%2F%2Fprinter.glb.thefacebook.com%2Fprinters%2FMPK21-07-E-Will_It_Blend.zip&h=AT3Ss3t-iTXw2Fu3WqXP191O-jZ38lILcWjcXrgRz3WIkN_R5G63mPrkrokbNMNnI6UzdQPUvsJXDJ80cXQg66FLY8Yt9-Z_vZ0CDmm1oMqmhhIh7vDUnpw2G9evINLK3o07pK8vIf2yeDYvm-uPIxITE5g")

        elif pr.name == "Press":
            webbrowser.open("https://l.facebook.com/l.php?u=https%3A%2F%2Fprinter.glb.thefacebook.com%2Fprinters%2FMPK21-07-D-Press.zip&h=AT2MGpHdPFIESdV6r0z_wtwFr-DhW0XV2POm8ndtPmS7PSAQOYbAdmM5aCJAXAoGc_2CWTlprDysNWPCmOPmk0Fr6oMRcnskYyySHzcHITJMQZiCRqY-G9f--3rsYS2Fo2PlLoaPt_1ldFU0jguAsgOo27U")

        elif pr.name == "Rock_Star":
            webbrowser.open("https://l.facebook.com/l.php?u=https%3A%2F%2Fprinter.glb.thefacebook.com%2Fprinters%2FMPK21-07-D-Rock_Star.zip&h=AT3AOGfZfJCKjdoLTihpytg9hpsk0jcpv8CD28EggCMPPoTd2UPoKCsNz3pUeah9SBsXA4rGbxL-MC-BhDGeM2HxD7Q63mw4-FdgYVEFtXu0dILltlBectpTYCDhA9mQHZWNP5x508hOR4RN0rjq4hgHK3g")

        elif pr.name == "Unknown":
            webbrowser.open("https://l.facebook.com/l.php?u=https%3A%2F%2Fprinter.glb.thefacebook.com%2Fprinters%2FMPK21-07-D-Unknown.zip&h=AT2I7v7WTdPCDdC6_pC8Kn0v0zTub15PSc44q9gKKzVCinwAcJYFrcxVxnKEHjsPlvkX_rVpFSfwEVU3ay4RDpYj_RiigGTF3ioQjzuibGSSbNQx_tOfqzOEpBGCzn_SlymzufJ6CkYCVQLP5VJ6SHhr9jaZSq_VMdtKWUVZ")

        elif pr.name == "Youre_Frozen":
            webbrowser.open("https://l.facebook.com/l.php?u=https%3A%2F%2Fprinter.glb.thefacebook.com%2Fprinters%2FMPK21-07-F-Youre_Frozen.zip&h=AT1zwtKbs5uhSAHy3fhqYT7zdj1cWJ_UIZERNNEwe6fXkFlFGbPsszgUSvaGC6PBCV7-7gsjAFgPL1BW_g9iDnDTY1zs0FCwATz79uuehZIwYzDHvqYifa_JrfTVVb1hSczDUs8yu7K8noxzgCnnGZFqpl0")

        elif pr.name == "Zurg":
            webbrowser.open("https://l.facebook.com/l.php?u=https%3A%2F%2Fprinter.glb.thefacebook.com%2Fprinters%2FMPK21-07-E-Zurg.zip&h=AT14wUL5fV6HHL0y3myzyKBza6v4UajJEtBeUQz46bN7RYTzZW_tKWnS2KJ_1HOtBnCEKq8LJRo587a0l7QypovKB5Tj2dpHi4relyUfEy86RPN1NpCQWK_4-f-5J17PrqWJTJIz8FoaV6Yzir_KbKtJ-yw")

        elif pr.name == "Were_Being_Kicked_Out":
            webbrowser.open("https://l.facebook.com/l.php?u=https%3A%2F%2Fprinter.glb.thefacebook.com%2Fprinters%2FMPK21-07-F-Were_Being_Kicked_Out.zip&h=AT2EzLtbLxBKmCR6l5FfpI5IGqyCvcU-wVQ_F3CMCIChGn6zV5wP1AJHmHx0vGDodT3dFG6EejTA3XGuqP_YqecBi_y1SZzHWemkWs6vqFG3LMKC6BsmvhmHS6sUwE2y0v58n0-aYDFgUNahPJMA-SB9GcA")

        elif pr.name == "SEViche":
            webbrowser.open("https://l.facebook.com/l.php?u=https%3A%2F%2Fprinter.glb.thefacebook.com%2Fprinters%2FMPK21-07-ME-SEViche.zip&h=AT1-S_GH-pUozUEqltBqpRJasBcg-ImMXH1zLSZ8Ou0gxL2Y5S_ZHDmyEstQGqC3x-jYXWafrxSF-3zWQ7hkrYjif2qd9Li92wzIEwqIji0gdXLB-cxggCDxyZOYGdNKTPZrxGIlPEg5hZUDOjtijVyoRFY")

        elif pr.name == "Tea_CP":
            webbrowser.open("https://l.facebook.com/l.php?u=https%3A%2F%2Fprinter.glb.thefacebook.com%2Fprinters%2FMPK21-07-ME-Tea_CP.zip&h=AT06BJCoOdp2tU_NXmLXv7NCBnJqqn8M5Gjt6L3qn4UsJiv2-x4Yn7dLoFWkpEkW_Fx8sVgzlWpJmMBYXzuemLcM0HGJmaUjDIlMLdzMNvkCDBHXi7ieStTFnypwf6TISko-b3NaR6CvaJ3aN6jnEZiZm2s")

        elif pr.name == "Ursula":
            webbrowser.open("https://l.facebook.com/l.php?u=https%3A%2F%2Fprinter.glb.thefacebook.com%2Fprinters%2FMPK21-07-ME-Ursula.zip&h=AT3RqjxOzTj9x37tez7YpLB2jjVk1Y8_MkQp3usrYqXh6DviQ4YiuwGuOntGObMp4hwSK9Myz2sW0ftyXsj9DpW5O0KAnda1S749cp6woP0_tGElnR6P86c6UM2Ick6v4b6D2Byjm5Xg3qRgfxwQ6M6m7eU")


    elif zone == 8:
        print("\n\nMPK 21 - Zone 8 Printers:")
        print("----------------------------")
        print("A) CommuteFB")
        print("B) Yoko_Ono")
        print("C) Spock")
        print("D) Sulu")
        print("E) Uhura")
        print("F) CJ_Cregg")
        print("G) TurnCreativityIntoCommunity")
        print("H) Yes_Definitely")
        name = input("\nPlease select a printer by entering its associated letter: ")
        pr = MPK_21_Printer(building, zone, zone_list[zone][name])
        print("\n___You Chose___")
        print("Building: ", pr.building)
        print("Floor: ", pr.zone)
        print("Name: ", pr.name)
        print("\nDownloading", pr.name, "printer driver...")
        pr.instructions()

        if pr.name == "CommuteFB":
            webbrowser.open("https://l.facebook.com/l.php?u=https%3A%2F%2Fprinter.glb.thefacebook.com%2Fprinters%2FMPK21-08-CommuteFB.zip&h=AT00tXaxar2whMZ11LAhKgOCIep6RMv2wSBRxTMAYFA0CCCHOpA7efpzIE-2hhL7z-d_Tsk1zXlg7nKJ2O166SpLZQJj94yxfdFK45xR0GTBGtbx7FQkgr2Uww6fDwDYpFoIXEd7-kbuhHK26fyjqLLEvO8")

        elif pr.name == "Yoko_Ono":
            webbrowser.open("https://l.facebook.com/l.php?u=https%3A%2F%2Fprinter.glb.thefacebook.com%2Fprinters%2FMPK21-08-J-Yoko_Ono.zip&h=AT0Q-cSCvhajNdBHLFajbCbHZXbU43n4kD8K9LAHhRZK_m0T8hJBzrBR8HUiM14nGm1oo-SgJSFpjPBUjBDVmcO64wDT3Ab8npbEydI517F-vHNYIuP1gQ0Jcp60fvFYiyU4_ofqi9O7IHyojwj6NyH7ae0")

        elif pr.name == "Spock":
            webbrowser.open("https://l.facebook.com/l.php?u=https%3A%2F%2Fprinter.glb.thefacebook.com%2Fprinters%2FMPK21-08-K-Spock.zip&h=AT2uRera2OYXfoAzdKZErQO8TR_tBwNtEN546DoKyPZh7lbupY-hbJGprtnY-Q4px-KoPskIIeP-k1cnIgJoOSM4IFWc3pkFor-iQvrcXl40EbpIkU4Nwn5Zayp0p6xzdzo_7qIhBuUEEf93gREmAs2w8jc")

        elif pr.name == "Sulu":
            webbrowser.open("https://l.facebook.com/l.php?u=https%3A%2F%2Fprinter.glb.thefacebook.com%2Fprinters%2FMPK21-08-K-Sulu.zip&h=AT0Nrsai9yVtB4tay95w8yFF_KmaekoOHc2xx9Gv04JBotpw2Q9Kr9bJDqBwx5I3gqRrOELg7svXNN1_ujxanhJLowaBnvLyUFcfRS5wT4aAOUdAEAljkazRkI00Z9-Fh1hIQNFkndeaXE7ykRLkIdrrzpc")

        elif pr.name == "Uhura":
            webbrowser.open("https://l.facebook.com/l.php?u=https%3A%2F%2Fprinter.glb.thefacebook.com%2Fprinters%2FMPK21-08-G-Uhura.zip&h=AT12CkowAPnxZZ133BlsP9rtOkeye67LvzVr3FIAlLo9xpHZModtAJwVvLk1S3TGVV45w18atsgmwD6TpZcoKemGHgYLvYt2I8rhXX9i_nOeePWHu7o4LGIWbadWuWCnhNxOFrgsgyv3tPPOY1bJTGw9IMo")

        elif pr.name == "CJ_Cregg":
            webbrowser.open("https://l.facebook.com/l.php?u=https%3A%2F%2Fprinter.glb.thefacebook.com%2Fprinters%2FMPK21-08-K-CJ_Cregg.zip&h=AT2OdwG6Cniz9ZjR2Z9o201j-lL-mQHAdNS-OUP1ebmvZ4wsqJkino13kLIXVZn1As-_bdPoOewiA-F1KKBMM0WUeUq5EJonw1JfNSHiQAzEyOSDmIQ4KtR0Gfdb_TRQIkGJ1237K1GHG_7SZ9CFlilYzqc")

        elif pr.name == "TurnCreativityIntoCommunity":
            webbrowser.open("https://l.facebook.com/l.php?u=https%3A%2F%2Fprinter.glb.thefacebook.com%2Fprinters%2FMPK21-08-L-TurnCreativityIntoCommunity.zip&h=AT3hwMiHMiPSUZCt7KU3NQYYinUeYdtFOmPNMGAtVXNwy250bCaZ_Eu3aixgFM2U7UDrE1KFiwODMafV7PsqSqTx7q07U7Qh61-CLOG-15O-YzFOlVH64AUkG9yt5rOYobs6NXybTMwUqV2fQGqqOk3LHdk")

        elif pr.name == "Yes_Definitely":
            webbrowser.open("https://l.facebook.com/l.php?u=https%3A%2F%2Fprinter.glb.thefacebook.com%2Fprinters%2FMPK21-08-MG-Yes_Definitely.zip&h=AT3jixuaDrVhaU1ziWQz7HlVyu7sHHcREXn813eQDqMx6n7tLJbC-j2V0aHEeeMGvHZCED6ljDOnOA65DPe01LTRrF4zqX4fATsgnBLVoyqi7YUhm7LTblLSR7WHDzMHeBWjn3uPs7N9UhI3qRJV1FtG6tQ")

    elif zone == 9:
        print("\n\nMPK 21 - Zone 9 Printers:")
        print("----------------------------")
        print("A) Villain_Pub")
        print("B) Weasley_Wizard_Wheezes")
        print("C) Ursulas_Grotto")
        print("D) Twilfitt_And_Tattings")
        print("E) Vault_101")
        print("F) Wily_Fortress")
        print("G) Victory_Road")
        print("H) Yoshis_Island")
        print("I) Blue_Fish")
        print("J) Local_39")
        print("K) Jackal")
        print("L) Ship_Happens")
        print("M) Judith-Love-Cohen")
        print("N) Satoshi")
        print("O) War_Heads")
        print("P) Stilton")
        name = input("\nPlease select a printer by entering its associated letter: ")
        pr = MPK_21_Printer(building, zone, zone_list[zone][name])
        print("\n___You Chose___")
        print("Building: ", pr.building)
        print("Floor: ", pr.zone)
        print("Name: ", pr.name)
        print("\nDownloading", pr.name, "printer driver...")
        pr.instructions()

        if pr.name == "Villain_Pub":
            webbrowser.open("https://l.facebook.com/l.php?u=https%3A%2F%2Fprinter.glb.thefacebook.com%2Fprinters%2FMPK21-09-N-Villain_Pub.zip&h=AT188woUzyZf_NreFSJ6VvB73q_0yBh2MW1AqEskBt9yYcOmHxaWz5K_nHRX2FjW8a0cM9wWHukIO7-tO1AeLKudE5obkWgwwLH18fwydSSfLplscpltwbCua_fT6HlcJQ5dGMvuM6244sagQLuziYYprqA")

        elif pr.name == "Weasleys_Wizard_Wheezes":
            webbrowser.open("https://l.facebook.com/l.php?u=https%3A%2F%2Fprinter.glb.thefacebook.com%2Fprinters%2FMPK21-09-Q-Weasleys_Wizard_Wheezes.zip&h=AT3TOGWZPAyvufoTiav3lZE1-2-tpldoc_cSx7n1KeLJbUWvaTIhOO5rGZINm2BdtDN1e_qPbBAN6FcF7UI6bsFtJVccJIamhRXy1RN1K6932rTK7jAD34N7-lJ3VYHZgJy6EHHZ_tzIGtTd31XmxuAoNgY")

        elif pr.name == "Ursulas_Grotto":
            webbrowser.open("https://l.facebook.com/l.php?u=https%3A%2F%2Fprinter.glb.thefacebook.com%2Fprinters%2FMPK21-09-N-Ursulas_Grotto.zip&h=AT2Czoi_QBLa7ZyQxKAHLgoPMZtMz1e2GfWQILNAvwHTCmr5tYrpLf5WoBlBK4j6j64RvnU0V1s12cYTHWb8GbCh8b7-ZbKMjaaeD7mrgMqxtpf8gN0YUFLSDULX94EE5gDxhTb7t9VttFcQPH4D0-Cyr-A")

        elif pr.name == "Twilfitt_And_Tattings":
            webbrowser.open("https://l.facebook.com/l.php?u=https%3A%2F%2Fprinter.glb.thefacebook.com%2Fprinters%2FMPK21-09-Q-Twilfitt_And_Tattings.zip&h=AT1FyOMyLGljqu42RfEA4tnkFisEqbcJZ7ncJ5Gwo9RJVbL_mQKCXBYpgsIR-d4mmxRLb9i26CTBimIL-Xkdp6VANEtJ2WtLTLCiyLM4xc_n7Qz1qRxktEXmcEtH_spEbsLm2MqyQNCYLfgv1GsmmmB64mk")

        elif pr.name == "Vault_101":
            webbrowser.open("https://l.facebook.com/l.php?u=https%3A%2F%2Fprinter.glb.thefacebook.com%2Fprinters%2FMPK21-09-Q-Vault_101.zip&h=AT3wOQeK9ZM995fOIodobvMKqqAlkGriSnnBmStoLFl4XYhBzJNarbv-WAyFnuGqs9icLmJn2-tdKnbl6GEJNa-TQXtoeAI8NPV_UEin-zvnzWpH-_AQUlnepNEM39HwlbSdCTnsTc_WahzGimPELA-BLAc")

        elif pr.name == "Wily_Fortress":
            webbrowser.open("https://l.facebook.com/l.php?u=https%3A%2F%2Fprinter.glb.thefacebook.com%2Fprinters%2FMPK21-09-Q-Wily_Fortress.zip&h=AT2Vfl-xYikweJoTgCTuGb8SP86Wq64DjiwLHd4WZ_1NGGNb1sMBNHZ5LTJl1RUqgxTTP5QeF-_oKTXWMkvllbWRzFee9w_YoEGH8S1SY5Ldgk-sMiwbs_0-ARv8BME4I0C-_rp8YjSeO8aa_X53hjBqrOk")

        elif pr.name == "Victory_Road":
            webbrowser.open("https://l.facebook.com/l.php?u=https%3A%2F%2Fprinter.glb.thefacebook.com%2Fprinters%2FMPK21-09-Q-Victory_Road.zip&h=AT3-gWZjr_0MGf3b5csgGKpzK9MHZ7AhvzIuAmdMyYPHDJ2Y-wTsBsu4fZ3Sr-Q7CmV7XpCS6lj8wVKWPATQ10-XpQzT1QJsKPQZVAwwLkhs8JsbufqQ8WQaTddlZJIXQAPNgQfa9eZOmK1l3IgaEi_mDQU")

        elif pr.name == "Yoshis_Island":
            webbrowser.open("https://l.facebook.com/l.php?u=https%3A%2F%2Fprinter.glb.thefacebook.com%2Fprinters%2FMPK21-09-Q-Yoshis_Island.zip&h=AT1estCpsIIIC6s4rUBHGHOy2t0gm-Uh0JIXoTzan-8dIqqfU5jPmVHmDOI_c6ygNH-BDQhLD8jST1k-kv9lK32EgRQKQXPitL9rNQIyavJyVMk3c1QRG3_2jK-NXdpr2RAScIkZdpOIGiJHduJuzZd42yM")

        elif pr.name == "Blue_Fish":
            webbrowser.open("https://l.facebook.com/l.php?u=https%3A%2F%2Fprinter.glb.thefacebook.com%2Fprinters%2FMPK21-09-Blue_Fish.zip&h=AT2dlmD8OGBR-HnePeqGcVzVQS7bhbxjM9QMRAhY6LdCM0y46ZBKejDM0JYJHjL8vLGSIJnkd7u4QuQbaw62HzbnsrLR1TYP62NqjBTbFKmICNlN_BT5-klFpEi2GY6eS7OWsLiy37fex7wbKkMM3ISm7NI")

        elif pr.name == "Local_39":
            webbrowser.open("https://l.facebook.com/l.php?u=https%3A%2F%2Fprinter.glb.thefacebook.com%2Fprinters%2FMPK21-09-Local_39.zip&h=AT3_OKjXX-JPCVC9m0JZ_8b2xOwrnGN9ZRMA7ngwa3lzH7k1IMvxoJ9UPkjJDAOA34q0K3MUHC2wieJxy3fLRkhbjEKtApiaZCtvqFkL-1emATRvRz-iZpC2hE8fyE07aikLG0m3oYIg1gkzvXmLJ3pha-c")

        elif pr.name == "Jackal":
            webbrowser.open("https://l.facebook.com/l.php?u=https%3A%2F%2Fprinter.glb.thefacebook.com%2Fprinters%2FMPK21-09-Jackal.zip&h=AT2PCunmxoqAZ5FHVIaTNKMXEgr2jpDGCYHr4MWXjouMPW606lagpQlvvU6bQv3PGk_s_hWj0TQslEswmlSAUY6z22nB4gqqw6pUf4EDIbCvXlcwan2jCqfQvPMPVV41-4stgmCm0VBTvmcJqOTPzG9ZQgLBQKd9QhBtDKDk")

        elif pr.name == "Ship_Happens":
            webbrowser.open("https://l.facebook.com/l.php?u=https%3A%2F%2Fprinter.glb.thefacebook.com%2Fprinters%2FMPK21-09-N-Ship_Happens.zip&h=AT3knbfiMvwZYzFMeUsZj4utGI8xVEc2-8nK0nKB5Acju-zGBTLYbMAIkhY7uTSDPn321OFvawcxIJ7EIcZ19CR5_JGiCK0DcYKVWKAt7Z6eN7N4f2t4RXNb8o_U7Ab1rSPM49c4bP1ryFHJIniJlpigBCE")

        elif pr.name == "Judith-Love-Cohen":
            webbrowser.open("https://l.facebook.com/l.php?u=https%3A%2F%2Fprinter.glb.thefacebook.com%2Fprinters%2FMPK21-01-Judith-Love-Cohen.zip&h=AT3gkn0S1GUYPHF6P9FfCx8VyepeE7ZVMi7MPvdM28LQeAgioBfIUM_hR8E9OAH1wpwjE9g3mIwYhVpzL7yB1c17jd76xQC_6_CwZWD5Xl3H-JaiFSu0c1GfD86HKpAhgbIq0an15Dzjzf-Pj0y3dF64QgU")

        elif pr.name == "Satoshi":
            webbrowser.open("https://l.facebook.com/l.php?u=https%3A%2F%2Fprinter.glb.thefacebook.com%2Fprinters%2FMPK21-09-MQ-Satoshi.zip&h=AT3G3tki9jHstI28X5gEs9S1Ks7ZYb3FYemVO-_xu-rdV0UZC9ZGJ6RqGZVHZIWW4I2IH9UrRXKeGxF26WnUGQSDkXrRdlxvRdCJUj-6RW7z3XJMClkVivNzNQSJZ7jyVtx9nIrBxobkf2jz1XViPrPNbt8")

        elif pr.name == "War_Heads":
            webbrowser.open("https://l.facebook.com/l.php?u=https%3A%2F%2Fprinter.glb.thefacebook.com%2Fprinters%2FMPK21-09-MN-War_Heads.zip&h=AT0RaVTqOSmu0kZJhVXEcQawLCkPriq9dTga7so6tRSBPj1lkn5rDCy7dLnaqM_7B0xidqzfx29IQSQ0qH_S3dEwjQLG7gV8Rb1FAz2YOTcpJtN8Sd1ygFAwKzr7ZB1ij24XdlADySYiDNbTdrHErbTB8xM")

        elif pr.name == "Stilton":
            webbrowser.open("https://l.facebook.com/l.php?u=https%3A%2F%2Fprinter.glb.thefacebook.com%2Fprinters%2FMPK21-09-MN-Stilton.zip&h=AT1eRQTYBTOAOoJ5dIk8wN-U1cv3ugGdiuBIA9JOEoHbFuxZsglI160IaR1Ac2ftm1JunQDKB4q1ppXNCTqWufKafJBzVplwRyZAsNelAO6FIdwIJryHGqT87VKThakHtouHT18gmK7L9rx61DgMe-SqbRA")



####################################### END OF MPK 21 ###########################################################################


#MPK 22
elif building == 22:
    floor = input("\nWhat floor in building 22 (1-4)? ")
    floor = int(floor)
    while int(floor) < 1 or int(floor) > 4:
        print("Please enter a valid floor for MPK 22 (1-4): ")
        floor = input("\nWhat floor in building 22 (1-4)? ")
        floor == int(floor)
    if floor == 1:
        print("\n\nMPK 22 - 1st Floor Printers:")
        print("----------------------------")
        print("A) Pidgeot")
        print("B) Raticate")
        print("C) Beets_of_Burden")
        print("D) Arbok")
        print("E) Nidoqueen")
        print("F) Psyduck")
        print("G) Butterfree")
        print("H) Peaches")
        name = input("\nPlease select a printer by entering its associated letter: ")
        pr = MPK_22_Printer(building, floor, floor_list[floor][name])
        print("\n___You Chose___")
        print("Building: ", pr.building)
        print("Floor: ", pr.floor)
        print("Name: ", pr.name)
        print("\nDownloading", pr.name, "printer driver...")
        pr.instructions()


        if pr.name == "Pidgeot":
            webbrowser.open("https://l.facebook.com/l.php?u=https%3A%2F%2Fprinter.glb.thefacebook.com%2Fprinters%2FMPK22-01-Pidgeot.zip&h=AT0KpxEL9QGASAtTYItLRKZgdXycgt6Tdrui5DZmiBH--beWm0addI_puKQaEzpq4MIy65jYq-cNde91CuxDhkAscGmI13XQw8Jtlu0HiJbB44hAmJomn7Lvr4yueQ9mxoAhMGG47-XrCQIeQ0WKBj9ZadLNenxGyjg6W6En")

        elif pr.name == "Raticate":
            webbrowser.open("https://l.facebook.com/l.php?u=https%3A%2F%2Fprinter.glb.thefacebook.com%2Fprinters%2FMPK22-01-Raticate.zip&h=AT0_R2LnV-4yHVobAnKi_gWA8JV994DjQYJR17cf6QCnLslRK_9e0aD-OmSKboOhUHOWGWoOE00LGaAQBv3Jd45DPJgsSGzDCeZtr5_elwphc_J3NUpkYgA0_1XBNyCNe8wxf_54faXK0MbwEFcewfm8Hw4")

        elif pr.name == "Beets_of_Burden":
            webbrowser.open("https://l.facebook.com/l.php?u=https%3A%2F%2Fprinter.glb.thefacebook.com%2Fprinters%2FMPK22-01-Beets_of_Burden.zip&h=AT1FRAtywV3DF233t-3XjPSSjPi8XQou47uKiJZjzG-y2BpTTd1W0qx98bvT3BX-5gNKSIzQUMNGO3FkvndpeJhpMCmfPqmjlRaazDhzu_WsCjEtw0fnYXJn6TdKCyfMCOeG8N_1y0FbO7f0uUY55zEOfI8")

        elif pr.name == "Arbok":
            webbrowser.open("https://l.facebook.com/l.php?u=https%3A%2F%2Fprinter.glb.thefacebook.com%2Fprinters%2FMPK22-01-Arbok.zip&h=AT2OKZkhMK1jQzHoSLa21kA8kQ-PIOAKVqqOuo6AEL--fibv9abKmlQlLQnB-dUQxVLDmtT78LzQFMqM7DLhJ1hTgRy3eHt-hAC2K86u9vMAVZ-UzD4TyOlqVcLXUa_HSxI2oK78RV5vaOTQPfen5lqmcmA")

        elif pr.name == "Nidoqueen":
            webbrowser.open("https://l.facebook.com/l.php?u=https%3A%2F%2Fprinter.glb.thefacebook.com%2Fprinters%2FMPK22-01-Nidoqueen.zip&h=AT3gcchNNBjZMQqKDTtB3xSfwHNQnOG2wkehdPLonahlLPl2YbbVyDPHl4_NcYezf-nEFTRTrvzh3DjAYtuAjxJj-IC3N0WNnddmIGZC5kIjx_3ohZ8NqJyeKdUPS55JnAWiz2eLtBgg75geUGm7NTj_Ld4")

        elif pr.name == "Psyduck":
            webbrowser.open("https://l.facebook.com/l.php?u=https%3A%2F%2Fprinter.glb.thefacebook.com%2Fprinters%2FMPK22-01-Psyduck.zip&h=AT0vI02nQ_J2p5mqAdkafNh_jwZmffwtBWmvOUN8lSp4aOKGx7-ctjEFRSUZY06iby9P2j7neX1n8nwHs8qA3W7rA0VyNdAxOvwsouVGWHWPF7nFSIuGk_F03uN31qnjZt8yuhIJPq8uOb1XlOaMr1mS8_o")

        elif pr.name == "Butterfree":
            webbrowser.open("https://l.facebook.com/l.php?u=https%3A%2F%2Fprinter.glb.thefacebook.com%2Fprinters%2FMPK22-01-Butterfree.zip&h=AT3G4CNWGed-6KbZFezTTfQVllAbwN9DTCtsZTM3zgVi00SCeLx-6zTUTUcrP6sthEbPADK7svLvIXu-iLPPos7z15hJeoXN2dKP0AIK0-Vf0Ha4dVeCEPI9sRtSC9TGbKo4k0wJVmCShJe7TSytYPlYOhM")

        elif pr.name == "Peaches":
            webbrowser.open("https://l.facebook.com/l.php?u=https%3A%2F%2Fprinter.glb.thefacebook.com%2Fprinters%2FMPK22-01-Peaches.zip&h=AT3FSnJf9Dwpgf-7s0lPfjY1NKddfw6tC7OO08NbF6Y5GddDrMCCGENH7AnsWs75-npTdeECQjVBwDMgX4swclTtV6RLytyPkHAaRuzjE76h-RaGaCSpsyyNk4IuzlqesURq36lLIRnHGHoIyTgMULwxVNo")



    elif floor == 2:
        print("\n\nMPK22 - 2nd Floor Printers")
        print("----------------------------")
        print("A) Lithium")
        print("B) Chlorine")
        print("C) Helium")
        print("D) Magnesium")
        print("E) Potassium")
        print("F) Shrimp_Tempura")
        print("G) California_Roll")
        name = input("\nPlease select a printer by entering its associated letter: ")
        pr = MPK_22_Printer(building, floor, floor_list[floor][name])
        print("\nYou Chose:")
        print("Building: ", pr.building)
        print("Floor: ", pr.floor)
        print("Name: ", pr.name)
        print("\nDownloading", pr.name, "printer driver...")
        pr.instructions()

        if pr.name == "Lithium":
            webbrowser.open("https://l.facebook.com/l.php?u=https%3A%2F%2Fprinter.glb.thefacebook.com%2Fprinters%2FMPK22-02-Lithium.zip&h=AT1Sua4WhvEpC_KFZL7wF85wzcNean3EUythDVmLwk1C-MxyV4YWhka-CZIRmUHOFHD-M3u93A1X43Isq2wSWlgQDwgGU5IEfWa66gjbC8v9xz7P-aoddFr1v3XCqGQbK0axlTOuqb2o8vEGsq5KOxQCGFw")

        elif pr.name == "Chlorine":
            webbrowser.open("https://l.facebook.com/l.php?u=https%3A%2F%2Fprinter.glb.thefacebook.com%2Fprinters%2FMPK22-02-Chlorine.zip&h=AT1tCLsW5ouv-IylAeOEOkA_feAabSbCLy42SMZNaQYFM83VaNEfOBsLD5EKqQKeV21KZZZOih1hoTCpOyqk0swB5qhQ_urh3RqfBN7KNxxoYyymlKDURQ_3JZQ5rQGfR2-Oci3RXA2mk_Gw5naUiMTPLNo")

        elif pr.name == "Helium":
            webbrowser.open("https://l.facebook.com/l.php?u=https%3A%2F%2Fprinter.glb.thefacebook.com%2Fprinters%2FMPK22-02-Helium.zip&h=AT0I33aPzTk_vRTKXaGjPZDOcHy4roTSuCFqT0LZdWaIRcjrkTM_mx6Rt8h6xXYCNJyi4fRQ0-97P_Af4Sc-ubhZM97KKjmYyptEjaYzTExBpCnck_fnpjOV61qFZamfNuA4VuJo2w8K0pu0wYAsMItcE4k")

        elif pr.name == "Magnesium":
            webbrowser.open("https://l.facebook.com/l.php?u=https%3A%2F%2Fprinter.glb.thefacebook.com%2Fprinters%2FMPK22-02-Magnesium.zip&h=AT2wLrYcg8yx1_YdYF5kRAeAjdEqE-3oFeviFCrVufnVjyp3wqaRHAWckMSuLltf6rr0zyMLnYAnIL_LVUjX2C7Z3X5m-TOBGSFgmXTZ37Vipr4s9Zf9wkbd9chmTPcuWmRanwv7ENrCBXND7hYe4TDmPCU")

        elif pr.name == "Potassium":
            webbrowser.open("https://l.facebook.com/l.php?u=https%3A%2F%2Fprinter.glb.thefacebook.com%2Fprinters%2FMPK22-02-Potassium.zip&h=AT2D3xtytg5t4nwsi0p4kNWKwvTKx4gdo4-MBvUm2UabWHc4lbutV59_LVoUQgx7-Ipb3BuYLtT0sIrjtQDmszWMMLS6KTJyE17xn368OEtKh9Sx8N1SwWlsO9efJF9H4iOdkb-AwxpX3AekKnIUJyrSPSI")

        elif pr.name == "Shrimp_Tempura":
            webbrowser.open("https://l.facebook.com/l.php?u=https%3A%2F%2Fprinter.glb.thefacebook.com%2Fprinters%2FMPK22-02-Shrimp_Tempura.zip&h=AT06AN3GsqUHlG5JxJR2_yqWtTmVkabpZ7LBpeGXumQxCRcxGq9hko6CR8HbJEfrmTL_6JKJI6_bpS3GCt_Zl-5Uj9iQeU8aQuoKWKbtIzOUjukjAxAqCcX9qDBiqlTVwLXEaktUb_IGNx5QvXrRa3H1Wgs")

        elif pr.name == "California_Roll":
            webbrowser.open("https://l.facebook.com/l.php?u=https%3A%2F%2Fprinter.glb.thefacebook.com%2Fprinters%2FMPK22-02-California_Roll.zip%3Fver2.0&h=AT2K8CA4cpBKWqm-JQiP4ljI262H_LYiG_6jU141K7AjCZQVJj7eYBIpTIJIqal-VKGEAngCLuN1cekjBPsfQDJn0kMixB3bGn49VKpzAVpD8-FQo4DL-naxBfmjOKbyuz9W9lzme1uv_4EEx2Rx5EbvmnE")



    elif floor == 3:
        print("\n\nMPK22 - 3rd Floor Printers")
        print("----------------------------")
        print("A) Hollyhock")
        print("B) Animalia")
        print("C) Go_Dog_Go")
        print("D) If_You_Give_a_Mouse_a_Cookie")
        print("E) Miss_Rumphius")
        print("F) Disagree_with_The_Characterization")
        print("G) What_Problem_Are_We_Trying_To_Solve")
        print("H) Countess_of_Grantham")
        name = input("\nPlease select a printer by entering its associated letter: ")
        pr = MPK_22_Printer(building, floor, floor_list[floor][name])
        print("\nYou Chose:")
        print("Building: ", pr.building)
        print("Floor: ", pr.floor)
        print("Name: ", pr.name)
        print("\nDownloading", pr.name, "printer driver...")
        pr.instructions()


        if pr.name == "Hollyhock":
            webbrowser.open("https://l.facebook.com/l.php?u=https%3A%2F%2Fprinter.glb.thefacebook.com%2Fprinters%2FMPK22-03-Hollyhock.zip&h=AT0B422MUACi9LVGPoB-MgQaJ8_pZmqfKj6rCkxMli4WugrnlMTmW0gKy4Ex51L1GlFP8zL7zAm5cJaeOytGk0aei2oTvtDBA6_xuyIkJjDO3_UteM_ajnO1NW5lZaQNGonJsmNZ3yM5tAJSZRDnf0CkMDo")


        elif pr.name == "Animalia":
            webbrowser.open("https://l.facebook.com/l.php?u=https%3A%2F%2Fprinter.glb.thefacebook.com%2Fprinters%2FMPK22-03-Animalia.zip&h=AT0xdqPrS2YQH8HlhHwB9S-9NmD__e8usAaA0fYNlaj9b9-ghDc-4YWtcOU1tlIB2_tcWstTcrWSawEqb1bK2LRWiUomJFgckoMWutPpDgVHH2_oVUrcdhsT87gm-C9LrLBeUiVgC4zc_7CL6erXcqOq_1s")


        elif pr.name == "Go_Dog_Go":
            webbrowser.open("https://l.facebook.com/l.php?u=https%3A%2F%2Fprinter.thefacebook.com%2Fprinters%2FMPK22-03-Go_Dog_Go.zip%3Fv2.1&h=AT0IDPKR1jJ7AobH9vuJAFcUAw8dvCi83VK88uyjbxo9ap4A5-fNKGy40xspCPHlfBk9uON-LL53Gz-bVgYzq9PhosnRUaiwyxuYLV3BpcL6pNvGXN36VSX8lxSpY7XGWXfNUwEWTEbogWDGbZlZGoKfkrI")


        elif pr.name == "If_You_Give_a_Mouse_a_Cookie":
            webbrowser.open("https://l.facebook.com/l.php?u=https%3A%2F%2Fprinter.glb.thefacebook.com%2Fprinters%2FMPK22-03-If_You_Give_a_Mouse_a_Cookie.zip&h=AT3bsLFaG3O1WZ_Gh3YPbCmHMEdussEX13wA0LdOBHDemu0n21ztr8EJX4VCPsaYml4NmLLTaPlzYay2HQXS54o0-15RKCHXpX8rp_Jtmg_MKDTUqqGlysqrHWSO2B1MYWHNd9QdPG2uv_z8wOhI3D0w-cY")


        elif pr.name == "Miss_Rumphius":
            webbrowser.open("https://l.facebook.com/l.php?u=https%3A%2F%2Fprinter.glb.thefacebook.com%2Fprinters%2FMPK22-03-Miss_Rumphius.zip&h=AT0urkf7aegLCUp66FSkkKNZPDMUc8KGvj3qKSYDuDRDvTjoEXfklk7lvAHcxyr7M9qTrPL-AMMltvp4Qr_Z0gSB30cc8vW622R06AvWuN4weB8vPzHKoqv_hA7TqCaCz7Z5iTUecfPYbTGBcg1fRPrY43U")

        elif pr.name == "Disagree_with_The_Characterization":
            webbrowser.open("https://l.facebook.com/l.php?u=https%3A%2F%2Fprinter.glb.thefacebook.com%2Fprinters%2FMPK22-03-Disagree_with_The_Characterization.zip&h=AT08WySkhijG56JPhGei2Ux4kqthaoVmQbQaFitc-dFl7MLxwcJGwL7Y5ba_qpZfo9MgriNUGx-11AtoadR-3bc4mIUE3TTevd-Hb1Ng_WQbxWSKy7tU1pow0SQUiaq2GrBOm3z0sQKc_sLFNzz8Xb8K5iM")

        elif pr.name == "What_Problem_Are_We_Trying_To_Solve":
            webbrowser.open("https://l.facebook.com/l.php?u=https%3A%2F%2Fprinter.glb.thefacebook.com%2Fprinters%2FMPK22-03-What_Problem_Are_We_Trying_To_Solve.zip&h=AT3U5PJ4f3SKjKsNaod1wwuNOvWmRxYvU8nfgBTfAs_XINNqBPv1xpCt-I2cfDNcRhwPXZbwjkNMXE6R8zeLgtSwIwZVIopZeYYKrTUBhcK42JUWdXylutRxGfs8NE61nvpt0H7d9ALqiuRaPo_ydLHEZUI")


        elif pr.name == "Countess_of_Grantham":
            webbrowser.open("https://l.facebook.com/l.php?u=https%3A%2F%2Fprinter.glb.thefacebook.com%2Fprinters%2FMPK22-03-Countess_of_Grantham.zip&h=AT0gr2h_smiP2H7jvCGppFd8AKLrFVGSFzYLersF94GdVOljbQsnrYstrPzCJS3Fdx5rLqnbKT5ooff3I-JDkIB5NcKS8fAlKGIkUKDjZeasPC3G_Q53fncNcBxoS6J5qhYoQZoq84KVRdSOdM_cg0H-HlY")


    elif floor == 4:
        print("\n\nMPK22 - 4th Floor Printers")
        print("----------------------------")
        print("A) Daisy_Mason")
        print("B) Dr_Clarkson")
        print("C) Lady_Edith")
        print("D) Lavinia_Swire")
        print("E) M_and_A_Team")
        print("F) Molesley")
        print("G) Mr_Carson")
        print("H) Mrs_Hughes")
        print("I) Mrs_Patmore")
        print("J) Sir_Richard_Carlisle")
        name = input("\nPlease select a printer by entering its associated letter: ")
        pr = MPK_22_Printer(building, floor, floor_list[floor][name])
        print("\nYou Chose:")
        print("Building: ", pr.building)
        print("Floor: ", pr.floor)
        print("Name: ", pr.name)
        print("\nDownloading", pr.name, "printer driver...")
        pr.instructions()

        if pr.name == "Daisy_Mason":
            webbrowser.open("https://l.facebook.com/l.php?u=https%3A%2F%2Fprinter.glb.thefacebook.com%2Fprinters%2FMPK22-04-Daisy_Mason.zip&h=AT27Adyo2YDnJTre9H2OzDQzH_XXthYjfwDiz5_gCLZvwxxyj9S3whbVUintT3DFLSMctv2Rzm9QPvT4Ox2KqJVrjU9sVJHSw3T15Kjih2PpP3qmInW73ytYdil9PZmBqOYnKjvbXtltM6Z4AJnRdIv04WE")

        elif pr.name == "Dr_Clarkson":
            webbrowser.open("https://l.facebook.com/l.php?u=https%3A%2F%2Fprinter.glb.thefacebook.com%2Fprinters%2FMPK22-04-Dr_Clarkson.zip%3Fver2.0&h=AT223qIpsazI6BhxI87f6bkqibSNCaxKqwblGvnx17vhoathztOyxLof5YAuq79HJwdu4nYvyy73GLur7lK3aWS1qzCJ_0pyqFbt8VhCE-bBZftxARDf9ArV1aNRhowBf4ay3Q-d2Wl0PVX3owMKQRftW4M")

        elif pr.name == "Lady_Edith":
            webbrowser.open("https://printer.glb.thefacebook.com/printers/MPK22-04-Lady_Edith.zip")

        elif pr.name == "Lavinia_Swire":
            webbrowser.open("https://l.facebook.com/l.php?u=https%3A%2F%2Fprinter.glb.thefacebook.com%2Fprinters%2FMPK22-04-Lavinia_Swire.zip&h=AT25eFpk0GZ0DEP4Xf5DjRh9tdU8d7o1DjIAPnJNOkR3ydjZz5iXKxwNhEVbyq3bjzMrXFaBx-x4Ylux71dIbJZKW01NF012jVdmZrhTVRu8fJa6YERmSGumXonnnFUhbPhidPM9NoCuKUN6bufCRNk6Z5Q")

        elif pr.name == "M_and_A_Team":
            webbrowser.open("https://l.facebook.com/l.php?u=https%3A%2F%2Fprinter.thefacebook.com%2Fprinters%2FMPK22-04-M_and_A_Team.zip&h=AT1qJ4KN34CEBaJJcFA3ULhXdfNqPcNgnK0EY8Bt0oDTLvr03OIIIizhMKqibmj2B0hxmenyrVqu5iR8XZsADuUJTRaYymRWfy1BbmtoMTuoNTsFgMzaq2HmRnJKqDD8d8oL82jI4Uk21t5WUkzT9rNgnVs")


        elif pr.name == "Molesley":
            webbrowser.open("https://l.facebook.com/l.php?u=https%3A%2F%2Fprinter.glb.thefacebook.com%2Fprinters%2FMPK22-04-Molesley.zip&h=AT2tPtH4l9eATLYuvT1sPbG149HEhtV0QEa9bpuXHY2goSXR5oxpvZRBEWRSidv37Dm6vM3X1CfibmkTgrtImyRA5Ir064ekpEtHKsn2FGa22ZmoRiMUCvEL5FanAevjFH-nSfYV99UIaA9LstDJv8erov0")


        elif pr.name == "Mr_Carson":
            webbrowser.open("https://l.facebook.com/l.php?u=https%3A%2F%2Fprinter.glb.thefacebook.com%2Fprinters%2FMPK22-04-Mr_Carson.zip&h=AT3KmOtKpQg1eJmvFoKQt-5p0V0L3IihN2D902084Y2a_a_-C9wHO4ncAT4-6n51alF_D4dAdxWJHGR9OW1amXqOf3aS9Hzm_7XP1trrjZ8nvdvgMGR4x2ZJT_eOFaZcdx5rD4wkafwxQW9mHio2TDNwEU8")


        elif pr.name == "Mrs_Hughes":
            webbrowser.open("https://l.facebook.com/l.php?u=https%3A%2F%2Fprinter.glb.thefacebook.com%2Fprinters%2FMPK22-04-Mrs_Hughes.zip&h=AT2vxbhfbHnRbR9np5G4OhEwmV9FOw1fxzBf3MZk5p2tgaX2h7oLdj6VK1didIpWM7A742I6BHwN5kjIMP3Ld66iFqJQvt8MTiR-qfQTpl_-DqHoVykexMeO6vKZnE8SxtAU6ln1Iqhhl04WwpH-j6CjG9U")


        elif pr.name == "Mrs_Patmore":
            webbrowser.open("https://l.facebook.com/l.php?u=https%3A%2F%2Fprinter.glb.thefacebook.com%2Fprinters%2FMPK22-04-Mrs_Patmore.zip&h=AT0nLe4jx6znYnjoxPz3EeLC5JknAwr-vkPVETsCf2SUIwhGf2YbsOZmm-dxD6of8GDijiNdNfHe7IrNmN16l8WGMKyLcjOxXMPRjTy4DLlboS1WhLs9tq9emKh0znSvdaqEg8Ai9-fwlIKDmo2l0-PrtEI")


        elif pr.name == "Sir_Richard_Carlisle":
            webbrowser.open("https://l.facebook.com/l.php?u=https%3A%2F%2Fprinter.glb.thefacebook.com%2Fprinters%2FMPK22-04-Sir_Richard_Carlisle.zip&h=AT1Ae297xKdgqMTW5LxRIwVgskLW9E5jHOylK4X5_wVLaCnNQPI4D5PbzXRrP3vUtoZf2XHhqeMog7SVZVETkcc55X4YMTfu1_1pVrGBCzKO4mbEfZsK_E0nhutHgyQd9eB45nhkc-egi4xiVDaDyiLYI0c")



####################################### END OF MPK 22 ###########################################################################

#MPK 23
elif building == 23:
    zone = input("\nWhat zone in building 23 (1 or 2)? ")
    zone = int(zone)
    while int(zone) < 1 or int(zone) > 2:
        print("Please enter a valid zone for MPK 23 (1 or 2): ")
        zone = input("\nWhat zone in building 23 (1 or 2)? ")
        zone == int(zone)
    if zone == 1:
        print("\n\nMPK 23 - Zone 1 Printers:")
        print("----------------------------")
        print("A) Atticus_Finch")
        print("B) Be_the_Nerd")
        print("C) Diplomacy")
        print("D) Duke_Nukem")
        print("E) Mall_Madness")
        print("F) Metal_Gear")
        print("G) Michael_Clayton")
        print("H) Oregon_Trail")
        print("D) Othello")
        print("E) Scotland_Yard")
        print("F) SkiFree")
        print("G) The_Precious")
        name = input("\nPlease select a printer by entering its associated letter: ")
        pr = MPK_23_Printer(building, zone, mpk23_zones[zone][name])
        print("\n___You Chose___")
        print("Building: ", pr.building)
        print("Floor: ", pr.zone)
        print("Name: ", pr.name)
        print("\nDownloading", pr.name, "printer driver...")
        pr.instructions()


        if pr.name == "Atticus_Finch":
            webbrowser.open("https://l.facebook.com/l.php?u=https%3A%2F%2Fprinter.glb.thefacebook.com%2Fprinters%2FMPK23-Atticus_Finch.zip&h=AT1uEKfQzZ-WKOhT8tLXNtt4LaO_69FLyIhcwbR4ITvp8BPJVaIw-Nn9EgX7QIu1Cy8IKeJrOdPvrN9wCNSTf4FqOG1Q-DUlmTXRnpkqiEKlojhmT04PQL8nI_ZIIOK5y3E03QM3nKntTjx5t1T4eCuj")

        elif pr.name == "Be_the_Nerd":
            webbrowser.open("https://l.facebook.com/l.php?u=https%3A%2F%2Fprinter.glb.thefacebook.com%2Fprinters%2FMPK23-Be_the_Nerd.zip&h=AT3jZq4SYvqHg0g35Bk8N6zcQZiCsxaiMuY162dmpDjTOv2P2H4Vo7PYah7m7ldJbgli3HaZfXy5_bwFplPtrB3p3NC3t0rn-_BOk8xP3YfO5SxxbBzletWvH2U3KPR_O8rdkA_XJPM")

        elif pr.name == "Diplomacy":
            webbrowser.open("https://l.facebook.com/l.php?u=https%3A%2F%2Fprinter.glb.thefacebook.com%2Fprinters%2FMPK23-Diplomacy.zip&h=AT0Y3zG_6_9PaJ4LpUW8zh8q4vqn6J18fPhrAQyFHuuNxazQexCns-gUXCEplrpDOnVX8v4rF5Kw3TyoJwUz0HkWh2WWQ3m2hivzt0DBMVptA9glT9-1gvNk6ap6l4qg8x1S_cPIg4k")

        elif pr.name == "Duke_Nukem":
            webbrowser.open("https://l.facebook.com/l.php?u=https%3A%2F%2Fprinter.glb.thefacebook.com%2Fprinters%2FMPK23-Duke_Nukem.zip&h=AT3v313qP_vt8wo7EvycoNc1yfz-TAApxzl4tSneISPqPU_d__gAFwnkZu-fZVO4W86pxzgc-yCUvDc6mAvcpoB8uToreSaQBoVTN_5fIZaulmGP24iALqBNjkUpiCvsR7Yer8Jf_r4")

        elif pr.name == "Mall_Madness":
            webbrowser.open("https://l.facebook.com/l.php?u=https%3A%2F%2Fprinter.glb.thefacebook.com%2Fprinters%2FMPK23-Mall_Madness.zip&h=AT0w5pQg8_pEm4ogIpQaOmFLo4k5vw0azaKUp9qJNCxuFdQqlT4PtLFySp_p3VUP8Ik96QpoGLQlT0JPjcTWsTLpBVLgg8-erumd1yRg2fNbHTa8YGkLd6oYUKwBVaghrJKsw0r1wtQ")

        elif pr.name == "Metal_Gear":
            webbrowser.open("https://l.facebook.com/l.php?u=https%3A%2F%2Fprinter.glb.thefacebook.com%2Fprinters%2FMPK23-Metal_Gear.zip&h=AT1QH6A9QLWrJuRGAmByYYKYa307a_psJdfts-hjUxX30chxQMBtLd8SeInjAvllZaHb43d9DLLDX1FzPVrnPQO5j3t5KCjylsKxu1Au7M2XtPPSD9i9F0d_LRtA8U29vXbrOeD2Jd0")

        elif pr.name == "Michael_Clayton":
            webbrowser.open("https://l.facebook.com/l.php?u=https%3A%2F%2Fprinter.glb.thefacebook.com%2Fprinters%2FMPK23-Michael_Clayton.zip&h=AT3qKFYKLEeNx_gznCrBxFLvZ4YtdlJGlN8hwieayr8EiVPw46HgaH1rKywyxMLvSZ5HHmIo4YJAKAwLHZZ4YG8VPIxPjNVKTwZVxsiPJhmRXNc7qon3-OvmMd2e8C5CeYGw9Hs_quE")

        elif pr.name == "Oregon_Trail":
            webbrowser.open("https://l.facebook.com/l.php?u=https%3A%2F%2Fprinter.glb.thefacebook.com%2Fprinters%2FMPK23-Oregon_Trail.zip&h=AT2VI1FGTZtMLJlgvqUCbXC5ilahX2mx1YOerI7ir-05lMuR0b1niuEixL7tHGZvOFlpxukNl3cxcEzoykAFLMIiBDBsPrG3kyEMX0UlLCTZRE-15UwAVGAC778ST4RbrYH33Zu3YmQ")

        elif pr.name == "Othello":
            webbrowser.open("https://l.facebook.com/l.php?u=https%3A%2F%2Fprinter.glb.thefacebook.com%2Fprinters%2FMPK23-Othello.zip&h=AT2Rm0nTGq_JxijXUaT7xtfcSajAUs6z2xDkHIz9XzYM9uVBmW5_aRaOZCXyd-aeQC6E4HEWb5eN0vREjAkYpfpuAr9_mlzAknPhsupF-q52zrKGHHDfoTL6lh6bzhX6hX1AoC7WIJQ")

        elif pr.name == "Scotland_Yard":
            webbrowser.open("https://l.facebook.com/l.php?u=https%3A%2F%2Fprinter.glb.thefacebook.com%2Fprinters%2FMPK23-Scotland_Yard.zip&h=AT09fdJ-2ovuQz-eBzJeTDBGMifdZUNnqj1bHQNvMpwQZWs5DzkuqPriAKC72ppEr4GXCuxB4IQPvaeHdpdZNEIklNvlUzl2xDxBM4f8LkNdL9QKdNB1Th9lpuFPliW5UH6raA-_U8Y")

        elif pr.name == "SkiFree":
            webbrowser.open("https://l.facebook.com/l.php?u=https%3A%2F%2Fprinter.glb.thefacebook.com%2Fprinters%2FMPK23-SkiFree.zip&h=AT1U9sgO7tq6TNXWGkWedrG3Zz5vNkBF38Q20AheCNTtRAbnxDDHBx8ymSFnB3_U1mBz9d4yi_w-beYtHgs__L2IdIT2vIOL_ZUbvzvBDJlLFWKF9SZ4SgaoNUvXw2KxP_SpA8rurL8")

        elif pr.name == "The_Precious":
            webbrowser.open("https://l.facebook.com/l.php?u=https%3A%2F%2Fprinter.glb.thefacebook.com%2Fprinters%2FMPK23-The_Precious.zip&h=AT3WLRCWYzvw-3mruxtZDI-Yu4dhu2Jdaofa4JLWLU1Uz8n1x069AYf8pLjiOThXGbkN8XsqD-fE2TI1Gzyys0It1pLbk78nIpOv5I9tvEntOQC2F27B-EwLoQwmH7LTTPT7-9pIuvU")


    elif zone == 2:
        print("\n\nMPK 23 - Zone 2 Printers:")
        print("----------------------------")
        print("A) Asks")
        print("B) At_the_End_of_the_Day")
        print("C) Cafe300_Dock")
        print("D) Candy_Colored_Clown")
        print("E) Fusilli_Jerry")
        print("F) Galactica")
        print("G) Inside_Out")
        print("H) JPeterman")
        print("D) Pegasus")
        print("E) Sherbet_Lemon")
        print("F) Taking_it_One_Day_at_a_Time")
        print("G) Treacle_Tart")
        print("H) Virginia_Woolf")
        print("I) Wizochoc")
        name = input("\nPlease select a printer by entering its associated letter: ")
        pr = MPK_23_Printer(building, zone, mpk23_zones[zone][name])
        print("\n___You Chose___")
        print("Building: ", pr.building)
        print("Floor: ", pr.zone)
        print("Name: ", pr.name)
        print("\nDownloading", pr.name, "printer driver...")
        pr.instructions()

        if pr.name == "Asks":
            webbrowser.open("https://l.facebook.com/l.php?u=https%3A%2F%2Fprinter.glb.thefacebook.com%2Fprinters%2FMPK23-Asks.zip&h=AT1OU8FQT8XazDHjHvRpWB6xTgXO51rA0mVfN7oi7gkS7pYzkKpX5Ov4Cpp32z5danKzS-0AolZVj5rguw0n0w1pQDm5KvN6ST6oOJEhDK_EViXjUgjlgd0QO10SpZ02hjaRGerix9oGcKiv-E5APaXj")

        elif pr.name == "At_the_End_of_the_Day":
            webbrowser.open("https://l.facebook.com/l.php?u=https%3A%2F%2Fprinter.glb.thefacebook.com%2Fprinters%2FMPK23-At_the_End_of_the_Day.zip&h=AT0XAjzHe3ca83hELE3BAO0Qv_q9iBg8F8qT9YX16j30SdMIaDiMw0NdK9Gg8QsI1XPoUqSNZPpEIIkBMqxPG28OU1sXJVR0Kl2yDMUFtHnpYqOPVi5Af6Bq_VEwkAK1Q3sgYM4hHpU")

        elif pr.name == "Cafe300_Dock":
            webbrowser.open("https://l.facebook.com/l.php?u=https%3A%2F%2Fprinter.glb.thefacebook.com%2Fprinters%2FMPK23-Cafe300_Dock.zip&h=AT067ldc_oLbMLqQgdp1_YLtIvd03WKYj049ZuE78u4VL2OtG7KE_O9Kgr6gHt7bAXog6xn6tsFlA-BC0uWgRU0cFDoq2T5m0yrAo7bRbuayTcafmegMrwAXjtpLsIl9uy0uQiVbhXc")

        elif pr.name == "Candy_Colored_Clown":
            webbrowser.open("https://l.facebook.com/l.php?u=https%3A%2F%2Fprinter.glb.thefacebook.com%2Fprinters%2FMPK23-Candy_Colored_Clown.zip&h=AT2Tu-p7ulVqqXpKNN6QL_zgittLcelX0-tfvBOzBBWSBI_vVWVotSHrGWgeuTkb7Utmdm14VoTIKuAprzzr2FfTiNTYdxbmRMdRTRBsPpqCDj8zsUbiwJAhVlh8wx1egEeOnN3rRv8")

        elif pr.name == "Fusilli_Jerry":
            webbrowser.open("https://l.facebook.com/l.php?u=https%3A%2F%2Fprinter.glb.thefacebook.com%2Fprinters%2FMPK23-Fusilli_Jerry.zip&h=AT0tvOKq_T8u7a8EUPxPVTMJZHOkXwrPWD_ewVKxqo4YCtYNCBat0EA-dshp-JyC96npAxaZeVJQwd6UfeYnP9v_PXX5hz_4GDwhulHCUNj3xqdTpH72N_9hUwX0RYP-901V2IvY_Bg")

        elif pr.name == "Galactica":
            webbrowser.open("https://l.facebook.com/l.php?u=https%3A%2F%2Fprinter.glb.thefacebook.com%2Fprinters%2FMPK23-Galactica.zip&h=AT0qHqD0FR6Yi7n1VP866jG-Bp2IlS8yGf-R6zvYoRMXOGR2azNe17ujzRWeXANF9bX6HjxYHoptBVQ4h_K_BD4j5u7kRFCjEp2qz4C43Tx4fb5TLZrZoWkH6Qu8WtwrvVyY23Ad2BM")

        elif pr.name == "Inside_Out":
            webbrowser.open("https://l.facebook.com/l.php?u=https%3A%2F%2Fprinter.glb.thefacebook.com%2Fprinters%2FMPK23-Inside_Out.zip&h=AT22lJu-29Z7tb5c4vQ-C-M4HERKbO_DKk9ZcJ-y4MB8t6VfDeUjHlR4pbqyaesICGSPo-6w9-lReuhhiLzZ45VxSMdokAZ7B8vVPvXMm6d0Y3px55SAPTmAtLGZwYs7KI0LSTzcxz8")

        elif pr.name == "JPeterman":
            webbrowser.open("https://l.facebook.com/l.php?u=https%3A%2F%2Fprinter.glb.thefacebook.com%2Fprinters%2FMPK23-JPeterman.zip&h=AT35HZWRd1T_ynB5ro4fjR4snDwdztKzqlHwLps05W5aDv4UpZpzV4KstlCVB8etS3WJtqbwLnsQ1wyYjBH8qZtNj5nLSGX9zdavDkp3RbLMe28KrA6rM-i5XxMdP95SPkmE0pSJX6c")

        elif pr.name == "Pegasus":
            webbrowser.open("https://l.facebook.com/l.php?u=https%3A%2F%2Fprinter.glb.thefacebook.com%2Fprinters%2FMPK23-Pegasus.zip&h=AT21KFuP1l5Avo1zoa2msX9lcxUf7Zrt1MrswlB8YnREAIITUb22X2Y0juInr5NIIc214OVW5RWwvdmzawF8DNg4PdPbkfFXTR8F5ac4iAQsup0T3kmFQYdW28sV417HZvbtEvzEoq4")

        elif pr.name == "Sherbert_Lemon":
            webbrowser.open("https://l.facebook.com/l.php?u=https%3A%2F%2Fprinter.glb.thefacebook.com%2Fprinters%2FMPK23-Sherbet_Lemon.zip&h=AT2GP_dgnOWAGoHRDUC_Z8G9xQas96J63seGQj0CpLynmJIfDZFhxwQFkmoSPiALyWdNAjjFH43HOxQwgoFpGjI4SMxAwCZ9GzHRGENqN7hNKfKX5bx6HCGEdIJRqkl92yM34yhkyUk")

        elif pr.name == "Taking_it_One_Day_at_a_Time":
            webbrowser.open("https://l.facebook.com/l.php?u=https%3A%2F%2Fprinter.glb.thefacebook.com%2Fprinters%2FMPK23-Taking_it_One_Day_at_a_Time.zip&h=AT06rZzwF4HyHl1mrE0AikOjWBna2RYR6VoLXWCIbHdXHxYDtC3GrpcvE01vuaO15rWhZ2_pCBJ008AuZLIMoFiSVHgAWITetKnsWOm423u6MYAih0Vc2nxXS4_Zbu7B5uL_mzMct2k")

        elif pr.name == "Treacle_Tart":
            webbrowser.open("https://l.facebook.com/l.php?u=https%3A%2F%2Fprinter.glb.thefacebook.com%2Fprinters%2FMPK23-Treacle_Tart.zip&h=AT37fiqy0kVyeD4AGJiBXdEnQHQKaMZIEVz-iMyeHngl9uNtyDthk6wICh83CdkAKGtRNf6ElDHPI62OnH8dId7cUPYBrYv9-GRDjHjOj_8ikHgpTxVIT9j3PLdMDBiGxxTKN12RL5o")

        elif pr.name == "Virginia_Woolf":
            webbrowser.open("https://l.facebook.com/l.php?u=https%3A%2F%2Fprinter.glb.thefacebook.com%2Fprinters%2FMPK23-Virginia_Woolf.zip&h=AT3550XW5NGwbh3Ham4R3aSztU_uF1LqH69K6z6WUHg-8IJL0XVFGGjktMr7CsBmLVMdYRdLQSVPLdEnWdHrV_gfQiG18-0juQa2cZIbvQ8k_EPNA-Rf0rEqe7vLh4YuJKxrMNMxtMY")

        elif pr.name == "Wizochoc":
            webbrowser.open("https://l.facebook.com/l.php?u=https%3A%2F%2Fprinter.glb.thefacebook.com%2Fprinters%2FMPK23-Wizochoc.zip&h=AT3Z1KDzFPzgcoJXHYpY-E5xzDBNqim0-WseqKva76l_xBP7j5iPSDHPhqUAbg6-wHW6jssmnRZvrc2VnZHcoPK-Qi7agODukEcVWcC0tyJO4-EAdDt-e6_1uiFrhVwdKGcnppyqfLU")





print("\n\nEnd of Code")
