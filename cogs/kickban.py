import discord
from discord.ext import commands

class misc(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def ban(self,ctx,user: discord.Member,*,reason):
        try:
            await user.ban(reason=reason)
            await ctx.send(f'{user} successfully banned!')
        except:
            await ctx.send(f'This user cannot be banned')
    
    @commands.command()
    async def unban(self,ctx,user: int):
        try:
            people = await self.client.fetch_user(user)
            await ctx.guild.unban(people)
            await ctx.send(f'<@{user}> successfully unbanned!')
        except:
            await ctx.send(f'This user cannot be unbanned')
    
    @commands.command()
    async def kick(self,ctx,user: discord.Member,*,reason):
        try:
            await user.kick(reason=reason)
            await ctx.send(f'{user} successfully kicked!')
        except:
            await ctx.send(f'{user} cannot be kicked')

def setup(client):
    client.add_cog(misc(client))