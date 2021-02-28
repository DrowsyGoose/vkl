import discord
from discord.ext import commands
import os
#d
bot = commands.Bot(command_prefix='-')


@bot.event()
async def on_ready():
    prine("online")

@bot.command()
async def ping(ctx):
    await ctx.send("pong")
    
token = os.environ.get('BOT_TOKEN')
    
bot.run(str(token))
