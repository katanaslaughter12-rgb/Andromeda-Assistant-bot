
import discord
from discord.ext import commands
from utils.config import load

class Logs(commands.Cog):
    def __init__(self, bot): self.bot=bot

    async def send_log(self, guild, msg):
        cfg=load().get(str(guild.id),{})
        cid=cfg.get("log_channel")
        if cid:
            ch=self.bot.get_channel(cid)
            if ch: await ch.send(msg)

    @commands.Cog.listener()
    async def on_message_delete(self, m):
        if m.guild:
            await self.send_log(m.guild, f"🗑️ {m.author}: {m.content}")

async def setup(bot):
    await bot.add_cog(Logs(bot))
