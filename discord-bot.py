
from discord.ext import commands
TOKEN = "MTAwMjIwMjc0OTg3OTk5NjUwOA.G0Vrfa.bruyJZiqVmlXXmqwDB2ZpnL8Uzv2dc-ayBtiWY"
bot = commands.Bot(command_prefix="!")

@bot.event
async def on_ready():
    print(f'{bot.user} successfully logged in!')

@bot.command()
async def ping(ctx):
    await ctx.send("pong")

bot.run(TOKEN)