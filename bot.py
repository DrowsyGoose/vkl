import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='-')

@bot.command()
async def test(ctx):
    await ctx.send("work")
    
token = os.environ.get("BOT_TOKEN")
    
bot.run(token)
