from distutils import command
from email import message
from sys import prefix
from unicodedata import name
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
bot = commands.Bot(command_prefix='$')	

@bot.event
async def on_ready():
    print('Bot is ready')
    await bot.change_presence(activity=discord.Game(name='calcular tasas :)'))


@bot.command()
async def comandos(ctx):
    embed = discord.Embed(title="Comandos", description="Comandos disponibles", color = discord.Color.blue())
    embed.add_field(name="$enviar", value="Calcula el monto a enviar con comision", inline=False)
    embed.add_field(name="$total", value="Calcula el monto en bs a recibir", inline=False)
    await ctx.send(embed=embed)
#evento envio de precio con la tasa
  
@bot.command()
async def enviar(ctx, monto):
    amount = float(monto)
    total = calculo(amount)
    embed = discord.Embed(title="Calculo venta Paypal", description=f"El monto a enviar con comision es de: {total}", color=discord.Colour.blue(), timestamp=datetime.datetime.utcnow())
    embed.add_field(name="fuente:" , value="**F8Network**")
    await ctx.send(embed=embed)



@bot.command()
async def total(ctx, num1: float , num2: float):
    total = calculo_venta(num1, num2)
    embed = discord.Embed(title="Calculo venta Paypal", description=f"El monto a recibir es de: **{total}** bs", color=discord.Colour.blue(), timestamp=datetime.datetime.utcnow())
    embed.add_field(name="Tasa comprador:" , value=f"**{num1}**")
    embed.add_field(name="Paypal neto enviado:" , value=f"**{num2}**")
    embed.add_field(name="fuente:" , value="**F8Network**")
    await ctx.send(embed=embed)

load_dotenv()
bot.run(os.getenv('DISCORD_TOKEN'))