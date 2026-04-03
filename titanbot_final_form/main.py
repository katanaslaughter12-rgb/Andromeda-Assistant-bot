
from dotenv import load_dotenv
import os, discord, asyncio
from discord.ext import commands

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.all()
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"✅ Logged in as {bot.user}")

    guild = discord.Object(id=GUILD_ID)

    # 🔥 FULL RESET
    print("🧹 Clearing ALL commands...")
    bot.tree.clear_commands(guild=guild)

    await asyncio.sleep(1)

    print("🔄 Syncing commands...")
    synced = await bot.tree.sync(guild=guild)

    print(f"✅ Synced {len(synced)} commands")

    for cmd in synced:
        print(f"➡️ /{cmd.name}")

asyncio.run(main())
