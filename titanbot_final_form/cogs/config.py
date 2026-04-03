
import discord
from discord.ext import commands
from discord import app_commands
from utils.config import load, save

class Config(commands.Cog):
    def __init__(self, bot): self.bot=bot

    @app_commands.command(name="setlog")
    async def setlog(self, i: discord.Interaction, channel: discord.TextChannel):
        d=load()
        g=str(i.guild.id)
        d.setdefault(g,{})["log_channel"]=channel.id
        save(d)
        await i.response.send_message("Log channel set")

async def setup(bot):
    await bot.add_cog(Config(bot))
