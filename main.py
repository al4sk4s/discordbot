import os
import discord
from btoken import *
from discord.ext import commands, tasks

client = commands.Bot(command_prefix = prefix)

@client.event
async def on_ready():
    print("I'm Alive!")

#cog loader
@client.command()
async def load(ctx, extension):
    if ctx.message.author.id == allowed_peoples:
        try:
            client.load_extension(f'cogs.{extension}')
        except:
            client.load_extension(f'cogs.musicas.{extension}')
        await ctx.message.channel.send(f'{extension} got loaded!')
    else:
        await ctx.send('do you not have permission to run this command')

#cog unloader
@client.command()
async def unload(ctx, extension):
    if ctx.message.author.id == allowed_peoples:
        try:
            client.unload_extension(f'cogs.{extension}')
        except:
            client.unload_extension(f'cogs.musicas.{extension}')
        await ctx.message.channel.send(f'{extension} got unloaded!')
    else:
        await ctx.send('do you not have permission to run this command')

#cog reloader
@client.command()
async def reload(ctx, extension):
    if ctx.message.author.id == allowed_peoples:
        try:
            try:
                client.unload_extension(f'cogs.{extension}')
                client.load_extension(f'cogs.{extension}')
            except:
                client.unload_extension(f'cogs.musicas.{extension}')
                client.load_extension(f'cogs.musicas.{extension}')
            await ctx.message.channel.send(f'{extension} got reloaded!')
        except:
            await ctx.message.channel.send('an error occurred, or this cog does not exist')
    else:
        await ctx.send('do you not have permission to run this command')

for filename in os.listdir('./cogs'): #cogs will be used to make the code more clean
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')

client.run(betoken)