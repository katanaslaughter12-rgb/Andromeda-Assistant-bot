
import random, discord
from discord.ext import commands, tasks
from discord import app_commands

Q=["Best game?","Dream job?","Goal?"]

class Q(commands.Cog):
    def __init__(self, bot):
        self.bot=bot; self.cid=None; self.loop.start()

    @app_commands.command(name="setqotd")
    async def set(self,i:discord.Interaction,ch:discord.TextChannel):
        self.cid=ch.id
        await i.response.send_message("set")

    @tasks.loop(hours=24)
    async def loop(self):
        if self.cid:
            ch=self.bot.get_channel(self.cid)
            if ch: await ch.send(random.choice(Q))

async def setup(bot):
    await bot.add_cog(Q(bot))
