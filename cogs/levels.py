
from discord.ext import commands
import math
import sqlite3

conn = sqlite3.connect('database.db')
c = conn.cursor()


class levels(commands.Cog):

    def __init__(self, client):
        self.client = client

    def find_level(self, xp):
        return int(math.floor((math.sqrt(20 * xp + 25) - 5) / 10))

    def find_xp(self, level):
        return 5 * level * level + (5 * level)

    
    prev = {}

    # @commands.Cog.listener()
    # async def on_message(self, msg):
    #     if msg.author.bot:
    #         return
    #     if msg.guild.id in self.prev:
    #         if msg.author.id == self.prev[msg.guild.id]:
    #             self.prev[msg.guild.id] = msg.author.id
    #             return
    #     c.execute("SELECT * FROM users WHERE id = ?", (msg.author.id,))
    #     data = c.fetchone()
    #     if not data:
    #         c.execute("INSERT INTO users VALUES (?,?,?)", (msg.author.id, msg.author.name, 1))
    #         conn.commit()
    #         return
    #     level = self.find_level(data[2])
    #     new_level = self.find_level(data[2] + 1)
    #     embed = discord.Embed(
    #         title=f"New Level",
    #         description=f"Congrats {msg.author.mention} you have reached level **{new_level}**",
    #         color=0xffe135
    #     )
    #     if level != new_level:
    #         await msg.channel.send(embed=embed)
    #     c.execute("UPDATE users SET xp = ?, name = ? WHERE id = ?", (data[2] + 1, msg.author.name, msg.author.id))
    #     conn.commit()
    #     self.prev[msg.guild.id] = msg.author.id


        

    # @commands.command(description="Shows your current xp level", aliases = ['rank', 'lvl', 'bal'])
    # async def level(self, ctx, user: typing.Optional[discord.Member] = None):
    #     if not user:
    #         user = ctx.author
    #     c.execute("SELECT * FROM users WHERE id = ?", (user.id,))
    #     data = c.fetchone()

    #     current_level = self.find_level(data[2])
    #     desc = f"Level **{current_level}**\n"
    #     desc += f"Total xp: **{data[2]}**\n"

    #     difference = self.find_xp(current_level + 1) - self.find_xp(current_level)
    #     progress = data[2] - self.find_xp(current_level)
    #     desc += f"**{progress}**/**{difference}** xp\n"

    #     bars = round(progress/difference * 20)
    #     dashes = 20 - bars
    #     desc += f"Progress `{'|' * bars + '-' * dashes}`"

    #     embed = discord.Embed(
    #         title = f"{user.name}'s level",
    #         color = 0xffe135,
    #         description = desc,
    #     )
    #     embed.set_thumbnail(url = user.avatar_url)
    #     await ctx.send(f"https://api.no-api-key.com/api/v2/rank/2?current={progress}&total={difference}&level={current_level}&username={ctx.author.name}=offline&barFill=gray&mainColor=white&avatar={ctx.author.avatar_ur}")


    # @commands.command(description="Global xp leaderboard for bananabot", aliases=['glb'])
    # async def globalleaderboard(self, ctx):
    #     c.execute("SELECT * FROM users ORDER BY xp DESC")
    #     data = c.fetchall()
    #     desc = '' 
    #     counter = 0
    #     for user in data:
    #         if counter == 25:
    #             break  
    #         name = user[1]
    #         xp = user[2]
    #         desc += f"#{counter +1} **{name}** - lvl {self.find_level(xp)} - {xp} xp\n"
    #         counter += 1
    #     embed = discord.Embed(
    #         title = "Global Leaderboard",
    #         color = 0xffe135,
    #         description = desc
    #     )
    #     await ctx.send(embed = embed)

    # @commands.command(description="Server xp leaderboard for bananabot", aliases=['lb'])
    # async def leaderboard(self, ctx):
    #     c.execute("SELECT * FROM users ORDER BY xp DESC")
    #     data = c.fetchall()
    #     desc = '' 
    #     counter = 0
    #     for user in data:
    #         if ctx.guild.get_member(user[0]):
    #             if counter == 10:
    #                 break  
    #             name = user[1]
    #             xp = user[2]
    #             desc += f"#{counter +1} **{name}** - lvl {self.find_level(xp)} - {xp} xp\n"
    #             counter += 1
    #     embed = discord.Embed(
    #         title = "Server Leaderboard",
    #         color = 0xffe135,
    #         description = desc
    #     )
    #     await ctx.send(embed = embed)


        



def setup(client):
    client.add_cog(levels(client))