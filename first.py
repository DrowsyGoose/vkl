import discord
from discord.ext import commands
import re
import os 
import random
import asyncio
import json
import requests
#1



bot = commands.Bot(command_prefix='>')

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
        
        
@bot.event
async def on_member_join(member):
    with open('users.json', 'r') as f:
        users = json.load(f)

    users[str(member.id)] = '0'

    with open('users.json', 'w') as f:
        json.dump(users, f)


@bot.event
async def on_message(message):
    if message.author.bot == False:
        with open('users.json', 'r') as f:
            users = json.load(f)
        

        await update_data(users, message.author)
        await add_experience(users, message.author, 5)
        await level_up(users, message.author, message)

        with open('users.json', 'w') as f:
            json.dump(users, f)

    await bot.process_commands(message)


async def update_data(users, user):
    if not f'{user.id}' in users:
        users[f'{user.id}'] = {}
        users[f'{user.id}']['опыт'] = 0
        users[f'{user.id}']['уровень'] = 1


async def add_experience(users, user, exp):
    users[f'{user.id}']['опыт'] += exp


async def level_up(user, users, message):
    with open('levels.json', 'r') as g:
        levels = json.load(g)
    with open('levels.json', 'w') as g:
        json.dump(levels, g)
    experience = users[user['id']]['опыт']
    lvl_start = users[user['id']]['уровень']
    print(user)
    lvl_end = int(experience ** (1 / 4))
    if lvl_start < lvl_end:
        await message.channel.send(f'{user.mention} поднял уровень до {lvl_end}')
        users[f'{user.id}']['уровень'] = lvl_end
        

@bot.command()
async def level(ctx, member: discord.Member = None):
    if not member:
        id = ctx.message.author.id
        with open('users.json', 'r') as f:
            users = json.load(f)
        exp = users[str(id)]['опыт']
        lvl = users[str(id)]['уровень']
        await ctx.send(f'У тебя {lvl} уровень! И {exp} опыта')
    else:
        id = member.id
        with open('users.json', 'r') as f:
            users = json.load(f)
        exp = users[str(id)]['опыт']
        lvl = users[str(id)]['уровень']
        await ctx.send(f'{member} имеет {lvl} уровень! И {exp} опыта')
print(users)







        
#


token = os.environ.get('BOT_TOKEN')

bot.run(str(token))
