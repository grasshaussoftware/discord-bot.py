import discord
from neuralintents import GenericAssistant

chatbot = GenericAssistant('intents.json')
chatbot.train_model()
chatbot.save_model()

intents = discord.Intents.default()
intents.message_content = True
intents.members = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.channel.id != 1018756543816155187: #the channel id that you want the bot to focus on
        return
    if message.content.startswith(""): #no prefix
        response = chatbot.request(message.content)
        await message.channel.send(response)

client.run('your secret token')
