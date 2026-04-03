
import discord
from discord.ext import commands
from discord import app_commands

class V(discord.ui.View):
    @discord.ui.button(label="Open Ticket", style=discord.ButtonStyle.green)
    async def open(self, i: discord.Interaction, b: discord.ui.Button):
        ch=await i.guild.create_text_channel(f"ticket-{i.user.name}")
        await ch.send(f"{i.user.mention} support will assist.")
        await i.response.send_message("Created", ephemeral=True)

class Tickets(commands.Cog):
    def __init__(self, bot): self.bot=bot

    @app_commands.command(name="ticketpanel")
    async def panel(self, i: discord.Interaction):
        await i.response.send_message("Open ticket:", view=V())

async def setup(bot):
    await bot.add_cog(Tickets(bot))
