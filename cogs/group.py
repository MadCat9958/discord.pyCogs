import discord
from discord.ext import commands
from discord import app_commands


class GroupExample(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

        class Group(app_commands.Group):
            """Пример группы. Это описание команды кста."""
            @app_commands.command(description="Что-то добавим")
            async def add(self, interaction: discord.Interaction):
                await interaction.response.send_message("Что-то добавлено")
            
            @app_commands.command(description="Что-то убираем")
            async def remove(self, interaction: discord.Interaction):
                await interaction.response.send_message("Что-то убрано")
                
        self.bot.tree.add_command(Group()) # НЕ ЗАБЫВАЕМ ЭТО


async def setup(bot: commands.Bot):
    await bot.add_cog(GroupExample())