import discord
from discord.ext import commands
import os 
import random
import asyncio

bot = commands.Bot(command_prefix='>')

@bot.event
async def on_ready():
    print("Раб готов к работе")
    
@bot.command(pass_context = True)
async def mydick(ctx):
    emded = discord.Emded(title = "Бот измерял твою пипиську. Результат:", description = (random.randint(1,41)), color = 
(0xF85252))
    await ctx.send(emded = emded)



token = os.environ.get('BOT_TOKEN')

bot.run(str(token))
