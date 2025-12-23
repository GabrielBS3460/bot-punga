import pickledb as database

from utilities.configreader import ConfigReader

config = ConfigReader.get_config()

# Itens que ocorrem ao iniciar o bot.

class InitBot():
    def __init__(self, bot=None) -> None:
        self.bot = bot
    
    async def start(self):
        pass
