#By Dhirk07
#check my repo here (https://github.com/Dhirk07/Roblox-Username-generator)
import requests, colorama, random
from colorama import Fore
from discord_webhook import DiscordWebhook, DiscordEmbed

webhook = DiscordWebhook(url="https://github.com/Dhirk07/Roblox-Username-generator")#replace your webhook
val = ('[Click Me](https://discord.gg/VK9dg6qFWw)')

def namegen():
    length = random.randint(5, 5) #set your min and max (min, max)
    eval = "a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R",
    "S","T","U","V","W","X","Y","Z","1","2","3","4","5","6","7","8","9","0","_"

    return ''.join(random.choice(eval) for i in range(length))

SignUp = ('[Here!](https://www.roblox.com/signup)')

print(f'{Fore.GREEN}', "If you have issues contact me at Discord | 𝕯𝓱𝓲𝓻𝓴07#0001")
while True:
        name = namegen()
        r = requests.get("https://api.roblox.com/users/get-by-username?username=" + name)
        a = r.text
        if a.find('Id') == -1:
            print(f'{Fore.GREEN}' + name + ' is not taken! SignUp ' + name + ' now!')
            print('='*38)
            open("UserNames.txt", "a").write(name + '\n')





            embed = DiscordEmbed(title='New Username Sniped!', color=0x00e3fd)#stuff
            embed.add_embed_field(name='Username', value=f'{name}')#stuff
            embed.add_embed_field(name='Cool Stuff', value=f'{val}')#stuff
            embed.add_embed_field(name='Register Here!', value=f'{SignUp}')#stuff
            webhook.add_embed(embed)
            response = webhook.execute(remove_embeds=True)
