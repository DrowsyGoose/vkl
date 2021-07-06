import discord
from discord.ext import commands
import os
import random
import discord_components 



bot = Bot(command_prefix = "!")





@bot.event

async def on_ready():

    DiscordComponents(bot)

    print(f"Logged in as {bot.user}!")





@bot.command()

async def button(ctx):

    await ctx.send(

        "Hello, World!",

        components = [

            Button(label = "WOW button!")

        ]

    )



    interaction = await bot.wait_for("button_click", check = lambda i: i.component.label.startswith("WOW"))

    await interaction.respond(content = "Button clicked!")





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
