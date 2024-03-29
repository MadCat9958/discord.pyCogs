import discord
from discord.ext import commands

cog_list = [
    "cogs.hello", # Точка заменяет нам '/', поэтому '.py' в конце писать не надо.
    "cogs.echo",
    "cogs.admin.kick", # Можно и так ¯\_(ツ)_/¯.
    "cogs.admin.ban",
    "cogs.context",
    "cogs.group"
]

class MyBot(commands.Bot):
    def __init__(self):
        super().__init__(
            command_prefix="$", 
            intents=discord.Intents.default() # ВНИМАНИЕ: теперь обязательно надо вводить параметр intents.
                                              # Если Вы не знаете, что это такое - введите, как у меня.
        )
    
    async def setup_hook(self): # Подлючение когов.
        for ext in cog_list:
            await self.load_extension(ext)
        
    async def on_ready(self):
        print(f"{bot.user} запущен!")

bot = MyBot()
bot.run("TOKEN")
