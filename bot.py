from distutils import command
import discord
from discord import embeds
from discord.colour import Color
from discord.ext import commands
from discord.utils import async_all
import datetime
from paypal import *
from dotenv import load_dotenv
import os


load_dotenv()
env_path = os.path.join(os.path.dirname(__file__), '.env')
load_dotenv(dotenv_path=env_path)
dst = os.getenv('DISCORD_TOKEN')

bot = discord.Client()

@bot.event
async def on_ready():
    print('Bot is ready')

@bot.event
async def on_message(message):
    prefix='$'

    if message.content.startswith(prefix):
        command = message.content.strip(prefix)
        monto = calculo(command)
        total = str(monto)
        embed = discord.Embed(title="Calculo venta Paypal", description=f"El monto a enviar con comision es de: {total}", color=discord.Colour.blue())
        await message.channel.send(embed=embed)

load_dotenv()
bot.run(os.getenv('DISCORD_TOKEN'))