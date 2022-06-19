import discord
from discord.ext import commands
from discord import app_commands


class Context(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

        self.ctx_command = app_commands.ContextMenu(
            name="Контекстное меню",
            callback=self.ctx
        )
        self.bot.tree.add_command(self.ctx_command)

        async def ctx(self, interaction: discord.Interaction, member: discord.Member):
            await interaction.response.send_message(f"Ты выбрал(-а) {member.mention}", ephemeral=True)


async def setup(bot: commands.Bot):
    await bot.add_cog(Context(bot))