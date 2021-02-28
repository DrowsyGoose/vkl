import discord
from discord.ext import commands
import os

bot = commands.Bot(command_prefix='-')

@bot.command()
async def ping(ctx):
    await ctx.send("pong")
    
token = os.environ.get('BOT_TOKEN')
    
bot.run(token)
