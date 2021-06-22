#By Dhirk07
#check my repo here (https://github.com/Dhirk07/Roblox-Username-generator)
import requests
import random
import colorama
from colorama import Fore
from discord_webhook import DiscordWebhook, DiscordEmbed

webhook = DiscordWebhook(url="https://discord.com/api/webhooks/abc")#replace your webhook

def namegen():
    length = random.randint(5, 5) #set your min and max (min, max)
    letters = "a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R",
    "S","T","U","V","W","X","Y","Z","1","2","3","4","5","6","7","8","9","0","_"

    return ''.join(random.choice(letters) for i in range(length))

duh = ('[Click Me](https://discord.gg/VK9dg6qFWw)')
SignUp = ('[Here!](https://www.roblox.com/signup)')

choice = input(f'{Fore.RED}[S] Start\n[E] Exit\n\n'f'{Fore.RED}Choice: ')

if choice == 'S':
    while True:
        name = namegen()
        r = requests.get("https://api.roblox.com/users/get-by-username?username=" + name)
        a = r.text
        if a.find('Id') == -1:
            print(f'{Fore.GREEN}' + name + ' is not taken! SignUp ' + name + ' now!')
            print('='*38)
            open("UserNames.txt", "a").write(name + '\n')





            embed = DiscordEmbed(title='New Username Sniped!', color=0x00e3fd)#stuff
            embed.add_embed_field(name='Username:', value=f'{name}')#stuff
            embed.add_embed_field(name='Join for more Cool Stuff', value=f'{duh}')#stuff
            embed.add_embed_field(name='Register Here!', value=f'{SignUp}')#stuff
            webhook.add_embed(embed)
            response = webhook.execute(remove_embeds=True)
