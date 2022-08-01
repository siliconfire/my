# bot.py
import os
from colorama import Fore, Back, Style

print("Hold on, importing important modules...")

os.system("cls")
print("------------------------------------------------------")
print("Welcome!")
print("")
print(Fore.GREEN + "(!) Press [ENTER] to start the bot.")
print(Style.RESET_ALL)
print("github.com/trashbin7")
print("------------------------------------------------------")
input()
os.system("cls")
print("------------------------------------------------------")
print("Loading bot...")
print()
print(Fore.GREEN + "---" + Fore.RED + "-----------------")
print(Style.RESET_ALL)
print("importing...")
print("------------------------------------------------------")
import discord
from dotenv import load_dotenv
import time
os.system("cls")
print("------------------------------------------------------")
print("Loading bot...")
print()
print(Fore.GREEN + "-----------" + Fore.RED + "---------")
print(Style.RESET_ALL)
print("Processing token...")
print("------------------------------------------------------")
load_dotenv()
TOKEN = ('MTAwMjkwNzE0NTkzNjgzNDU5MA.GkY3F4.Rdzlhgyi6SYgyQScrU9Ylo7_fZqFAR4-z3dYAg')
GUILD = ('DISCORD_GUILD')

client = discord.Client()

os.system("cls")
print("------------------------------------------------------")
print("Loading bot...")
print()
print(Fore.GREEN + "---------------" + Fore.RED + "-----")
print(Style.RESET_ALL)
print("Getting guild name...")
print("------------------------------------------------------")
@client.event
async def on_ready():
    for guild in client.guilds:
        if guild.name == GUILD:
            break
    os.system("cls")
    print("------------------------------------------------------")
    print("Loading bot...")
    print()
    print(Fore.GREEN + "--------------------")
    print(Style.RESET_ALL)
    print("All Done!")
    print("------------------------------------------------------")
    time.sleep(0.3)
    os.system("cls")
    print("------------------------------------------------------")
    print(Fore.YELLOW + str(client.user) + Style.RESET_ALL + " Aşağıdaki sunucuya bağlı:")
    print(Fore.YELLOW + str(guild.name))
    print(Style.RESET_ALL + "(id: " + Fore.YELLOW + str(guild.id) + Style.RESET_ALL + ")")
    print()
    print("github.com/trashbin7/DcGamesTR")
    print("------------------------------------------------------")

@client.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f"Merhaba {member.name}, Discord sunucumuza hoş geldin!")

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!hello'):
        await message.channel.send('Hello!')

    if message.content.startswith('!ping'):
        await message.channel.send('Pong!')
client.run(TOKEN)