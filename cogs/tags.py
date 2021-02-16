import discord
from discord.ext import commands 

class tags(commands.Cog):
    
    def __init__(self, client):
        self.client = client
        self.messages = {} # Dict for storing sniped messages 

    @commands.group(description="All tags for bananabot!", aliases=['tags'], invoke_without_command=True)
    
    async def tag(self, ctx):
        await ctx.send("list of all commands")

    @tag.command()
    async def yoshi(self, ctx):
        emoji = self.client.get_emoji(799708267790073908)
        msg = await ctx.send(emoji)
        await msg.add_reaction(emoji)

    @tag.command()
    async def help(self, ctx):
        await ctx.send("Can't seem to understand the commands and functions? Here are the most common mistakes\n**You forgot to put a required arg!**```❌: b weather\n✔️: b weather new york```")

    @tag.command()
    async def tos(self, ctx):
        embed = discord.Embed(
            title="Banana-bot TOS",
            color=0xffe135,
            description="""
         __**BananaBot Terms of Service**__
        __Punish List__
        Server:```1st time: Warning\n2nd time: 3 hour cooldown\n3rd time: 1 day cooldown\n4th time: Bot leave\n5th time: Bot blacklist```
        User:```1st time: Warning\n2nd time: 1 day cooldown\n3rd time: 1 week blacklist\n4th time: Perma blacklist```
        __Privacy__
        We **do not** store data of any sort or whatever. However, if someone has reported your server for abuse, we **will** ask you to stop and proceed onto the punish list. 
        __Contact__
        To contact us, join the support server [here](https://discord.gg/768VyfaASp), or email us at `banana.bot.dev@gmail.com`. """
        )
        await ctx.send(embed=embed)

def setup(client): 
    client.add_cog(tags(client))