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

@bot.event

async def on_message(message):

    if message.content.startswith(">spin"): 

        channel = message.channel

        await channel.send("Quess the number from 0-10 by writing number in this channel!") 

        number1 = random.randint(1,10) 

        print(number1)

        

        number2 = str(number1) 

        def check(m):

            return m.content == number2 and m.channel == channel 

        

        msg = await client.wait_for('message', check=check)

        await channel.send("Correct answer {.author}" .format(msg)) 
#


token = os.environ.get('BOT_TOKEN')

bot.run(str(token))
