from redbot.core import commands

class TimotheeMain(commands.Cog):
    """My custom cog"""

    @commands.command()
    async def beautiful(self, ctx):
        """this does stuff!"""
        await ctx.send("Me? I'm beautiful? I know that already silly :stuck_out_tongue:")
    
    @commands.command()
    async def iwanttofuckenkillmyself(self, ctx):
        await ctx.send("I want to fucken kill myself - Chris 2019")

    @commands.command()
    async def howswefeelin(self, ctx):
        await ctx.send("yee fuckn haw time to die")