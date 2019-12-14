from redbot.core import commands

class Mycog(commands.Cog):
    """My custom cog"""

    @commands.command()
    async def mycom(self, ctx):
        """This does stuff!"""
        # Your code will go here
        await ctx.send("I can do stuff!")

    @commands.command()
    async def beautiful(self, ctx):
        """this does stuff!"""
        await ctx.send("Me? I'm beautiful? I know that already silly :stuck_out_tongue:")