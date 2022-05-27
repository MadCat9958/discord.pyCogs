from cgitb import reset
import discord
from discord import app_commands
from discord.ext import commands

class Echo(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
    
    @app_commands.command(name="echo", description='Вывести текст от имени бота')
    @app_commands.describe(text="Текст, который бот должен написать.")
    async def echo(self, interaction: discord.Interaction, text: str):
        await interaction.response.send_message(f"{interaction.user}: {text}.")


async def setup(bot: commands.Bot):
    await bot.add_cog(Echo(bot))