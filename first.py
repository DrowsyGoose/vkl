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
    embed = discord.Embed(title = "Бот измерял твою пипиську. Результат:", description = (random.randint(1,41)), color = 
(0xF85252))
    await ctx.send(embed = embed)

@bot.command(pass_context = True)
async def report(ctx, user : discord.Member, *reason):

    channel = bot.get_channel(739057829599641630) 

    author = ctx.message.author

    rearray = ' '.join(reason[:]) 

    if not rearray: 

        await channel.send(f"{author} жалуется на  {user}, по причине: Без причины")

        await ctx.message.delete() 

    else:

        await channel.send(f"{author} жалуется на {user}, по причине: {rearray}")

        await ctx.message.delete()


#520571349811462147
token = os.environ.get('BOT_TOKEN')

bot.run(str(token))
