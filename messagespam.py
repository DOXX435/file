# messagespam.py
import discord
import asyncio

async def start_spamming(token, guild_id, message, delay, msg_count):
    intents = discord.Intents.default()
    intents.message_content = True
    intents.guilds = True

    client = discord.Client(intents=intents)

    sent_channels = set()

    async def spam_loop():
        await client.wait_until_ready()
        guild = discord.utils.get(client.guilds, id=int(guild_id))

        if not guild:
            print("[-] Guild not found")
            return

        while True:
            for channel in guild.text_channels:
                if channel.id not in sent_channels:
                    sent_channels.add(channel.id)
                    asyncio.create_task(spam_channel(channel))

            await asyncio.sleep(3)  # Check for new channels every 3 seconds

    async def spam_channel(channel):
        try:
            for _ in range(msg_count):
                await channel.send(message)
                print(f"[+] Sent message in #{channel.name}")
                await asyncio.sleep(delay)
        except discord.HTTPException as e:
            print(f"[=] HTTP Error in #{channel.name}: {e}")
        except Exception as e:
            print(f"[-] Failed to send in #{channel.name}: {e}")

    @client.event
    async def on_ready():
        print("[+] Bot is ready. Starting spammer...")
        asyncio.create_task(spam_loop())

    await client.start(token)
