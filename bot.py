import discord
from discord.ext import commands
import os
from mcstatus import MinecraftServer

bot = commands.Bot(command_prefix='-')


@bot.event
async def on_ready():
    print("online")

@bot.command()
async def ping(ctx):
    await ctx.send("pong")
    
@bot.command()
async def online(ctx):
    server = MinecraftServer.lookup("appleshield.ru")
    status = server.status()
    if status.players.online == 0:
        await ctx.send(f"На сервере нету игроков.")
    elif status.players.online == 1:
        await ctx.send(f"Онлайн на сервере: {status.players.online} игрок")
    elif status.players.online == 2 or status.players.online == 3 or status.players.online == 4:
        await ctx.send(f"Онлайн на сервере: {status.players.online} игрока")
    else:
        await ctx.send(f"Онлайн на сервере: {status.players.online} игроков")
 
@bot.command()
async def onlinelist(ctx):
    server = MinecraftServer.lookup("appleshield.ru")
    query = server.query()
    await ctx.send("Список игроков на сервере: {0}".format(", ".join(query.players.names)))
        

    
token = os.environ.get('BOT_TOKEN')
    
bot.run(str(token))
