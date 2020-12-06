import discord
from discord.ext import commands
import re
import os 
import random
import asyncio
import json



bot = commands.Bot(command_prefix='>')
client = discord.Client()

@bot.event
async def on_ready():
    print("Раб готов к работе")
    
@bot.command(pass_context = True)
async def mydick(ctx):
    embed = discord.Embed(title = "Бот измерял твою пипиську. Ваш результат:", description = (random.randint(1,69)), color = (0x6eb3ac))
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
async def me(ctx,*,s):
    autho = ctx.message.author
    await ctx.send(f"{autho} {s}")
    await ctx.message.delete()

    
@bot.command()
async def rp(ctx,com,*ss):
    autho = ctx.message.author.name
    ran = random.choice(["Удачно","Неудачно"])
    s = ' '.join(ss[:]) 
    if com == "me":
        await ctx.send(f"**{autho}** {s}")
        await ctx.message.delete()
    elif com == "try":
        await ctx.send(f"**{autho}** {s} **({ran})**")
        await ctx.message.delete()
        
try:
    with open("users.json") as fp:
        users = json.load(fp)
except Exception:
    users = {}

def save_users():
    with open("users.json", "w+") as fp:
        json.dump(users, fp, sort_keys=True, indent=4)

def add_points(user: discord.User, points: int):
    id = user.id
    if id not in users:
        users[id] = {}
    users[id]["points"] = users[id].get("points", 0) + points
    print("{} now has {} points".format(user.name, users[id]["points"]))
    save_users()

def get_points(user: discord.User):
    id = user.id
    if id in users:
        return users[id].get("points", 0)
    return 0

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    print("{} sent a message".format(message.author.name))
    if message.content.lower().startswith("!points"):
        msg = "You have {} points!".format(get_points(message.author))
        await client.send_message(message.channel, msg)
    add_points(message.author, 1)
    #ddd
               












        
#


token = os.environ.get('BOT_TOKEN')

bot.run(str(token))
