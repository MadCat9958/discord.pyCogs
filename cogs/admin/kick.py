import discord
from discord import app_commands
from discord.ext import commands


class Kick(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
    
    @app_commands.command(name='kick', description="Кикнуть участника")
    @app_commands.describe(member="Участник, которого надо кикнуть", reason="Причина")
    async def kick(self, interaction: discord.Interaction, member: discord.Member, reason: str = None):
        if interaction.user.guild_permissions.kick_members:
            try:
                await member.kick(reason=reason)
            except:
                await interaction.response.send_message("Не удалось кикнуть участника!", ephemeral=True)
            else:
                await interaction.response.send_message(f"{member.mention} кикнут!")
        else:
            await interaction.response.send_message("У тебя нет прав!", ephemeral=True)
    

async def setup(bot: commands.Bot):
    await bot.add_cog(Kick(bot))
