import discord
from discord.ext import commands
from discord import app_commands
from utils.ai_client import ask_ai

class AI(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="chat", description="Talk to AI")
    async def chat(self, interaction: discord.Interaction, message: str):
        try:
            # ⏳ Prevent timeout
            await interaction.response.defer()

            # 🤖 Get AI response
            reply = await ask_ai([{"role": "user", "content": message}])

            # 📤 Send response
            await interaction.followup.send(reply)

        except Exception as e:
            await interaction.followup.send(f"⚠️ Error: {e}")

async def setup(bot):
    await bot.add_cog(AI(bot))
