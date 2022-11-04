import discord
from discord import app_commands

MY_GUILD = discord.Object(id=0)

class MyBot(discord.Client):
    def __init__(self, *, intents: discord.Intents):
        super().__init__(intents=intents)
        self.tree = app_commands.CommandTree(self)
 
    async def setup_hook(self):
        self.tree.copy_global_to(guild=MY_GUILD)
        await self.tree.sync(guild=MY_GUILD)

intents = discord.Intents.default()
client = MyBot(intents=intents)

@client.event
async def on_ready():
    print(f'Logged in as {client.user} (ID: {client.user.id})')
    print('------')

@client.tree.command(name = "hello", description="greeting")
async def hello(interaction: discord.Interaction):
    await interaction.response.send_message(f"Hello! Welcome {interaction.user}")

@client.tree.command(name = "lets-goooooo", description="the battle cry")
async def letsgo(interaction: discord.Interaction):
    await interaction.response.send_message("Let's goooooo!")

@client.tree.command(name = "to-the-mooon", description="the motto")
async def tothemoon(interaction: discord.Interaction):
    await interaction.response.send_message("To the moooon!")

@client.tree.command(name = "what-is-it", description="what is cannacoin?")
async def button(interaction: discord.Interaction):
    await interaction.response.send_message("Cannacoin is a crowd managed service based cryptocurrency protocol for the cannabis community and was first deployed on March 28, 2014 as a solution to the 'cash only' predicament set on growers, dispensaries, and consumers alike through Federal regulation as well as a response to the Global Financial Crisis of 2008. It is the evolution of distributed computing and the BitTorrent protocol. It was the brainchild of the pseudonymous Subtoshi, the founder of the popular, but now defunct, 'NWGT.org' (Northwest Green Thumb) online medical cannabis forum based in the Pacific Northwest. It is a new form of electronic money called 'cryptocurrency' similar to Litecoin, Dogecoin, and other 'altcoins' and is intended for use within the independent, medical, and recreational cannabis communities as a medium of exchange, a unit of account, and a store of value for cannabis and cannabis related products and services, worldwide.")


client.run("...")
