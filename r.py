import discord
from discord.ext.commands import Bot
import os

bot = Bot(command_prefix='%')
token = str(input('Token: '))
clear = lambda: os.system('cls')

@bot.event
async def on_ready():
    print('Ready')

@bot.event
async def on_message(message):
    if message.content.startswith('+status'):
        embed = discord.Embed(color=0x7FFF00, title="GODZILLA IS ONLINE")
        await bot.send_message(message.channel, embed=embed)


bot.run(token)
