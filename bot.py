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

        components = [

            Button(label = "Спойлер!")

        ]

    )



    interaction = await bot.wait_for("button_click", check = lambda i: i.component.label.startswith("WOW"))

    await interaction.respond(content = "Я твою мать ебал)")





@bot.command()

async def select(ctx):

    await ctx.send(

        "Hello, World!",

        components = [

            Select(placeholder="select something!", options=[SelectOption(label="a", value="A"), SelectOption(label="b", value="B")])

        ]

    )



    interaction = await bot.wait_for("select_option", check = lambda i: i.component[0].value == "A")

    await interaction.respond(content = f"{interaction.component[0].label} selected!")


    
token = os.environ.get('BOT_TOKEN')
    
bot.run(str(token))
