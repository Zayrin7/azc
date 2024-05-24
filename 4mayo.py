import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'Hemos iniciado sesión como {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hola, soy un bot {bot.user}!')

@bot.command()
async def heh(ctx,count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def bye(ctx):
    await ctx.send("\U0001f642")

@bot.command()
async def emoji(ctx):
    emodji = ["U+2764 U+FE0F", "U+2615	", "U+1F339", "U+1F31E", "U+1F319"]
    return random.choice(emodji)

@bot.command()
async def repeat(ctx, times: int, content='repeating...'):
    for i in range(times):
        await ctx.send(content)
