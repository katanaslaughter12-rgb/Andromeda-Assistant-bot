
import json, os, discord
from discord.ext import commands
from discord import app_commands

PATH="data/users.json"

def load():
    if not os.path.exists(PATH): return {}
    return json.load(open(PATH))

def save(d): json.dump(d, open(PATH,"w"))

class Eco(commands.Cog):
    def __init__(self, bot): self.bot=bot

    @commands.Cog.listener()
    async def on_message(self, m):
        if m.author.bot: return
        d=load(); u=str(m.author.id)
        d.setdefault(u,{"bal":0,"xp":0})
        d[u]["xp"]+=1
        save(d)

    @app_commands.command(name="balance")
    async def bal(self, i: discord.Interaction):
        d=load(); u=str(i.user.id)
        await i.response.send_message(str(d.get(u,{"bal":0})["bal"]))

    @app_commands.command(name="daily")
    async def daily(self, i: discord.Interaction):
        d=load(); u=str(i.user.id)
        d.setdefault(u,{"bal":0,"xp":0})
        d[u]["bal"]+=100
        save(d)
        await i.response.send_message("100 added")

async def setup(bot):
    await bot.add_cog(Eco(bot))
