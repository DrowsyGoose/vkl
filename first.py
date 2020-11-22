import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='>')

@bot.command()
async def ping(ctx):
    await ctx.send('pong')

token = os.environ.get('BOT_TOKEN')

bot.run(str(token))
