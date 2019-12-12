from redbot.core import commands

class timothee(commands.Cog):
    """My custom cog"""

    @commands.command()
    async def timothee(self, ctx):
        """This does stuff!"""
        # Your code will go here
        await ctx.send("This is a test timothee command. If you see this it works!")
