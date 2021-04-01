import discord
from discord.ext import commands
import os
import random
from rcon import Client


bot = commands.Bot(command_prefix='-')


@bot.event
async def on_ready():
    print("online")

@bot.command()
async def ping(ctx):
    await ctx.send("pong")
    
@bot.command()
async def who(ctx):
    pros = random.randint(0, 100)
    ari = random.choice(["Автосексуал", "Андрогинсексуал", "Андросексуал", "Асексуал", "Бисексуал", "Гетеросексуал", "Гиносексуал", "Гомосексуал", "Грейсексуал", "Демисексуал", "Литосексуал", "Объектумсексуал", "Омнисексуал", "Пансексуал", "Полисексуал", "ПоМосексуал", "Сапиосексуал", "Сколиосексуал", "Цифросексуал"])
    embed=discord.Embed(title="**Геемер**", description= f"Вы {ari} на {pros}%", color=0xff0000)
    await ctx.send(embed=embed)
    #d
    

@bot.command()
@commands.has_permissions(administrator=True)
async def wl(ctx, nick):
    with Client('188.127.241.11', 25575, passwd='Hhdef3536') as client:
    response = client.run(rcon.console.rconcmd(f"easywhilelist add {nick}"))
    print(response)
                                    
    
        

    
token = os.environ.get('BOT_TOKEN')
    
bot.run(str(token))
