import sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from client import CLIENT, BOT_NAME

from utilities.configreader import ConfigReader
ConfigReader.set_mode(dev_mode=False)

from project._init import InitBot
init_bot = InitBot(CLIENT)

@CLIENT.event
async def on_ready():
    mensagemInicial = f"SUCESSFUL: {BOT_NAME} is Online!"
    print(mensagemInicial)
    await init_bot.start()
    print("=" * 50)

CLIENT.run(ConfigReader.get_token())
