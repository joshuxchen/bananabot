
import discord
from discord.ext import commands
from discord.ext.commands import Cog

import discord


class mod(commands.Cog):

    def __init__(self, client):
        self.client = client
        self.get_channel = client.get_channel

    @commands.command(description="Toggle locks a channel (turns off send message for @everyone role). Ex: `b lock` - locks the channel, `b lock` (second time) - Unlocks the channel ", aliases = ['l'])
    
    @commands.has_permissions(manage_channels=True)
    async def lock(self, ctx, channel: discord.TextChannel=None):
        channel = channel or ctx.channel

        if ctx.guild.default_role not in channel.overwrites:
            overwrites = {
            ctx.guild.default_role: discord.PermissionOverwrite(send_messages=False)
            }
            await channel.edit(overwrites=overwrites)
            await ctx.send("**:lock:Locked `{}`**".format(ctx.channel.name))
        elif channel.overwrites[ctx.guild.default_role].send_messages == True or channel.overwrites[ctx.guild.default_role].send_messages == None:
            overwrites = channel.overwrites[ctx.guild.default_role]
            overwrites.send_messages = False
            await channel.set_permissions(ctx.guild.default_role, overwrite=overwrites)
            await ctx.send("**:lock:Locked `{}`**".format(ctx.channel.name))
        else:
            overwrites = channel.overwrites[ctx.guild.default_role]
            overwrites.send_messages = True
            await channel.set_permissions(ctx.guild.default_role, overwrite=overwrites)
            await ctx.send('**:unlock:Unlocked `{}`**'.format(ctx.channel.name))





    @commands.command(description="Nicks everyone in the server. Ex: `b nickall test` - nicks everyone to test", aliases = ['na', 'nicknameall'])
    
    @commands.has_permissions(administrator=True)
    async def nickall(self, ctx, *, args = None):
        if not args:
            msg = await ctx.send(f"02 Depleting")
        else:
            msg = await ctx.send(f"Deploying 02 **{args}**")
        for p in ctx.guild.members:
            try:
                await p.edit(nick = args)
            except:
                pass
        await msg.edit(content = "Cleaned air")


    @commands.command(description="Checks which mods are online")
    
    async def mods(self, ctx):
        """ Check which mods are online on current guild """
        message = ""
        online, idle, dnd, offline = [], [], [], []

        for user in ctx.guild.members:
            if ctx.channel.permissions_for(user).kick_members or \
               ctx.channel.permissions_for(user).ban_members:
                if not user.bot and user.status is discord.Status.online:
                    online.append(f"**{user}**")
                if not user.bot and user.status is discord.Status.idle:
                    idle.append(f"**{user}**")
                if not user.bot and user.status is discord.Status.dnd:
                    dnd.append(f"**{user}**")
                if not user.bot and user.status is discord.Status.offline:
                    offline.append(f"**{user}**")

        if online:
            message += f"🟢 {', '.join(online)}\n"
        if idle:
            message += f"🟡 {', '.join(idle)}\n"
        if dnd:
            message += f"🔴 {', '.join(dnd)}\n"
        if offline:
            message += f"⚫ {', '.join(offline)}\n"

        await ctx.send(f"Online Mods in **{ctx.guild.name}**\n{message}")


        






def setup(client):
    client.add_cog(mod(client))