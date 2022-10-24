#discord.py bot to return a random number between 1 and 10, answer a "yes or no" question, and roll a six sided die

import discord
import random

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)
yes_no = ["yes", "no"]
dice = ["[ . ]", "[ : ]", "[ .: ]", "[ :: ]", "[ :.: ]", "[ ::: ]"]

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.channel.id != 1018756543816155187:
        return
    if 'random' in message.content.lower():
        await message.channel.send(random.randint(1, 10))
    if 'yes or no' in message.content.lower():
        await message.channel.send(random.choice(yes_no))
    if 'roll' in message.content.lower():
        await message.channel.send(random.choice(dice))

client.run('<your secret token>')
