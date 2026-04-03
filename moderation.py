
import discord
from discord.ext import commands
from discord import app_commands

class Mod(commands.Cog):
    def __init__(self, bot): self.bot=bot

    @app_commands.command(name="ban")
    async def ban(self, i: discord.Interaction, user: discord.Member, reason:str="No reason"):
        await user.ban(reason=reason)
        await i.response.send_message(f"Banned {user}")

    @app_commands.command(name="kick")
    async def kick(self, i: discord.Interaction, user: discord.Member):
        await user.kick()
        await i.response.send_message(f"Kicked {user}")

async def setup(bot):
    await bot.add_cog(Mod(bot))
