import discord
import random
from discord.ext import commands, tasks
import os
import requests
import asyncio
import json
from discord.ext.commands import Bot
import html

import random
import discord
import urllib
import asyncio
import aiohttp
import typing
from covid import Covid

class games(commands.Cog):

    def __init__(self, client):
        self.client = client
        self.get_channel = client.get_channel

    
    
    
    
    @commands.command(description="Trivia!! A multiple choice trivia question", aliases = ['t'])
    
    async def trivia(self, ctx):
        data = requests.get("https://opentdb.com/api.php?amount=1&type=multiple").json()
        results = data['results'][0]
        embed = discord.Embed(
            title = ":question: Trivia",
            description = f"Category: {results['category']} | Difficulty: {results['difficulty'].capitalize()}",
            color = 0xffe135
        )
        pos = random.randint(0,3)
        if pos == 3:
            results['incorrect_answers'] + [results['correct_answer']]
        else:
            answers = results['incorrect_answers'][0:pos] + [results['correct_answer']] + results['incorrect_answers'][pos:]
        print(answers)
        value = ''
        letters = ['a', 'b', 'c', 'd']
        for a in range(len(answers)):
            value += f"{letters[a].capitalize()}) {answers[a]}\n"
        embed.add_field(name = html.unescape(results['question']), value = value)
        embed2 = embed
        question = await ctx.send(embed = embed)
        available_commands = letters + [a.lower() for a in answers]
        def check(m):
            return m.channel == ctx.channel and m.content.lower() in available_commands
        try:
            msg = await self.client.wait_for('message', timeout = 30.0, check = check)
        except asyncio.TimeoutError:
            await ctx.send("Timed Out")
            return
        answer_string = f"The answer was **{letters[pos].upper()}) {results['correct_answer']}**"
        if msg.content.lower() == letters[pos] or msg.content.lower() == results['correct_answer'].lower():
            name = ":white_check_mark:  Correct"
        else:
            name = ":x:  Incorrect"
        embed2.clear_fields()
        embed2.add_field(name = name, value = answer_string)
        await question.edit(embed = embed2)


    
    @commands.command(description="Say something in an embed. Ex: `b say test`  - says test in an embed")
    
    async def esay(self, ctx, *, message):
        await ctx.message.delete()

        embed = discord.Embed(title="Paradise", description=message, color=0xffe135)

        # embed.add_field(name=(message), icon_url=ctx.author.avatar_url)


        await ctx.send(embed=embed)

    @commands.command(description="Say something in an embed. Ex: `b say test`  - says test in an embed")
    
    async def say(self, ctx, *, message):
        await ctx.message.delete()


        await ctx.send(message)
        
    @commands.command(aliases=['ks'])
    async def kstats(self, ctx):
        msg = ctx.message.content
        prefix_used = ctx.prefix
        alias_used = ctx.invoked_with
        text = msg[len(prefix_used) + len(alias_used):]
        if text == '':
            await ctx.send(content="Please put a user's IGN after `k stats`!")
            pass

        os.system("clear")
        print("Importing...")
        print("")

        ite=0
        link = "https://krunker.io/social.html?p=profile&q=" + text
        response = requests.get(link)

        requests.get('https://api.github.com')

        if response.status_code == 200:
            print('Successfully connected to webpage.')
            print("Parsing content...")
            print("")
            code = str(response.content)
            codelist = list(code)

            print("Succesfully parsed content.")
            letter = input("Enter Letter you're looking for (surname): ").upper()
            print(f'Parsing HTML for letter(s):{letter}...')
            print("")
            
            codeletter = '">'+letter
            codeletter = codeletter
            #if codeletter in code:
            #  ite+=1
            ite = code.count(codeletter)
            for a in range(0,len(codelist)):
                if codelist[a] == '"':
                    if codelist[a+1] == letter:
                        print("pos: "+str(a))
                        print(code[a]+code[a+1]+code[a+2]+code[a+3])
                
            print(f'Artists with a Surname starting with \'{letter}\': {ite}')
        
        elif response.status_code == 404:
            print('Failed to connect to webpage.')
            print("404 error occured.")

    @commands.command()
    async def f(self, ctx, *, text: commands.clean_content = None):
        embedagain = discord.Embed(
            title = ctx.guild.name,
            description = f"**Channel**: #{ctx.channel.name} \n**User**: {ctx.author.name} \n**Command**: {ctx.message.content}",
            color = 0xffe135
        )
        channel5 = self.get_channel(779041897427501076)
        await channel5.send(embed=embedagain)
        await ctx.message.delete()
        """ Press F to pay respect """
        hearts = ['❤', '💛', '💚', '💙', '💜']
        reason = f"for **{text}** " if text else ""
        await ctx.send(f"**{ctx.author.name}** has paid their respect {reason}{random.choice(hearts)}")


    @commands.command(description="Your classic vegas slot machine into discord")
    
    async def bet(self, ctx):
        message = await ctx.send(content="Rolling....")
        await asyncio.sleep(2)
        await message.edit(content="Calculating....")
        await asyncio.sleep(2)
        await message.edit(content="Configuring....")
        await asyncio.sleep(1)
        emojis = "🍎🍊🍐🍋🍉🍇🍓🍒"
        a = random.choice(emojis)
        b = random.choice(emojis)
        c = random.choice(emojis)

        slotmachine = f"**[ {a} {b} {c} ]\n{ctx.author.name}**,"

        if (a == b == c):
            await message.edit(content=f"{slotmachine} All matching, you won! 🎉")
        elif (a == b) or (a == c) or (b == c):
            await message.edit(content=f"{slotmachine} 2 in a row, you won! 🎉")
        else:
            await message.edit(content=f"{slotmachine} No match, you lost 😢")

            
    # @commands.Cog.listener()
    # async def on_message(self, message):
    #     if message.author.id == 508863359777505290:
    #         await message.add_reaction("🇾")

    # @commands.Cog.listener()
    # async def on_message(self, message):
    #     if message.author.id == 412361868540116992:
    #         await message.add_reaction("🍌")

    @commands.command(description="Doggo", pass_contex=True)
    
    async def dog(self,ctx):
        url = 'https://api.thedogapi.com/v1/images/search'

        response = urllib.request.urlopen(url)
        data = json.load(response)[0]
        image = data['url']
        try:
            data = data['breeds'][0]
        except IndexError:
            data = data['breeds']
        if not data:
            await self.dog(ctx)
        else:
            try:
                fields = {
                    ('Weight',f"{data['weight']['imperial']}lbs.",True),
                    ('Height',f"{data['height']['imperial']}in.",True),
                    ('Breed Group',data['breed_group'] if data['breed_group'] else "N/A",True),
                    ('Life Span',data['life_span'],True),
                    ('Bred for',data['bred_for'] if data['bred_for'] else 'N/A',False),
                    ('Temperament',data['temperament'],False)
                }
                embed=discord.Embed(title=data['name'])
                embed.set_image(url = image)
                for name,value,inline in fields:
                    embed.add_field(name=name,value=value,inline=inline)
                await ctx.send(embed=embed)
            except KeyError:
                await self.dog(ctx)

    @commands.command(description="Dictionary from dictionary.api. Ex: `b dictionary check` - Returns the definion of check with other features")
    
    async def dictionary(self, ctx, term: str):
        async with aiohttp.ClientSession() as session:
            async with session.get(f"https://api.dictionaryapi.dev/api/v1/entries/en/{term}") as r:
                result = await r.json()
        try:
            data = result[0]['meaning']
            key = list(data.keys())[0]
        except KeyError:
            await ctx.send("> Unable to find word!")
            return

        embed = discord.Embed()
        embed.title = f"definition of {term}"
        embed.add_field(name="Definition", value=data[key][0]['definition'])
        try:
            embed.add_field(name="Example", value=data[key][0]['example'])
        except KeyError:
            pass
        try:
            embed.add_field(name="Synonyms", value=data[key][0]['synonyms'])
        except KeyError:
            pass
        await ctx.send(embed=embed)

    @commands.command(description="Urban dictionary. Ex: `b urban test` - returns urban dictionary definition of test", aliases=['define'])  # Creats command object
    
    async def urban(self, ctx, index: typing.Optional[int] = 0, *, term: str):  # Defines command

        async with aiohttp.ClientSession() as session:  # Opens client session
            async with session.get("https://api.urbandictionary.com/v0/define", params={"term": term}) as r:  # Result
                result = await r.json()  # Parses file as json

            data = result["list"][index]  # Assigns list in dict as 'data'

            defin = data["definition"]  # Gets key value
            if "2." in defin:  # If there is a second definition
                defin = data["definition"].split("2.")  # Splits data
                defin = defin[0]  # Sets defin as first definition
            elif len(defin) > 250:  # Sets a 250 character limit
                defin = defin[:250]

            example = data["example"]  # Gets key value
            if "2." in defin:  # If there is a second example splits data
                example = data["example"].split("2.")  # Splits data
                example = example[0]  # Sets defin as first example
            elif len(example) > 250:   # Sets a 250 character limit
                example = example[:250]

            urban_embed = discord.Embed(title="Result for {0}".format(term),
                                        url=data["permalink"],
                                        colour=0x025513)
            # Creates# embed with a title with a hyperlink and set's the colour of the bar
            urban_embed.add_field(name="Definition", value=defin, inline=False)  # Adds field
            urban_embed.add_field(name="Example", value=example or "N/A", inline=False)
            urban_embed.add_field(name="👍", value=data["thumbs_up"], inline=True)
            urban_embed.add_field(name="👎", value=data["thumbs_down"], inline=True)
            urban_embed.set_footer(text="Author: " + data["author"])
            await ctx.send(embed=urban_embed)  # Sends the embed
            return  # Halts further action

    @commands.command(description="Shows covid cases to the county input provided. Ex: `b covid china` - shows covid stats for china. ||Note: this is very slow as there is no accurate and offical api to pull from||")  # Creates a command objec
    
    async def covid(self, ctx, *, region: typing.Optional[str] = "United Kingdom"):  # Defines func with args

        cases = Covid().get_status_by_country_name(region.lower())  # Gets covid 19 information by region from 'Covid'

        msrona = discord.Embed()  # Creates initial discord embed
        msrona.title = "Corona virus statistics for {0}".format(cases["country"])  # Adds a title to embed
        msrona.add_field(name="Confirmed Cases", value="{0}".format(cases["confirmed"]))  # Adds a field to embed
        msrona.add_field(name="Active Cases", value="{0}".format(cases["active"]))  # Adds a field to embed
        msrona.add_field(name="Deaths", value="{0}".format(cases["deaths"]))  # Adds a field to embed
        msrona.add_field(name="Recovered", value="{0}".format(cases["recovered"]))  # Adds a field to embed

        await ctx.send(embed=msrona) 
    @commands.command()
    
    async def cat(self, ctx):
      response = requests.get('https://aws.random.cat/meow')
      data = response.json()
      embed = discord.Embed(
          title = 'Kitty Cat 🐈',
          description = 'Cats :star_struck:',
          colour = discord.Colour.purple()
          )
      embed.set_image(url=data['file'])            
      embed.set_footer(text="")
      await ctx.send(embed=embed)

def setup(client):
    client.add_cog(games(client))