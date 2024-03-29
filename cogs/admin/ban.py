import discord
from discord import app_commands
from discord.ext import commands


class Ban(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
    
    @app_commands.command(name='ban', description="Забанить участника")
    @app_commands.describe(member="Участник, которого надо забанить", reason="Причина")
    async def ban(self, interaction: discord.Interaction, member: discord.Member, reason: str = None):
        if interaction.user.guild_permissions.ban_members:
            try:
                await member.ban(reason=reason)
            except:
                await interaction.response.send_message("Не удалось забанить участника!", ephemeral=True)
            else:
                await interaction.response.send_message(f"{member.mention} забанен!")
        else:
            await interaction.response.send_message("У тебя нет прав!", ephemeral=True)
    

async def setup(bot: commands.Bot):
    await bot.add_cog(Ban(bot))
