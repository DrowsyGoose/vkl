import discord
from discord.ext import commands
import os 
import random

bot = commands.Bot(command_prefix='>')

@bot.command()
async def mydick(ctx):
    piska=random.randint(1,41)
    await ctx.send('Бот измерял твой писюн. Результат:',piska,"см")

token = os.environ.get('BOT_TOKEN')

bot.run(str(token))
