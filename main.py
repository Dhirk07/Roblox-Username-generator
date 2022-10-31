import requests, colorama, random, threading
from colorama import init, Fore, Back, Style
from discord_webhook import DiscordWebhook, DiscordEmbed




## CONFIG

sendtowebhook = True ## (False, True) 

yourwebhook = "https://discord.com/api/webhooks/1111"

min = 5 

max = 6

threads = 1 ## i would reccomend u keep this at 1 IF u are using the send to webhook feature, if not u can turn this up, this will speed up the process of finding usernames.

## END OF CONFIG




init()

def namegen():
    length = random.randint(min, max)
    eval = "a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R",
    "S","T","U","V","W","X","Y","Z","1","2","3","4","5","6","7","8","9","0","_"

    return ''.join(random.choice(eval) for i in range(length))

if sendtowebhook:
    setwebhook = DiscordWebhook(url=yourwebhook)

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
                    embed = DiscordEmbed(title='New Username Sniped!', color=0x00e3fd)#stuff
                    embed.add_embed_field(name='Username', value=f'{name}')#stuff
                    embed.add_embed_field(name='Register Here!', value=f'[Here!](https://www.roblox.com/signup)')
                    setwebhook.add_embed(embed)
                    response = setwebhook.execute(remove_embeds=True)
             
          
for noni in range(threads):
    try:

        t = threading.Thread(target=main)
        t.start()

    except Exception as e:
        print(e)
