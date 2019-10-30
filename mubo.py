import subprocess 

def Home():
    print("* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *  ")
    print("*" + "                                       MUBO                                          *")
    print("*" + "                                                                                     *")
    print("*" + "       1. VsCode                                                                     *")
    print("*" + "       2. League Of Legends                                                          *")
    print("*" + "       3. Chrome                                                                     *")
    print("*" + "       4. My Youtube Playlist                                                        *")
    print("*" + "       5. Xampp                                                                      *")
    print("*" + "       6. Word                                                                       *")
    print("*" + "       7. Discord                                                                    *")
    print("*" + "                                                                                     *")
    print("*" + "                                                                                     *")
    print("*" + "                                                                                     *")
    print("*" + "                             Made by: mmb it developer                               *")
    print("* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *  ")    

# The first input of the program. And what you want to do.
i = 2
Home()

def openprogram():
    WhatProgram = input("\n--> Start: ")  

    # All of the programs
    # VsCode
    if (WhatProgram == "1"):
        subprocess.Popen(["D:/Microsoft VS Code/Code.exe"])

    # League Of Legends
    elif (WhatProgram == "2"):
        subprocess.Popen(["D:/League Of Legends/LeagueClient"])

    # Chrome
    elif (WhatProgram == "3"):
        subprocess.Popen(["C:/Program Files (x86)/Google/Chrome/Application/Chrome"])

    # Playlist
    elif (WhatProgram == "4"):
        subprocess.Popen(["C:/xampp/htdocs/mubo/MyPlaylist.bat"])

    # Xampp
    elif (WhatProgram == "5"):
        subprocess.Popen(["C:/xampp/xampp-control"])

    # Word
    elif (WhatProgram == "6"):
        subprocess.Popen(["C:/Program Files (x86)/Microsoft Office/root/Office16/WINWORD.exe"])

    # Discord
    elif (WhatProgram == "7"):
        subprocess.Popen(["C:/Users/Mustafa Bolat/AppData/Local/Discord/app-0.0.305/Discord.exe"])

while i > 1:
    openprogram()