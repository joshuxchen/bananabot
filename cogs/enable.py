import discord
from discord.ext import commands 
import asyncio
class enable(commands.Cog):
    
    def __init__(self, client):
        self.client = client

        self.client.remove_command("help")

    @commands.command()
    @commands.is_owner()
    async def toggle(self, ctx, *, command): 
        command = self.client.get_command(command)

        if command is None:
            await ctx.send("Command not found")

        elif ctx.command == command:
            await ctx.send("You cannot disable this command")

        else:
            command.enabled = not command.enabled
            ternary = "Enabled" if command.enabled else "Disabled"
            await ctx.send(f"{ternary} `{command}`")

def setup(client): 
    client.add_cog(enable(client))