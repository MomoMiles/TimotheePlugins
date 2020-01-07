from redbot.core import commands

class twitch(commands.Cog):
    """My custom cog"""

    @commands.command()
    async def twitchstats(self, ctx):
        """This does stuff!"""
        # Your code will go here
        await ctx.send("This is a test frc command. If you see this it works!")
