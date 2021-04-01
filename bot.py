import discord
from discord.ext import commands
import os
import random
from discord.ext.commands import has_permissions, MissingPermissions
from mcrcon import MCRcon


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
    
mcr = MCRcon("25575", "Hhdef3536")


@bot.command()
@bot.has_permisions(administrator=True)
async def wl(ctx, nick):
    mcr = MCRcon("25575", "Hhdef3536") as mrc:
        comm = mcr.command(f"/easywhitelist add {nick}")
        print(comm)
                                    
    
        

    
token = os.environ.get('BOT_TOKEN')
    
bot.run(str(token))
