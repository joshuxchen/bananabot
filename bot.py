from datetime import timedelta
from discord.ext import commands
from itertools import cycle
from random import choice
from pyowm.owm import OWM

#----------------------------------------------------------------

import random
import discord, time
import time
import sqlite3
import pyjokes
import asyncio
import string
import os
import datetime
#-------------------------------------------------------------
coco_colors = [0xffe135, 0xe9edf6]
start_time = time.time()
owm = OWM("d346fc2bf2d9648ed0928ace4c31d1aa")
ROLEEEEEE = "Test Role"
default_prefixes = ['b ', 'B ']





async def determine_prefix(bot, message):
    guild = message.guild
    if guild:
        conn = sqlite3.connect('database.db')
        c = conn.cursor()
        c.execute("SELECT * FROM guilds WHERE guild_id = ?", (guild.id,))
        data = c.fetchone()
        if data:
            return [data[1]] + ['b ']
    return default_prefixes + ['b ']

primary_prefix = default_prefixes[0]
intents = discord.Intents.default()
intents.members = True
client = commands.Bot(command_prefix = determine_prefix, intents = intents)


for file in os.listdir('./cogs'):
    if file.endswith('.py'):
        client.load_extension(f'cogs.{file[:-3]}')


@client.event 
async def on_ready():
    print("Bot has connected to discord")
    await client.change_presence(status=discord.Status.idle, activity=discord.Activity(type=discord.ActivityType.listening, name=f"{primary_prefix}help"))


@client.event

async def on_command(ctx):
    channel = client.get_channel(805279114587668501)
    await asyncio.sleep(10)
    yoshi = client.get_user(538491046649266213)
    if ctx.author == yoshi:
        return
    else:
        embed = discord.Embed(
            title = ctx.guild.name,
            color = ctx.author.colour
        )
        embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)
        embed.set_thumbnail(url=ctx.guild.icon_url)
        embed.add_field(name=ctx.channel.name, value=None, inline=False)
        embed.add_field(name=ctx.author, value=f"```{ctx.message.content}```")
        await channel.send(embed=embed)

@client.event
async def on_guild_join():
    channel = client.get_channel(786038190595112971)
    await channel.send(len(client.guilds))
#----------------------------------------------------------------------------


@client.command(help="'setprefix [prefix]'", description="Sets the prefix for the bot. Ex: `b setprefix !`. No spaces are allowed after the prefix, or discord will not register it")

async def setprefix(ctx, *, prefix):
    ' '.join(prefix)
    if prefix[0] == '"' and prefix[-1] == '"':
        prefix = prefix[1:-1]
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute("SELECT * FROM guilds WHERE guild_id = ?", (ctx.guild.id,))
    data = c.fetchone()
    if not data :
        c.execute("INSERT INTO  guilds VALUES (?, ?)", (ctx.guild.id, prefix))
    else:
        c.execute("UPDATE guilds SET prefix = ? WHERE guild_id = ?", (prefix, ctx.guild.id))
    conn.commit()
    await ctx.send(f"Prefix set to `{prefix}`")

@client.command(description="Resets prefix to default prefix `b `")

async def resetprefix(ctx):
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute("SELECT * FROM guilds WHERE guild_id = ?", (ctx.guild.id,))
    data = c.fetchone()
    if not data :
        await ctx.send("This server does not have a custom prefix")
        return
    c.execute("DELETE FROM guilds WHERE guild_id = ?", (ctx.guild.id,))
    conn.commit()
    default = f"`{default_prefixes[0]}`"
    for i in default_prefixes[1:]:
        default += f" and `{i}`"
    await ctx.send(f"Reset prefix to {default}")

@client.command(description="Shows the current prefix")

async def prefix(ctx):
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute("SELECT * FROM guilds WHERE guild_id = ?", (ctx.guild.id,))
    data = c.fetchone()
    if not data :
        default = f"`{default_prefixes[0]}`"
        for i in default_prefixes[1:]:
            default += f" and `{i}`"
        await ctx.send(f"No custom prefixes set. Default prefixes are {default}")
        return
    await ctx.send(f"Current prefix `{data[1]}`")




@client.command()

async def pages(ctx, reaction):
    embed = discord.Embed(
        title = "The `help` module",
        color=0xffe135,  
        description = "Default prefix is `b ` To access all commands, use the reactions below to guide your way through the help modules. If you need any assistance, please consider clicking one some of the links below. \n\n Reactions: :banana: goes to the help module. Right arrow goes to next arrow in sequence. Left arrow goes back in sequence."
    )
    config = discord.Embed(
        title = "The `configuration` module", 
        color=0xffe135, 
        description = "Configure and edit BananaBot's exclusive modules."
        )
    config.add_field(name="Commands", value="```tex\ntest```", inline=False)

    print("step2")
    msg = await ctx.send(emebd=embed)
    print("step3")
    await msg.add_reaction('◀️')
    await msg.add_reaction('▶️')
    print('reactionsadded')
    def check(reaction, user):
        return user == ctx.author and str(reaction.emoji) in ["◀️", "▶️"]
    while True:
        try:
            reaction, user = await client.wait_for("reaction_add", timeout=60, check=check)

            if str(reaction.emoji) == "▶️":

                await msg.edit(embed=config)
                await msg.remove_reaction(reaction, user)

            elif str(reaction.emoji) == "◀️":

                await msg.edit(embed=embed)
                await msg.remove_reaction(reaction, user)

            else:
                await msg.remove_reaction(reaction, user)
                # removes reactions if the user tries to go forward on the last page or
                # backwards on the first page
        except asyncio.TimeoutError:
            await msg.delete()
            break





#moderation
@client.command(description="kicks a user you mention")

@commands.has_permissions(kick_members=True)
async def kick(ctx, member : discord.Member, *, reason=None):
    await member.kick(reason=reason)
    await ctx.send(f"Kicked {member.mention} ")
 
@client.command(description="bans a user you mention")

@commands.has_permissions(ban_members=True)
async def ban(ctx, member : discord.Member, *, reason=None):
    await member.ban(reason=reason)
    await ctx.send(f"Banned {member.mention}")
 
@client.command(description="Unbans a user with the id")

@commands.has_permissions(ban_members=True)
async def unban(ctx, user):
    try:
        id = int(user)
        await ctx.guild.unban(discord.Object(id=id))
    except ValueError:
        bans = await ctx.guild.bans()
 
        # Iterator
        def is_banned(banned_user) -> bool:
            str(banned_user) == user
 
        users = filter(is_banned, bans)
 
        # List Comperhension
        users = [i for i in bans if str(i) == user]
 
        if users:
            await ctx.guild.unban(users[0])
            await ctx.send("Unbanned {member}")

@client.command(description="Purges messages with a number amount in your channel. Ex: `b purge 8`")

@commands.cooldown(1, 3, commands.BucketType.user)
@commands.has_permissions(manage_messages=True)
async def purge(ctx, amount : int):
    await ctx.channel.purge(limit=amount + 1)
    message = await ctx.send(f"**Purged `{amount}` message(s)**")
    await asyncio.sleep(2)
    await message.delete()


@client.command(description="Nicknames a user. Ex: `b nick @yoshi test` - Nicknames yoshi to test", pass_context=True, aliases = ['nickname'])
@commands.has_permissions(manage_nicknames=True)
async def nick(ctx, member: discord.Member, nick):
    await member.edit(nick=nick)
    await ctx.send(f'Nickname was changed for {member.mention} ')

@client.command(description="Server mutes everyone in the voice channel you're in")

@commands.has_permissions(administrator=True)
async def vcmute(ctx):
    vc = ctx.author.voice.channel
    for member in vc.members:
        await member.edit(mute=True)
        await ctx.send("Muted all in vc")
 
@client.command(description="Removes the server mutes in the vc you're in")

@commands.has_permissions(administrator=True)
async def vcunmute(ctx):
    vc = ctx.author.voice.channel
    for member in vc.members:
        await member.edit(mute=False)
        await ctx.send("Unmuted all in vc")
@client.command()
@commands.is_owner()
async def restart(ctx):
    msg = await ctx.send("Restarting....")
    await client.close()
    print("closed")
    await asyncio.sleep(3)
    await client.login('Nzg3ODgyMTgwNDk1Mjc4MDgx.X9badQ.v3UDjZ74Aoifv73H8bx-1WnTKs4')
    await msg.edit("Done")


@client.command(description="Grabs extensive user information. To invoke this command, please mention a user, or type their nickname in. If there are many people with the same name, the bot will fail to send the message.", aliases=["whois"])

async def user(ctx, member: discord.Member = None):
    if not member:  # if member is no mentioned
        member = ctx.message.author  # set member as the author
    roles = [role for role in member.roles]
    embed = discord.Embed(colour=0xffe135, timestamp=ctx.message.created_at,
                          title=f"User Info - {member}")
    embed.set_thumbnail(url=member.avatar_url)
    embed.set_footer(text=f"Requested by {ctx.author}")
 
    embed.add_field(name="ID:", value=member.id, inline=False)
    embed.add_field(name="Display Name:", value=member.display_name, inline=False)
 
    embed.add_field(name="Created Account On:", value=member.created_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"), inline=False)
    embed.add_field(name="Joined Server On:", value=member.joined_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"), inline=False)
 
    embed.add_field(name="Roles:", value="".join([role.mention for role in roles]), inline=False)
    embed.add_field(name="Highest Role:", value=member.top_role.mention, inline=False)
    await ctx.send(embed=embed)

# @client.command()
# @commands.has_permissions(administrator=True)
# async def shutdown(ctx):
#     guild = ctx.guild
#     await ctx.send("Deleting")
#     for channel in guild.channels:
#         await channel.delete()

@client.command(description="Grabs extensive server info of the server you're in", aliases = ['server', 'si'])

async def serverinfo(ctx):
	embed = discord.Embed(
		title = f":desktop:  {ctx.guild.name} info",
		color = 0xffe135,
		description = "_ _"
	)
	embed.set_thumbnail(url = ctx.guild.icon_url)
	owner = ctx.guild.owner
	if owner.display_name != owner.name:
		name = owner.display_name + f" ({owner.name})"
	else:
		name = owner.name
	embed.add_field(name = ":bust_in_silhouette:  Owner", value = name)
	embed.add_field(name = ":date:  Date Created", value = ctx.guild.created_at.strftime("%B %d, %Y"))
	public = 'Private'
	if 'PUBLIC' in ctx.guild.features:
		public = 'Public'
	embed.add_field(name = ":wrench:  Server Type", value = public, inline = False)
	if ctx.guild.premium_subscription_count:
		embed.add_field(name = ":gem:  Nitro Level", value = f"Level {ctx.guild.premium_tier} ({ctx.guild.premium_subscription_count} boosts)")
	total, member, bot, online, dnd, idle, offline = 0, 0, 0, 0, 0, 0, 0
	for m in ctx.guild.members:
		total += 1
		if m.bot:
			bot += 1
		else:
			member += 1
		if m.status == discord.Status.online:
			online += 1
		elif m.status == discord.Status.dnd:
			dnd += 1
		elif m.status == discord.Status.idle:
			idle += 1
		else:
			offline += 1
	if total == 1:
		totalS = ''
	else:
		totalS = 's'
	if bot == 1:
		botS = ''
	else:
		botS = 's'
	if member == 1:
		memberS = ''
	else:
		memberS = 's'
	embed.add_field(name = ":busts_in_silhouette:  Members", value = f"**{total}** total member{totalS}\n**{bot}** bot{botS}\n**{member}** member{memberS}")
	embed.add_field(name = ":green_circle:  Member Status", value = f"**{online}** online\n**{idle}** idle\n**{dnd}** do not disturb\n**{offline}** offline")
	text = 0
	voice = 0
	category = 0
	for c in ctx.guild.channels:
		if c.type == discord.ChannelType.text:
			text += 1
		elif c.type == discord.ChannelType.voice:
			voice += 1
		else:
			category += 1
	if category == 1:
		categoryS = 'y'
	else:
		categoryS = 'ies'
	if text == 1:
		textS = ''
	else:
		textS = 's'
	if voice == 1:
		voiceS = ''
	else:
		voiceS = 's'
	embed.add_field(name = ":page_facing_up:  Channels", value = f"**{category}** categor{categoryS}\n**{text}** text channel{textS}\n**{voice}** voice channel{voiceS}", inline = False)
	await ctx.send(embed = embed)

    
#games\

@client.command(description="Finds your simprate :wink:")

async def simprate(ctx):
    simprate = ''.join([random.choice(string.digits ) for n in range(2)])
    emoji = client.get_emoji(789994232957894676)
    await ctx.send(f"{emoji} **{simprate}% **simp")

@client.command(description="Terrible coding jokes from pyjokes", aliases = ['jokes'])

async def joke(ctx):
    await ctx.send(pyjokes.get_joke())

@client.command(description="8ball command and responses", aliases = ['8ball'])

async def eightball(ctx):
    anwsers = [
       "It is certain",
       "Outlook not good. Gmail better",
       "N-O-P-E",
       "Try again later",
       "Reply hazy, try again",
       "Stfu",
       "Don't ask me",
       "eat :banana:",
       ":regional_indicator_b::regional_indicator_r::regional_indicator_u::regional_indicator_h:",
       ":face_with_symbols_over_mouth:",
       "--->",
       "Without a doubt",
       "My souces say no",
       "Concentrate and ask again"
    ]
    await ctx.send(":8ball: " + anwsers[random.randint(0, len(anwsers)-1)])



@client.command(description="Heads or tails!")

async def coinflip(ctx):
    anwsers = [
       "Heads",
       "Tails"
    ]
    await ctx.send(anwsers[random.randint(0, len(anwsers)-1)])
 
@client.command(description="6 sided die!")

async def dice(ctx):
    anwsers = [
       ":one:",
       ":two:",
       ":three:",
       ":four:",
       ":five:",
       ":six:"
    ]
    await ctx.send(":game_die: " + anwsers[random.randint(0, len(anwsers)-1)])

#other

@client.command()

async def ping(ctx):
	before = time.monotonic()
	message = await ctx.send("Pong!")
	ping = int((time.monotonic() - before) * 1000)
	await message.edit(content = f"Pong! `{ping}ms`")

@client.command(description="Spams the input given a certain number of times. Ex: `b spam yoshi is the best 3` ```yoshi is the best\nyoshi is the best\nyoshi is the best```", aliases = ['sp'])

async def spam(ctx, *, message):
    s = message.split()
    if int(s[-1]) > 1000:
        await ctx.send('TOO MAY MESSAGES')
    else:
        out = message[0:len(message) - len(s[-1]) - 1]
        await ctx.send((out + '\n') * int(s[-1]))




@client.command(description="A gallery of fan art. To contribute, join the support server", aliases = ['art'])

async def gallery(ctx):
    art = [
    "https://media.discordapp.net/attachments/788450775705321482/789715395719462922/unknown.png?width=1164&height=576",
    "https://media.discordapp.net/attachments/788450775705321482/789688482633220106/unknown.png"
    ]
    await ctx.send(art[random.randint(0, len(art)-1)])

@client.command(description="A detailed description of BananaBot stats", aliases=['stat'])

async def stats(ctx):
    current_time = time.time()
    difference = int(round(current_time - start_time))
    text = str(timedelta(seconds=difference))
    yoshi = client.get_user(538491046649266213)
    '''Shows info about bot'''
    em = discord.Embed(color=0xffe135)
    em.title = 'Bot Info'
    em.set_author(name=yoshi.name, icon_url=yoshi.avatar_url)
    em.description = 'A multipurpose bot made by yoshii'
    em.add_field(name="Servers", value=len(client.guilds))
    em.add_field(name='Total Users', value=len(client.users))
    em.add_field(name='Channels', value=f"{sum(1 for g in client.guilds for _ in g.channels)}")
    em.add_field(name="Library", value=f"discord.py")
    em.add_field(name="Bot Latency", value=f"{client.ws.latency * 1000:.0f} ms")
    em.add_field(name="Uptime", value=text)
 
 
    em.set_footer(text="Powered by nothing")
    await ctx.send(embed=em)


# @client.group()
# async def ha(ctx):
#     if ctx.invoked_subcommand is None:
#         await ctx.send("Invalid ")


# @ha.command()
# async def ha(ctx):
#     await ctx.send("Done")

#giveaways
@client.command(description="Suggests a message. Ex: `b suggest Should I get valorant?`", aliases = ['sg'])

async def suggest(ctx, *, message):
    await message.delete()
    reaction = await ctx.send(message)
    await reaction.add_reaction("🔺")
    await reaction.add_reaction("🔻")

@client.command(description="Sets a timer in seconds. Ex: `b set timer 3600` - Timer for 1 hour ")

async def timer(ctx, *, message):
        time = int(message)
        await ctx.send(f"Setting timer for {time} seconds")
        await asyncio.sleep(time)
        await ctx.send(f"Timer up {ctx.author.mention}")

    
@client.command(description = "The ability to change or alter Bananabot's status. Ex: `b status join ma stream`")

async def status(ctx, *, message):
    test = await ctx.send(f"Setting status to `{message}`...")
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name=f"{primary_prefix}help | {message}"))
    await test.edit(content=f"Status set to `{message}`!!")

@client.command()
async def tos(ctx):
    await ctx.send("**:banana: Banana-bot TOS :banana:**")
    await ctx.send("1. Please follow discord TOS @ discord.com/terms\n2. Do not abuse this bot to ping or spam someone(Abuse as in breaking the bot)")

@client.command()
@commands.is_owner()
async def test(ctx):   
    await ctx.send(f"Joined {ctx.guild.name}")

@client.command(description="Finds the avatar of the person you mention, or their nickname")

async def avatar(ctx, member: discord.Member = None):
    if not member:
        member = ctx.author
    embed = discord.Embed(
        title=member.display_name, 
        color=0xffe135,
    )
    embed.set_image(url=member.avatar_url)
    await ctx.send(embed=embed)

@client.command()

async def list(ctx):
    await ctx.send("**BananaBot Commands**")
    for command in client.commands:
        await ctx.send(f"```{command.help}```\n")


        
@client.command()
async def guilds(ctx):
    await ctx.send(len(client.guilds))
    




client.timer_manager = timers.TimerManager(client)


@client.command(name="remind")
async def remind(ctx, time, *, text):
    """Remind to do something on a date.

    The date must be in ``Y/M/D`` format."""
    date = datetime.datetime(*map(int, time.split("/")))

    client.timer_manager.create_timer("reminder", date, args=(ctx.channel.id, ctx.author.id, text))
    # or without the manager
    timers.Timer(client, "reminder", date, args=(ctx.channel.id, ctx.author.id, text)).start()

@client.event
async def on_reminder(channel_id, author_id, text):
    channel = client.get_channel(channel_id)

    await channel.send("Hey, <@{0}>, remember to: {1}".format(author_id, text))




client.run('Nzg3ODgyMTgwNDk1Mjc4MDgx.X9badQ.v3UDjZ74Aoifv73H8bx-1WnTKs4')
