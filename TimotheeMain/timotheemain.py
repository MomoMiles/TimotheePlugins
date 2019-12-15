from redbot.core import commands

class TimotheeMain(commands.Cog):
    """My custom cog"""

    @commands.command()
    async def beautiful(self, ctx):
        """Self Confidence Reminder"""
        await ctx.send("You're beautiful. Anyone that tells you otherwise is just trying to hurt you. Don't hate yourself for how you look.")
    
    @commands.command()
    async def iwanttofuckenkillmyself(self, ctx):
        """Chris Command: I want to fucking kill myself"""
        await ctx.send("I want to fucken kill myself - Chris 2019")

    @commands.command()
    async def howswefeelin(self, ctx):
        """Kayleighs Command: Yee Fucking Haw"""
        await ctx.send("yee fuckn haw time to die")