
TOKEN = 'token'
import discord
from discord.ext import commands
import os
import importlib
import asyncio

intents = discord.Intents.default()
intents.message_content = True
intents.members = True
intents.guilds = True
intents.voice_states = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Bot is Up and Ready! Logged in as {bot.user}")
    try:
        synced = await bot.tree.sync()
        print(f"Synced {len(synced)} command(s)")
    except Exception as e:
        print(f"Error syncing commands: {e}")

async def load_commands():
    for filename in os.listdir('./commands'):
        if filename.endswith('.py'):
            module_name = filename[:-3]
            try:
                module = importlib.import_module(f'commands.{module_name}')
                await module.setup(bot)
            except Exception as e:
                print(f"Error loading {filename}: {e}")

async def main():
    await load_commands()
    await bot.start(TOKEN)

if __name__ == "__main__":
    asyncio.run(main())
