import discord
import inspect
from discord.ext import commands 
import asyncio
class help(commands.Cog):
    
    def __init__(self, client):
        self.client = client

        self.client.remove_command("help")


    @commands.command(description="List of all commands")
    async def help(self, ctx, command = None):
        if command:
            com = commands.Bot.get_command(self.client, str(command))
            embed = discord.Embed(
                title = f"Command `{com}`",
                color = 0xffe135
            )
            embed.add_field(name="Description", value=str(com.description), inline=False)
            if len(com.aliases) > 0:
                for a in com.aliases:
                    continue
                embed.add_field(name="Aliases", value=str(a), inline=False)
            if com.checks:
                permissions = {}
                for check in com.checks:
                    permissions.update({
                        check.__qualname__.split(".", 1)[0]: check.__closure__[0].cell_contents
                    })
                    embed.add_field(name="Permissions", value=str(permissions), inline=False)
            if com.enabled == False:
                embed.add_field(name="Disabled", value="This command is disabled", inline=False)
            embed.set_footer(text="Need more help? Type b tag help")
            await ctx.send(embed=embed)
        else:
            yoshi = self.client.get_user(787882180495278081)
            music = self.client.get_emoji(804137593297174608)
            mod = self.client.get_emoji(804143768306712646)
            games = self.client.get_emoji(804145011670384640)
            images = self.client.get_emoji(799708210591825960)
            lennnn = len(self.client.commands)
            help = discord.Embed(
                color=0xffe135, 
                description = "Default prefix is `b ` To change prefix, type `b setprefix {your_prefix_here}`. If you need more assistance, please consider clicking one of the links below.\nLinks: [Support Server](https://discord.gg/768VyfaASp), [Invite](https://discord.com/api/oauth2/authorize?client_id=787882180495278081&permissions=8&scope=bot), Website \nCommands with an `(x)` are under maintainance\n**To view specific details of a command, type `b help {insert_command}`\n`[]` is a optional argument but `<>` is a mandatory requirement** To view bot TOS, type `b tag tos`"
            )
            help.set_thumbnail(url=yoshi.avatar_url)
            help.set_author(name="Help Page", icon_url=yoshi.avatar_url)
            help.add_field(name=":gear: Configuration", value="""Configuring <@787882180495278081> & servers!
            ```\nsetprefix\nremoveprefix\nprefix\nshutdown (x)\nserver\nwhois\nstats\nping```""")
            help.add_field(name=f"{mod} Moderation", value="""Simple but ***powerful*** moderation!!
            ```\nmods\nkick\nban\nunban (x)\npurge\nnick\nnickall\nlock\nsnipe\nvcmute\nvcunmute```""")
            help.add_field(name=":face_with_raised_eyebrow: Meta", value="""Basically the "other" category
            ```css\nglb\nlb\nlevel\nweather\ndictionary\ncovid\nsuggest\ntimer\ntag\nstatus```""")
            help.add_field(name=f"{games} Games", value="""Fun games that give xp!
            ```fix\ncoinflip\ndice\n8ball\ngallery\njoke\nspam\nbet\ntrivia\ndefine\nreddit```""")
            help.add_field(name=f"{images} Images", value="""Image based commands!
            ```yaml\nmeme\ndog\ncat\navatar```""")
            help.add_field(name=f"{music} Music", value="""Top notch high quality music!
            ```tex\n$about (x)\nplay\nstop\npause\nresume\nshuffle\nqueue\nnow\nremove\nvolume```""")
            help.set_footer(text=f"{lennnn} commands")
            await ctx.send(embed=help)


        
def setup(client): 
    client.add_cog(help(client))
