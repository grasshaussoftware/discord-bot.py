import discord
from discord import app_commands

MY_GUILD = discord.Object(id=935395948727779328)

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

class button_view(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)
        self.value = None
        self.timeout = None
    
    @discord.ui.button(label = "Get OG Status, Now!", style = discord.ButtonStyle.green, custom_id = "role_button")
    async def get_mod(self, interaction: discord.Interaction, button: discord.ui.Button) -> None:
        if interaction.user.get_role(985708739392839720) is None:
            role = interaction.guild.get_role(985708739392839720) or await interaction.guild.fetch_role(985708739392839720)
            await interaction.user.add_roles(role)
            await interaction.response.send_message(f"I have given you {interaction.guild.get_role(985708739392839720)}!", ephemeral = True)
        else:
            await interaction.response.send_message(f"You already have {interaction.guild.get_role(985708739392839720)} or HIGHER!", ephemeral = True)
            self.get_mod.disabled = True
            await interaction.message.edit(view=self)
            

@client.tree.command(guild=MY_GUILD, name = 'get-og-status', description='Get OG status!')
async def launch_button(interaction: discord.Interaction): 
    await interaction.response.send_message(view = button_view())

client.run(...)
