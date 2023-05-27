import os

def cls():
 os.system("cls")


import ctypes
import requests
import colorama
import random
import string
import time

colorama.init()


os.system("title GANG-NITRO ::: Made By Vynix")


print(colorama.Fore.LIGHTGREEN_EX + """

           $$$$$$\   $$$$$$\  $$\   $$\  $$$$$$\          $$\   $$\ $$$$$$\ $$$$$$$$\ $$$$$$$\   $$$$$$\  
          $$  __$$\ $$  __$$\ $$$\  $$ |$$  __$$\         $$$\  $$ |\_$$  _|\__$$  __|$$  __$$\ $$  __$$\ 
          $$ /  \__|$$ /  $$ |$$$$\ $$ |$$ /  \__|        $$$$\ $$ |  $$ |     $$ |   $$ |  $$ |$$ /  $$ |
          $$ |$$$$\ $$$$$$$$ |$$ $$\$$ |$$ |$$$$\ $$$$$$\ $$ $$\$$ |  $$ |     $$ |   $$$$$$$  |$$ |  $$ |
          $$ |\_$$ |$$  __$$ |$$ \$$$$ |$$ |\_$$ |\______|$$ \$$$$ |  $$ |     $$ |   $$  __$$< $$ |  $$ |
          $$ |  $$ |$$ |  $$ |$$ |\$$$ |$$ |  $$ |        $$ |\$$$ |  $$ |     $$ |   $$ |  $$ |$$ |  $$ |
          \$$$$$$  |$$ |  $$ |$$ | \$$ |\$$$$$$  |        $$ | \$$ |$$$$$$\    $$ |   $$ |  $$ | $$$$$$  |
           \______/ \__|  \__|\__|  \__| \______/         \__|  \__|\______|   \__|   \__|  \__| \______/ 
  
                                           ---: Made By Vynix :---                                                                                                                                        
""")

colorama.init()

num = int(input(colorama.Fore.LIGHTWHITE_EX + 'How Many Codes to Generate Nitro : '))

with open("Nitro Codes.txt", "w", encoding='utf-8') as file:
    print("Your nitro codes are being generated, be patient if you entered the high number!")

    start = time.time()

    for i in range(num):
        code = "".join(random.choices(
            string.ascii_uppercase + string.digits + string.ascii_lowercase,
            k = 16
        ))

        file.write(f"https://discord.gift/{code}\n")

    print(f"Generated {num} codes | Time taken: {time.time() - start}\n")

with open("Nitro Codes.txt") as file:
    for line in file.readlines():
        nitro = line.strip("\n")

        url = "https://discordapp.com/api/v6/entitlements/gift-codes/" + nitro + "?with_application=false&with_subscription_plan=true"

        r = requests.get(url)

        if r.status_code == 200:
            print(f" Valid | {nitro} ",colorama.Fore.LIGHTWHITE_EX + "")
            break
        else:
            print(f" Invalid |  {nitro} ",colorama.Fore.LIGHTWHITE_EX + "")

time.sleep(0.2)

input("\nYou have generated, Now press enter to close this, you'll get valid codes in Valid Codes.txt if you see its empty then you didn't get any hits!")