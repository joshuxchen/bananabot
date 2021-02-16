import discord
from discord.ext import commands 

class snipe(commands.Cog):
    
    def __init__(self, client):
        self.client = client
        self.messages = {} # Dict for storing sniped messages 

        

    @commands.Cog.listener()
    async def on_message_delete(self, message):
        self.messages[message.channel.id] = message

    @commands.command(aliases = ['sn'])
    
    async def snipe(self, ctx):
        if ctx.channel.id not in self.messages:
            await ctx.send("No messages to snipe.")
            return
        msg = self.messages[ctx.channel.id]
        embed = discord.Embed(
            description = msg.content,
            color=0xffe135,
            timestamp = msg.created_at
        )
        embed.set_author(name = msg.author.name, icon_url = msg.author.avatar_url)
        await ctx.send(embed = embed)

def setup(client): 
    client.add_cog(snipe(client))