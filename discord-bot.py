"""
from discord.ext import commands
TOKEN = 
bot = commands.Bot(command_prefix="!")

@bot.event
async def on_ready():
    print(f'{bot.user} successfully logged in!')

@bot.command()
async def ping(ctx):
    await ctx.send("pong")

async def scanStart()

bot.run(TOKEN)
"""