#discord.py bot to return a random number between 1-10 in the channel

import discord
import random

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)



@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if 'random' in message.content:
        await message.send(random.randint(1, 10))

client.run('<private token>')
