from datetime import datetime

import discord
from config.config import get_settings
from discord import app_commands


class MentionsCommands:
    def __init__(self, cliente):
        self.cliente_discord = cliente

    @app_commands.describe(horario='Horário do alerta: %H:%M')
    async def definir_alerta(
        self, interaction: discord.Interaction, horario: str
    ):
        authorization_ids = [
            int(id) for id in get_settings().AUTHORIZATION_IDS.split(',')
        ]

        if interaction.user.id not in authorization_ids:
            await interaction.response.send_message(
                'Você não está autorizado a usar este comando.', ephemeral=True
            )
            return

        horario = datetime.strptime(horario, '%H:%M').time()

        # Converta a hora e os minutos para uma string no formato 'HH:MM'
        horario_str = horario.strftime('%H:%M')

        # Salve a hora e os minutos como uma string
        self.cliente_discord.alerta_checkpoint_horario = horario_str
        self.cliente_discord.save()
        await interaction.response.send_message(
            f'Alerta definido para {self.cliente_discord.alerta_checkpoint_horario}.',
            ephemeral=True,
        )

    async def offeveryone(self, interaction: discord.Interaction):
        authorization_ids = [
            int(id) for id in get_settings().AUTHORIZATION_IDS.split(',')
        ]

        if interaction.user.id not in authorization_ids:
            await interaction.response.send_message(
                'Você não está autorizado a usar este comando.', ephemeral=True
            )
            return

        # Responda à interação primeiro
        await interaction.response.send_message(
            'Desativando menções a todos...', ephemeral=True
        )
        self.cliente_discord.enviar_everyone = False
        self.cliente_discord.save()

    async def oneveryone(self, interaction: discord.Interaction):
        authorization_ids = [
            int(id) for id in get_settings().AUTHORIZATION_IDS.split(',')
        ]

        if interaction.user.id not in authorization_ids:
            await interaction.response.send_message(
                'Você não está autorizado a usar este comando.', ephemeral=True
            )
            return

        # Responda à interação primeiro
        await interaction.response.send_message(
            'Ativando menções a todos...', ephemeral=True
        )
        self.cliente_discord.enviar_everyone = True
        self.cliente_discord.save()

    def load_mentions_commands(self, tree):
        tree.command(
            name='horario_alerta', description='Define o horário do alerta'
        )(self.definir_alerta)
        tree.command(
            name='offeveryone', description='Desativa menções a todos'
        )(self.offeveryone)
        tree.command(name='oneveryone', description='Ativa menções a todos')(
            self.oneveryone
        )