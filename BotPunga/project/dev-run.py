import sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Carrega todas as funções dentro de app.
from client import CLIENT, EXTENTION_LIST, BOT_NAME
for EXTENTION in EXTENTION_LIST:
    CLIENT.load_extension("app." + EXTENTION)

# Define se estamos em produção ou desenvolvimento.
from utilities.configreader import ConfigReader
ConfigReader.set_mode(dev_mode=True)

# Instancia a classe para executar funções ao iniciar o bot.
from project._init import InitBot
init_bot = InitBot(CLIENT)
    
@CLIENT.event
async def on_ready():
    mensagemInicial = f"SUCESSFUL: {BOT_NAME} DevBot is Online!"
    await init_bot.start()
    print(f'\033[32m{mensagemInicial:^15}')
    print('\033[33m=\033[m' * 50)

# Excecuta o bot.
CLIENT.run(ConfigReader.get_token())
