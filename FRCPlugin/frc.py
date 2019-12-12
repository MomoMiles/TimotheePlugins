from redbot.core import commands

class frc(commands.Cog):
    """My custom cog"""

    @commands.command()
    async def frc(self, ctx):
        """This does stuff!"""
        # Your code will go here
        await ctx.send("This is a test frc command. If you see this it works!")
