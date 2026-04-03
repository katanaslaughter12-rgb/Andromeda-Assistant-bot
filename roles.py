
import discord
from discord.ext import commands
from discord import app_commands

class Btn(discord.ui.Button):
    def __init__(self, role):
        super().__init__(label=role.name)
        self.role=role
    async def callback(self, i: discord.Interaction):
        if self.role in i.user.roles:
            await i.user.remove_roles(self.role)
            await i.response.send_message("Removed", ephemeral=True)
        else:
            await i.user.add_roles(self.role)
            await i.response.send_message("Added", ephemeral=True)

class Roles(commands.Cog):
    def __init__(self, bot): self.bot=bot

    @app_commands.command(name="rolepanel")
    async def panel(self, i: discord.Interaction, role1: discord.Role, role2: discord.Role=None):
        v=discord.ui.View()
        for r in [role1, role2]:
            if r: v.add_item(Btn(r))
        await i.response.send_message("Roles:", view=v)

async def setup(bot):
    await bot.add_cog(Roles(bot))
