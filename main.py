import requests, colorama, random, threading
from colorama import init, Fore, Back, Style
from dhooks import Webhook, Embed




## CONFIG

sendtowebhook = True ## (False, True) 

yourwebhook = "https://discord.com/api/webhooks/1042731218904547328/JetfeYUKdBARUQMsrvlSI_M-sGhxvNl2i9JSO0eDL_arZGY965HKY18qDTBWyS43YknJ"

min = 5 

max = 6

threads = 2 ## i would reccomend u keep this at 1 IF u are using the send to webhook feature, if not u can turn this up, this will speed up the process of finding usernames.

## END OF CONFIG




init()

def namegen():
    length = random.randint(min, max)
    eval = "a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R",
    "S","T","U","V","W","X","Y","Z","1","2","3","4","5","6","7","8","9","0","_"

    return ''.join(random.choice(eval) for i in range(length))

if sendtowebhook:
    setwebhook = Webhook(url=yourwebhook)

def main():
    while True:
            name = namegen()
            r = requests.get("https://api.roblox.com/users/get-by-username?username=" + name)
            a = r.text
            ## credits to @thatonehen https://github.com/thatonehen
            if not a.find('{"success":false,"errorMessage":"User not found"}') == -1:
                print(f'{Fore.GREEN}{name} Is Not Taken!')
                print('='*38)
                open("UserNames.txt", "a").write(name + '\n')
                if sendtowebhook:
                    embed = Embed(title='New Username Sniped!', color=0x00e3fd)#stuff
                    embed.add_field(name='Username', value=f'{name}')#stuff
                    embed.add_field(name='Register Here!', value=f'[Here!](https://www.roblox.com/signup)')
                    embed.add_field(name='Discord', value=f'[Join!](https://discord.gg/H5bcd7fTYb)')
                    setwebhook.execute(embed=embed)
             
          
for noni in range(threads):
    try:
        t = threading.Thread(target=main)
        t.start()
    except Exception as e:
        print(e)
