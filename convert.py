import convertapi
import colorama
import time
import os
import webbrowser
import random

from colorama import Fore, Style, Back

os.system("title PyConvert File Converter ^| In Menu...")
convertapi.api_secret = '6VlQ5uxj413f2mJV'

blue = Fore.BLUE
red = Fore.RED
green = Fore.GREEN
cyan = Fore.CYAN
purp = Fore.MAGENTA
white = Fore.WHITE
reset = Style.RESET_ALL

rn = random.randint(1, 9999)
githubURL = 'https://github.com/WooxHimself'

def goodbye():
    os.system('cls')
    time.sleep(0.3)
    print("""

                                     ▄▄ •             ·▄▄▄▄  ▄▄▄▄·  ▄· ▄▌▄▄▄ .
                                    ▐█ ▀ ▪ ▄█▀▄  ▄█▀▄ ██· ██ ▐█ ▀█▪▐█▪██▌▀▄.▀·
                                    ▄█ ▀█▄▐█▌.▐▌▐█▌.▐▌▐█▪ ▐█▌▐█▀▀█▄▐█▌▐█▪▐▀▀▪▄
                                    ▐█▄▪▐█▐█▌.▐▌▐█▌.▐▌██. ██ ██▄▪▐█ ▐█▀·.▐█▄▄▌
                                    ·▀▀▀▀  ▀█▄▀▪ ▀█▄▀▪▀▀▀▀▀• ·▀▀▀▀   ▀ •  ▀▀▀ 
                                    
    
    """)
    exit()


print("Loading...")
time.sleep(0.1)
os.system('cls')

print(Fore.CYAN + f"""

                                         {purp}╔══════════════════════════════════════════╗
                                         {purp}║     {cyan}╔═══╗     ╔═══╗                ╔╗    {purp}║
                                         {purp}║     {cyan}║╔═╗║     ║╔═╗║               ╔╝╚╗   {purp}║
                                         {purp}║     {cyan}║╚═╝║╔╗ ╔╗║║ ╚╝╔══╗╔╗╔╗╔══╗╔═╗╚╗╔╝   {purp}║
                                         {purp}║     {cyan}║╔══╝║║ ║║║║ ╔╗║╔╗║║╚╝║║╔╗║║╔╝ ║║    {purp}║
                                         {purp}║     {cyan}║║   ║╚═╝║║╚═╝║║╚╝║╚╗╔╝║║═╣║║  ║╚╗   {purp}║
                                         {purp}║     {cyan}╚╝   ╚═╗╔╝╚═══╝╚══╝ ╚╝ ╚══╝╚╝  ╚═╝   {purp}║
                                         {purp}║     {cyan}     ╔═╝║                            {purp}║
                                         {purp}║     {cyan}     ╚══╝                            {purp}║
                                         {purp}╚══════════════════════════════════════════╝
                                        {red}Convert image files to another format in pure Python
                                           GitHub: github.com/WooxHimself/PyConvert


                                                  {white}[{red}1{white}] {purp}Convert Files
                                                  {white}[{red}2{white}] {purp}Visit my GitHub
                                                  {white}[{red}3{white}] {red}EXIT
                                                  {reset}
""")

choice = input(f"{cyan}♥ {purp}>>> ")

def convert():
    os.system("title PyConvert File Converter ^| Converting...")


    file = input(f"{cyan}Drop your file here or paste the file location {purp}>>> ")
    if "\\" not in file:
        print(f"{red} Invalid File Location {reset}")
        convert()
    else:
        print(f"""
        
                                           Choose what do you want to do:
                                              {white}[{red}1{white}] {purp}Convert to .png
                                              {white}[{red}2{white}] {purp}Convert to .ico
                                              {white}[{red}3{white}] {purp}Convert to .jpg
                                              {white}[{red}4{white}] {purp}Convert to .jpeg
                                              {white}[{red}5{white}] {red}ABORT
                                              {reset}
        """)
        image = input(f"{cyan}Choice {purp}>>> ")
        if image == '1':
            print(f"{green}Converting...")
            result = convertapi.convert('png', { 'File': file })
            print(f"{green}Finishing up...")
            result.file.save(f'PyConvert_{rn}.png')
            print(f"{purp} Success! File converted successfuly and has been saved to the location along with this script.")

        if image == '2':
            print(f"{green}Converting...")
            result = convertapi.convert('ico', { 'File': file })
            print(f"{green}Finishing up...")
            result.file.save(f'PyConvert_{rn}.ico')
            print(f"{purp} Success! File converted successfuly and has been saved to the location along with this script.")

        if image == '3':
            print(f"{green}Converting...")
            result = convertapi.convert('jpg', { 'File': file })
            print(f"{green}Finishing up...")
            result.file.save(f'PyConvert_{rn}.jpg')
            print(f"{purp} Success! File converted successfuly and has been saved to the location along with this script.")

        if image == '4':
            print(f"{green}Converting...")
            result = convertapi.convert('jpeg', { 'File': file })
            print(f"{green}Finishing up...")
            result.file.save(f'PyConvert_{rn}.jpeg')
            print(f"{purp} Success! File converted successfuly and has been saved to the location along with this script.")

        if image == '5':
            goodbye()



    

if choice == '1':
    convert()

elif choice == '2':
    webbrowser.open(githubURL, new=2)

elif choice == '3':
    goodbye()