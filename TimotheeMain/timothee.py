from redbot.core import commands

<<<<<<< Updated upstream
class frc(commands.Cog):
    """My custom cog"""

    @commands.command()
    async def frc(self, ctx):
=======
class timothee(commands.Cog):
    """My custom cog"""

    @commands.command()
    async def timothee(self, ctx):
>>>>>>> Stashed changes
        """This does stuff!"""
        # Your code will go here
        await ctx.send("This is a test frc command! If you see this it works!")
