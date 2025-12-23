import discord
from discord.ext import commands

BOT_NAME = 'Bot de Punga'

# Lista de Cogs (app/punga.py, por exemplo)
EXTENTION_LIST = [
    'punga'
]

# ⚠️ Use apenas o que você realmente precisa
intents = discord.Intents.default()
intents.message_content = True  # ative no Discord Developers também

class Client(commands.Bot):
    async def setup_hook(self):
        for ext in EXTENTION_LIST:
            await self.load_extension(f"app.{ext}")
            print(f"Extensão carregada: app.{ext}")

CLIENT = Client(
    command_prefix=">>!",
    intents=intents
)

