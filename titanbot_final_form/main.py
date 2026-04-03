from dotenv import load_dotenv
import os, discord, asyncio
from discord.ext import commands

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

# ✅ ADD YOUR SERVER ID HERE
GUILD_ID = 1483636431774679255

intents = discord.Intents.all()
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"✅ Logged in as {bot.user}")

    guild = discord.Object(id=GUILD_ID)

    # 🔥 CLEAR OLD COMMANDS
    print("🧹 Clearing ALL commands...")
    bot.tree.clear_commands(guild=guild)

    await asyncio.sleep(1)

    # 🔄 SYNC NEW COMMANDS
    print("🔄 Syncing commands...")
    synced = await bot.tree.sync(guild=guild)

    print(f"✅ Synced {len(synced)} commands")
    for cmd in synced:
        print(f"➡️ /{cmd.name}")

# ✅ LOAD COGS
async def load_cogs():
    print("📦 Loading cogs...")
    for file in os.listdir("./cogs"):
        if file.endswith(".py"):
            print(f"Loading {file}")
            await bot.load_extension(f"cogs.{file[:-3]}")

# ✅ MAIN START
async def main():
    async with bot:
        await load_cogs()
        print("🔑 Starting bot...")
        await bot.start(TOKEN)

# ✅ RUN BOT
asyncio.run(main())
