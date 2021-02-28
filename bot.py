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
async def online(ctx, pl):
    server = MinecraftServer.lookup("appleshield.ru")
    status = server.status()
    if pl != list:
        await ctx.send(f"онлайн на сервере: {status.players.online} игроков")
    elif pl == list:
        query = server.query()
        await ctx.send("Список игроков на сервере: {0}".format(", ".join(query.players.names)))

    
token = os.environ.get('BOT_TOKEN')
    
bot.run(str(token))
