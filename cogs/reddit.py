import discord
from discord.ext import commands
import random
import asyncio
import praw

def setup(client):
    client.add_cog(Reddit(client))

r = praw.Reddit(client_id="ZXvIdPuxyLq_-Q",
    client_secret="WsbwQ9ExCQTO7B7yT3cLIGD2RK4",
    user_agent="bananabot")


class Reddit(commands.Cog):



    def __init__(self, client):
        self.client = client

    @commands.command(description='A "dank" meme straight from reddit.', aliases = ['m'])
    
    async def meme(self, ctx):
        msg = await ctx.send("Loading...")
        submissions = []
        for submission in r.subreddit("dankmemes").hot(limit = 100):
            if submission.score > 100:
                submissions.append(submission)
        submission = submissions[random.randint(0, len(submissions) -1)]
        embed = discord.Embed(
            title = submission.title,
            url = f"https://reddit.com{submission.permalink}",
            color = 0xffe135
        )
        if submission.url.startswith('https://i.redd.it/'):
            embed.set_image(url = submission.url)
            await ctx.send(embed = embed)
        elif submission.url.startswith('https://v.redd.it/'):
            await ctx.send(submission.url)
        else:
            await ctx.send(embed = embed)
            await ctx.send(submission.url)
        await msg.delete()


    @commands.command(description='A "dank" meme straight from reddit.')
    @commands.is_owner()
    async def automeme(self, ctx):
        while True:
            
            msg = await ctx.send("Loading...")
            submissions = []
            for submission in r.subreddit("dankmemes").hot(limit = 100):
                if submission.score > 100:
                    submissions.append(submission)
            submission = submissions[random.randint(0, len(submissions) -1)]
            embed = discord.Embed(
                title = submission.title,
                url = f"https://reddit.com{submission.permalink}",
                color = 0xffe135
            )
            if submission.url.startswith('https://i.redd.it/'):
                embed.set_image(url = submission.url)
                await ctx.send(embed = embed)
            elif submission.url.startswith('https://v.redd.it/'):
                await ctx.send(submission.url)
            else:
                await ctx.send(embed = embed)
                await ctx.send(submission.url)
            await msg.delete()
            await asyncio.sleep(60)

    
    @commands.command(description="Finds the reddit subreddit for the subreddit given. ONLY SUBREDDITS WILL WORK. Ex: `b reddit free` - Shows latest posts about the subreddit free", aliases = ['r', 'reddi', 'redd', 'red', 're'])
    
    async def reddit(self, ctx, subreddit):
        submissions = []
        def check_subreddit(subreddit):
            valid = True
            if subreddit == 'all' or subreddit == 'popular':
                return valid
            try:
                r.subreddit(subreddit).subreddit_type
            except:
                valid = False
            return valid
        if not check_subreddit(subreddit):
            await ctx.send("Invalid subreddit.")
            return
        for submission in r.subreddit(subreddit).hot(limit=50):
            submissions.append(submission)
        submission = submissions[random.randint(0, len(submissions) - 1)]
        embed = discord.Embed(
            description = f"[{submission.title}](https://reddit.com{submission.permalink})",
            title = f"r/{subreddit}",
            color = 0xffe135,
        )
        embed.set_footer(text = f"{submission.score} points | {submission.num_comments} comments")
        if submission.is_self:
            embed.description += f"\n\n{submission.selftext}"
            await ctx.send(embed = embed)
            return
        if submission.over_18 and not ctx.channel.is_nsfw():
            await ctx.send("NSFW commands can only be used in a NSFW channel.")
            return
        if submission.url.startswith('https://i.redd.it/'):
            embed.set_image(url = submission.url)
            await ctx.send(embed = embed)
        elif submission.url.startswith('https://v.redd.it/'):
            await ctx.send(submission.url)
        elif submission.url.startswith('/r/'):
            embed.description += f"\n\nhttps://reddit.com{submission.url}"
            await ctx.send(embed = embed)
        else:
            await ctx.send(embed = embed)
            await ctx.send(submission.url)