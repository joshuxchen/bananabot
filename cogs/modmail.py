
from discord.ext import commands 

class modmail(commands.Cog):
    
    def __init__(self, client):
        self.client = client
        self.messages = {} # Dict for storing sniped messages 

    # @commands.Cog.listener()
    # async def on_message(self, ctx, *, message):
    #     channel = self.client.get_channel(803427928792629298)
    #     if message.guild:
    #         return
    #     else:
    #         await channel.send(message)
    #         await ctx.message.add_reaction('✔️')
            
def setup(client): 
    client.add_cog(modmail(client))