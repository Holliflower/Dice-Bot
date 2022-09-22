import os

import discord
from dotenv import load_dotenv

from helper.dice_function import dice_roll

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

client = discord.Client(intents=discord.Intents.default())


@client.event
async def on_ready():
    guild = discord.utils.get(client.guilds, name=GUILD)
    print(
        f'{client.user} is connected to the following server: \n'
        f'{guild.name} (id: {guild.id})'
    )


@client.event
async def on_message(message):
    if message.author == client.user:  #
        return

    if message.content.startswith("!roll"):
        if message.author == client.user:  # Checks user typing message is not bot
            return

        words = message.content.split(" ")  # Extract XDY from input and assign values to x and y
        x, y = words[1].split('d')

        result = dice_roll(int(x), int(y))  # Convert input to integers and roll dice
        await message.channel.send(result)

client.run(TOKEN)

