from .twitch import Twitch


def setup(bot):
    bot.add_cog(Twitch())
