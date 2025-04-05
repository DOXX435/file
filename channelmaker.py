# channelmaker.py
import discord
import asyncio
import random

emojis = ["💣", "🔥", "😈", "👻", "⚡", "🎯", "💀", "🧨", "🚨", "📛"]

async def create_channels(token, guild_id, base_name, count, delay):
    intents = discord.Intents.default()
    client = discord.Client(intents=intents)

    @client.event
    async def on_ready():
        guild = discord.utils.get(client.guilds, id=int(guild_id))
        if not guild:
            print(f"[-] Guild with ID {guild_id} not found.")
            await client.close()
            return

        for i in range(1, count + 1):
            emoji = random.choice(emojis)
            name = f"{emoji}-{base_name}-{i}"
            try:
                await guild.create_text_channel(name)
                print(f"[+] Created channel: {name}")
            except Exception as e:
                print(f"[-] Failed to create {name} - {e}")
            await asyncio.sleep(delay)

        await client.close()

    await client.start(token)
