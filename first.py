import discord
from discord.ext import commands
import re
import os 
import random
import asyncio
import json
import requests
from mcstatus import MinecraftServer
from discord.utils import get
import datetime
from MojangAPI import Client
import nest_asyncio

nest_asyncio.apply()






bot = commands.Bot(command_prefix='>')

@bot.command(name='bot')
async def _bot(ctx):
    em = discord.Embed(color=discord.Color.green())
    em.title = 'Bot Info'
    em.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)
    try:
        em.description = bot.psa + '\n[Support Server](Скоро)'
    except AttributeError:
        em.description = 'Это информация о CreeperGamer. Девелоперы: DrowsyGoose аля RUProstocky'
    em.add_field(name="Серверов", value=len(bot.guilds))
    em.add_field(name="Онлайн юзеров", value=str(len({m.id for m in bot.get_all_members() if m.status is not discord.Status.offline})))
    em.add_field(name='Всего юзеров', value=len(bot.users))
    em.add_field(name='Каналов', value=f"{sum(1 for g in bot.guilds for _ in g.channels)}")
    em.add_field(name="Библиотека", value=f"discord.py, discord.js")
    em.add_field(name="Пригласить", value=f"[Click Here](https://discordapp.com/oauth2/authorize?client_id={bot.user.id}&scope=bot&permissions=268905542)")
    em.add_field(name='Гитхаб', value='[2 часть](https://github.com/DrowsyGoose/vkl)')

    em.set_footer(text="CreeperGamerBot | Powered by discord.py")
    await ctx.send(embed=em)

@bot.command()
async def server(ctx):
    serv = MinecraftServer.lookup("mc.reworlds.ru")
    status = serv.status()
    embed = discord.Embed(title = "MC.REWORLDS.RU", description = "Онлайн сервере {0}. Отклик {1} ms".format(status.players.online, status.latency), color = (0x6eb3ac))
    await ctx.send(embed=embed)
    
@bot.event
async def on_ready():
    print("Раб готов к работе")
    
@bot.command(pass_context = True)
async def mydick(ctx):
    idd = ctx.message.author.id
    rand = random.randint(1,40)
    embed = discord.Embed(title = "Бот измерял твою пипиську. Ваш результат:", description = rand, color = (0x6eb3ac))
    await ctx.send(embed = embed)
    with open('gam.json', 'w+') as f:
        json.dump(rand, f)

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

    await ctx.send(otpr)
    

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
    unverified = discord.utils.get(member.guild.roles, name="unverified") 
    await member.add_roles(unverified) 
    

def is_channel(ctx):
    return ctx.channel.id == 796338274016821258


@bot.command()
@commands.check(is_channel) 
async def verify(ctx):
    unverified = discord.utils.get(ctx.guild.roles, name="unverified") 
    if unverified in ctx.author.roles: 
        verify = discord.utils.get(ctx.guild.roles, name="Гость") 
        msg = await ctx.send('Верификация ')
        await msg.add_reaction('✅')
        e = discord.Embed(color=0x7289da)
        e.add_field(name='Пожалуйста выполните верификацию.',
                    value='** ПОДСКАЗКА: ** Вам ** нужно написать ответ с фото в этот чат **')
        e.set_image(url='https://media.discordapp.net/attachments/739056945474043986/791714231677747231/fa78b7e045e46132.jpg')
        await ctx.author.send(embed=e)

        def check(m):
            return m.content == '4'

        msg = await bot.wait_for('message', check=check)
        e = discord.Embed(color=0x7289da)
        await ctx.author.remove_roles(unverified)
        e.add_field(name='Спасибо за верификацию!', value='Теперь сервер открыт для тебя.')
        await ctx.author.send(embed=e)
        await ctx.author.add_roles(verify) 
    else:
        await ctx.send('Ты верифицированный!')
        
role = "unverified" 

@bot.event
async def on_member_join(member): 
    rank = discord.utils.get(member.guild.roles, name=role) 
    await member.add_roles(rank)
    print(f"{member} получил {rank} ")
@bot.command()    
async def py(ctx,*, args):
    




    await ctx.send(f"https://discordpy.readthedocs.io/en/latest/api.html#{args}")

    
@bot.command(pass_context=True)
async def ping(ctx):
    now = datetime.datetime.utcnow()
    delta = ctx.message.created_at
    pingtime = now - delta
    embed = discord.Embed(title = """
░▒█▀▀▄░▒█▀▀▄░▒█▀▀▀░▒█▀▀▀░▒█▀▀█░▒█▀▀▀░▒█▀▀▄
░▒█░░░░▒█▄▄▀░▒█▀▀▀░▒█▀▀▀░▒█▄▄█░▒█▀▀▀░▒█▄▄▀
░▒█▄▄▀░▒█░▒█░▒█▄▄▄░▒█▄▄▄░▒█░░░░▒█▄▄▄░▒█░▒█
""", description="Pong! {} ms".format(pingtime), color=(0x176cd5))
    embed.set_author(name="Requested by " + str(ctx.message.author), icon_url=ctx.message.author.avatar_url)
    await ctx.send(embed=embed)
    
    
@bot.command()
async def skin(ctx, name):

    user = await Client.User.createUser(name)

    profile = await user.getProfile()

    await ctx.send(profile.skin)
token = os.environ.get('BOT_TOKEN')

bot.run(str(token))
