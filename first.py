import discord
from discord.ext import commands
import re
import os 
import random
import asyncio



bot = commands.Bot(command_prefix='>')

@bot.event
async def on_ready():
    print("Раб готов к работе")
    
@bot.command(pass_context = True)
async def mydick(ctx):
    embed = discord.Embed(title = "Бот измерял твою пипиську. Ваш результат:", description = (random.randint(1,45)), color = (0x6eb3ac))
    await ctx.send(embed = embed)

@bot.command(pass_context = True)
async def report(ctx, user : discord.Member, *reason):

    channel = bot.get_channel(739057829599641630) 

    author = ctx.message.author

    rearray = ' '.join(reason[:]) 

    if not rearray: 
        
        goose = discord.Embed(title = f"{author} жалуется на  {user}, по причине: Без причины", color = (0x6eb3ac))

        await channel.send(embed = goose)

        await ctx.message.delete() 

    else:
        
        goose1 = discord.Embed(title = f"{author} жалуется на  {user}, по причине: {rearray}", color = (0x6eb3ac))

        await channel.send(embed = goose1)

        await ctx.message.delete()

@bot.command()
async def Модерн(ctx):
    await ctx.send("Вы приняты в 1 район. Для подробностей напишите в лс Pelmeshka_Otoidi#1258")

@bot.command()
async def Средневековье(ctx):
    gorod=random.randint(1, 6)
    if gorod == 2:
        await ctx.send("Вы приняты во 2 район. Для подробностей напишите в лс Pelmeshka_Otoidi#1258")
    else:
        await ctx.send("Вы приняты в {} район. Для подробностей напишите в лс Pelmeshka_Otoidi#1258".format(gorod))

@bot.command()

async def play(ctx,game):

    if game == "1":

        await ctx.send("Окей, давай начнем нашу игру")

        await ctx.send("Угадай число от 1 до 12")

        await ctx.send("Используй >go чтобы начать")

@bot.command()

        
async def go(ctx, num: int = None):
        
    cislo = 12

    number = random.randint(1, 12)

    if num != number:

        await ctx.send("Не верно, попробуй еще раз")





    if num == number:

        await ctx.send("Ты угадал, молодец.")
            
    if num > cislo:
            
        await ctx.send("Ты далбаеб, по русски написано, от 1 до 12")

    await ctx.send("А бот загадал число:")
    await ctx.send(number)



@bot.command()

async def send(ctx,*, otpr):
    channel = bot.get_channel(739056945474043986)
    await channel.send(otpr)
@bot.command()
async def me(ctx,*, sosok):
    uss=ctx.message.author
    await ctx.send(uss, sosok)
    await ctx.message.delete()
    

















        
#


token = os.environ.get('BOT_TOKEN')

bot.run(str(token))
