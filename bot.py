import discord
from discord.ext import commands
import os
import random
from discord.ext.commands import Bot
from discord_components import DiscordComponents, Button, Select, SelectOption



bot = Bot(command_prefix = "!")





@bot.event

async def on_ready():

    DiscordComponents(bot)

    print(f"Logged in as {bot.user}!")





@bot.command()

async def button(ctx):

    await ctx.send(

        " ",

        components = [

            Button(label = "Нажми на меня")

        ]

    )



    interaction = await bot.wait_for("button_click")

    await interaction.respond(content = "Поздравляю, ваша мать была выебана!")






@bot.command()

async def select(ctx):

    await ctx.send(

        "Выбери:",

        components = [

            Select(placeholder="От этого зависит твоя жизнь!", options=[SelectOption(label="Я гомосексуал", value="A"), SelectOption(label="Я бисексуал", value="B")])

        ]

    )



    interaction = await bot.wait_for("select_option", check = lambda i: i.component[0].value == "A")

    await interaction.respond(content = "Мне похуй")
    
    interaction = await bot.wait_for("select_option", check = lambda i: i.component[0].value == "B")

    await interaction.respond(content = "Мне похуй")


    
token = os.environ.get('BOT_TOKEN')
    
bot.run(str(token))
