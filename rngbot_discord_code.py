#a very simple RNG (random number generator) bot for Discord. Programmed in Python 3.7. Open source.
#this code was developed by godofbooks (https://github.com/godofbooks) as a personal project.
#feel free to use and modify the code as you'd like. credit is appreciated.

#import packages
import os
import random
import discord
from dotenv import load_dotenv

#gets info from rng.env
load_dotenv("rng.env")
Token=os.getenv("DISCORD_TOKEN")
Guild=os.getenv("DISCORD_GUILD")

#establishes client
client = discord.Client()

#log in message 
@client.event
async def on_ready():
    print("Logged in as {0.user}".format(client))

    for guild in client.guilds:
        if guild.name == Guild:
            break
    print(
        f'{client.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})'
    )

#sets bot prefix
bot_prefix = "-"

#when user types, bot responds
@client.event
async def on_message(message):
    if message.author == client.user:
        return

    #sets nickname variable
    nickname=message.author.display_name

    #lists RNG variables
    #RNG.final_num

    #-rng x,y
    def RNG():
        if message.content.startswith("{0}rng".format(bot_prefix)):
            text=message.content
            strip_text=text.strip("{0}rng ".format(bot_prefix))
            Boundaries=strip_text.split(",")
            num1=int(Boundaries[0])
            num2=int(Boundaries[1])
            RNG.final_num=random.randint(num1,num2)

    #-rng error handling
    if message.content.startswith("{0}rng".format(bot_prefix)):
        try:
            RNG()
            await message.channel.send("{0}'s number is: {1}".format(nickname,RNG.final_num))
            print("{0}'s number is: {1}".format(nickname,RNG.final_num))
        except Exception as error:
            await message.channel.send("Sorry, there was an error. Make sure you're typing the numbers right! If you need help, type {0}help".format(bot_prefix))
            print("{0} caused an error: {1}".format(nickname,error))

    #-help
    if message.content.startswith("{0}help".format(bot_prefix)):
        await message.channel.send("**List of current commands:**\n"
            "\n"
            "*{0}info*\n"
            "Lists the prefix, bot developer, and coding information.\n"
            "\n"
            "*{0}help*\n"
            "Displays the commands list.\n"
            "\n"
            "*{0}rng x,y*\n"
            "Picks a number between the 2 chosen numbers.\n"
            "Correct useage: {0}rng 1,4     {0}rng 4,14\n"
            "Incorrect useage: {0}rng 1,3,4    {0}rng 1-5"
            .format(bot_prefix))
        print(nickname,"requested the commands list.")

    #-info
    if message.content.startswith("{0}info".format(bot_prefix)):
        await message.channel.send("**Bot Info**\n"
            "\n"
            "*Prefix*\n"
            "{0}\n"
            "\n"
            "*Bot Developer*\n"
            "godofbooks (https://github.com/godofbooks)\n"
            "\n"
            "*Programming and useage*\n"
            "Programmed in Python 3.7. Open source. Code available at https://github.com/godofbooks/rng-discord \n"
            "\n"
            .format(bot_prefix))
        print(nickname,"requested the info list")


#runs the bot
client.run(Token)
