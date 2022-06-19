import discord
from discord import app_commands
from discord.ext import commands


class SayHello(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
    
    @app_commands.command(name='hello', description="Скажи привет") # Создаём слеш-команду
    async def hello(self, interaction: discord.Interaction):
        await interaction.response.send_message(f"Привет, {interaction.user.mention}!")


async def setup(bot: commands.Bot): # Подключение кога.
    await bot.add_cog(SayHello(bot))