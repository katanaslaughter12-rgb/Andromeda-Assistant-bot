
import discord
from discord.ext import commands
from discord import app_commands
from utils.ai_client import ask_ai

class AI(commands.Cog):
    def __init__(self, bot): self.bot=bot

    @app_commands.command(name="chat")
    async def chat(self,i:discord.Interaction,message:str):
        await i.response.defer()
        r=await ask_ai([{"role":"user","content":message}])
        await i.followup.send(r)

async def setup(bot):
    await bot.add_cog(AI(bot))
