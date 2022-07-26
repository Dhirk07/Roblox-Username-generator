import requests, colorama, random, threading, time
from colorama import init, Fore, Back, Style
from discord_webhook import DiscordWebhook, DiscordEmbed




## CONFIG

sendtowebhook = True ## (False, True) 

yourwebhook = "https://discord.com/api/webhooks/1111"

min = 5

max = 6

timetowait = 3 ## if you are getting ratelimited raise this number if not lower it

threads = 1 ## i would reccomend u keep this at 1 IF u are using the send to webhook feature, if not u can turn this up, this will speed up the process of finding usernames but probs ratelimit you.

## END OF CONFIG

if min < 3:
    print(f'{Fore.RED}Usernames have to be 3 to 20 characters long.')
    quit()

if max > 20:
    print(f'{Fore.RED}Usernames have to be 3 to 20 characters long.')
    quit()


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

            if r.status_code == 429:
                print(f'{Fore.RED}Ratelimited - Increae The timetowait Variable Value')
                time.sleep(5)



            elif a.find('Id') == -1:
                print('='*38)
                print(f'{Fore.GREEN}{name} Is Not Taken!')
                print('='*38)
                open("UserNames.txt", "a").write(name + '\n')
                if sendtowebhook:
                    embed = DiscordEmbed(title='New Username Sniped!', color=0x00e3fd)
                    embed.add_embed_field(name='Username', value=f'{name}')
                    embed.add_embed_field(name='Register Here!', value=f'[Here!](https://www.roblox.com/signup)')
                    setwebhook.add_embed(embed)
                    response = setwebhook.execute(remove_embeds=True)
            
          
for noni in range(threads):
    try:

        t = threading.Thread(target=main)
        t.start()
        time.sleep(timetowait)
    except Exception as e:
        print(e)
