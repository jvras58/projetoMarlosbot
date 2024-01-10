import time
from config.conector_discord import ConectorDiscord
from config.config import get_settings
from funcoes.comandos_basicos import load_basic_commands
from funcoes.comandos_mencoes import MentionsCommands
from funcoes.comandos_dm import DmCommands
from funcoes.comandos_config_canal import CanalCommands

cliente_discord = ConectorDiscord()
tree = cliente_discord.tree


load_basic_commands(tree)


MentionsCommands = MentionsCommands(cliente_discord)
MentionsCommands.load_mentions_commands(tree)


dm_commands = DmCommands(cliente_discord)
dm_commands.load_dm_commands(tree)



canal_commands = CanalCommands(cliente_discord)
canal_commands.load_channel_commands(tree)

while True:
    try:
        # Inicialização do cliente do Discord
        cliente_discord.run(get_settings().DISCORD_TOKEN)
    except Exception as e:
        print(f'Erro: {e}. Reiniciando o bot.')
        time.sleep(5)  # Pausa por 5s
