"""
This module contains the main functionalities of the bot.
"""

__author__ = "dariuscioban@yahoo.com"

import responses
from token import BOT_TOKEN

import discord


def run_bot():
    intents = discord.Intents.default()
    intents.message_content = True

    client = discord.Client(intents=intents)

    @client.event
    async def on_ready():
        print(f'We have logged in as {client.user}')

    @client.event
    async def on_message(message):
        if message.author == client.user:
            return

        if message.content.startswith('roll'):
            await message.channel.send(
                responses.handle_response(message.content))

    client.run(BOT_TOKEN)
