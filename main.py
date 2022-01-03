import os
import discord
from bot_config import *
from discord.ext import commands, tasks

client = commands.Bot(command_prefix = prefix)

@client.event
async def on_ready():
    print("I'm Alive!")

@client.command()
async def cog(ctx,identify=None,name=None):
    if ctx.message.author.id == allowed_peoples:

        #This will create a new cog so your code doesn't get messed up
        if identify == 'new':
            if name == None:
                await ctx.send('Put a name for your cog')
            else:
                if os.path.isfile(f'./cogs/{name}.py'):
                    await ctx.message.channel.send('There is already a cog with this name')
                else:
                    create = open(f'./cogs/{name}.py', 'x')
                    create.close()
                    with open(f'./cogs/{name}.py', 'a') as archive:
                            archive.write('import discord\nfrom discord.ext import commands\n\nclass misc(commands.Cog):\n\n    def __init__(self, client):\n        self.client = client\n\n    \n\ndef setup(client):\n    client.add_cog(misc(client))')
                    client.load_extension(f'cogs.{name}')
                    await ctx.reply(f'{name}.py successfully created!')

        #This will cause your existing cog to be deleted.
        if identify == 'delete':
            if name == None:
                await ctx.send('Put a name for delete your cog')
            else:
                try:
                    os.remove(f'./cogs/{name}.py')
                    await ctx.send(f'{name}.py has been deleted!')
                except:
                    await ctx.send('There is no cog with this name')

        #This will cause your cog to be reloaded, but be careful not to break its code, if that happens it will not be reloaded
        if identify == 'reload':
            if name == None:
                await ctx.send('Put a name for reload your cog')
            else:
                try:
                    client.unload_extension(f'cogs.{name}')
                    client.load_extension(f'cogs.{name}')
                    await ctx.send('Successfully reloaded!')
                except:
                    await ctx.send(f'{name}.py is unable to reload, check if the name is typed correctly, or if his code is broken')

        #This will make your cog be loaded, if you got the one from the internet
        if identify == 'load':
            if name == None:
                await ctx.send('Put a name for load your cog')
            else:
                try:
                    client.load_extension(f'cogs.{name}')
                    await ctx.send(f'{name}.py successfully loaded!')
                except:
                    await ctx.send('Could not load your cog, check if the correct name is typed')

        #This will cause your cog to be unloaded if you want to make it unusable for a while
        if identify == 'unload':
            if name == None:
                await ctx.send('Put a name for unload your cog')
            else:
                try:
                    client.unload_extension(f'cogs.{name}')
                    await ctx.send(f'{name}.py successfully unloaded!')
                except:
                    await ctx.send('Could not unload your cog, check if the correct name is typed')

        #A little help for using this command
        if identify == None:
            await ctx.send('`new: This command followed by "-cog " creates a new cog with a template`\n`delete: This command followed by "-cog " delete an existing cog`\n`reload: This command followed by "-cog " reload your cog, use when you update the code of him`\n`load: This command followed by "-cog " load an existing cog`\n`unload: This command followed by "-cog " unload an existing cog`')

    else:
        await ctx.send('Do you not have permission to run this command')

#This will make all your cogs load automatically
for filename in os.listdir('./cogs'): #cogs will be used to make the code more clean
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')

#This will make the bot run(make sure you put your bot's token into bot_config)
client.run(betoken)