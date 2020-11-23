import discord
from discord.ext import commands
import os 
import random
import asyncio

bot = commands.Bot(command_prefix='>')

@bot.event
async def on_ready():
    print("Раб готов к работе")
    
@bot.command(pass_context = True)
async def mydick(ctx):
    embed = discord.Embed(title = "Бот измерял твою пипиську. Результат:", description = (random.randint(1,41)), color = 
(0xF85252))
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
@commands.command()
commands.has_permissions(add_reactions=True,embed_links=True)
async def help(self,ctx,*cog):
    """Gets all cogs and commands of mine."""
    try:
        if not cog:
            halp=discord.Embed(title='Cog Listing and Uncatergorized Commands',
                               description='Use `!help *cog*` to find out more about them!\n(BTW, the Cog Name Must Be in Title Case, Just Like this Sentence.)')
            cogs_desc = ''
            for x in self.bot.cogs:
                cogs_desc += ('{} - {}'.format(x,self.bot.cogs[x].__doc__)+'\n')
            halp.add_field(name='Cogs',value=cogs_desc[0:len(cogs_desc)-1],inline=False)
            cmds_desc = ''
            for y in self.bot.walk_commands():
                if not y.cog_name and not y.hidden:
                    cmds_desc += ('{} - {}'.format(y.name,y.help)+'\n')
            halp.add_field(name='Uncatergorized Commands',value=cmds_desc[0:len(cmds_desc)-1],inline=False)
            await ctx.message.add_reaction(emoji='✉')
            await ctx.message.author.send('',embed=halp)
        else:
            if len(cog) > 1:
                halp = discord.Embed(title='Error!',description='That is way too many cogs!',color=discord.Color.red())
                await ctx.message.author.send('',embed=halp)
            else:
                found = False
                for x in self.bot.cogs:
                    for y in cog:
                        if x == y:
                            halp=discord.Embed(title=cog[0]+' Command Listing',description=self.bot.cogs[cog[0]].__doc__)
                            for c in self.bot.get_cog(y).get_commands():
                                if not c.hidden:
                                    halp.add_field(name=c.name,value=c.help,inline=False)
                            found = True
                if not found:
                    halp = discord.Embed(title='Error!',description='How do you even use "'+cog[0]+'"?',color=discord.Color.red())
                else:
                    await ctx.message.add_reaction(emoji='✉')
                await ctx.message.author.send('',embed=halp)
    except:
        pas

#520571349811462147
token = os.environ.get('BOT_TOKEN')

bot.run(str(token))
