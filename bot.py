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
from dolartoday import Dolartoday
import os


url = ('https://s3.amazonaws.com/dolartoday/data.json')


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
    embed.add_field(name="$mesualidad", value="Calcula el monto de la mensualidad en Bs y proporciona los datos para el pago", inline=False)
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


@bot.command()
async def mensualidad(ctx):
    cedula = '25960409'
    telf = '0412-5003420'
    banco = '0105 - Mercantil'
    dolar = Dolartoday(url)
    mensaje = dolar.get_data()
    embed = discord.Embed(title="Precio del dolar", color = discord.Color.green(), timestamp=datetime.datetime.utcnow())
    embed.add_field(name="Mensualidad en bolivares" , value=f"{mensaje}", inline=False)
    embed.add_field(name="Datos para el pago en bs: " , value=f"cedula: **{cedula}** , telefono **{telf}** banco: **{banco}**", inline=False)
    embed.add_field(name="Importante", value="""Una vez realizado el pago en Bolívares debes enviar el comprobante de Pago al canal de #Pagos bajo el siguiente formato:
    1) Nombre y Apellido:
    2) Número de Cedula:
    3) Número o ID de Transacción:
    4) Mes Correspondiente del Pago:
    5) Captura del Pago (donde se refleje el número o ID de transacción):
    Gracias y que le saques provecho a este próximo mes!""")
    embed.set_footer(text="Fuente: F8Network")
    await ctx.send(embed=embed)


load_dotenv()
bot.run(os.getenv('DISCORD_TOKEN'))