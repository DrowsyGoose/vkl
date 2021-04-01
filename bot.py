import discord
from discord.ext import commands
import os
import random
import factorio_rcon




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
    client = factorio_rcon.RCONClient("188.127.241.11", 25575, "Hhdef3536")
    client.connect
    response = client.send_command(f"/easywl add {nick}")
    await ctx.send(f"Игрок под ником {nick} был добавлен в вайтлист")

                                    
    
        

    
token = os.environ.get('BOT_TOKEN')
    
bot.run(str(token))
