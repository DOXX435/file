import discord
from discord.ext import commands
import asyncio

# Role Spammer logic
async def role_spammer(guild, cfg):
    """
    Creates and spams roles.
    - guild: The discord server (guild) where roles will be created.
    - cfg: Configuration dictionary containing role settings.
    """
    print("[=] Creating and Spamming roles...", "yellow")

    role_count = cfg["role_count"]
    role_name = cfg["role_name"]
    role_color = discord.Color(int(cfg["role_color"], 16))  # Convert hex color to discord color
    message_count = cfg["message_count"]

    for i in range(role_count):
        try:
            # Create the role with the specified color
            role = await guild.create_role(name=f"{role_name}-{i+1}", color=role_color)
            print(f"[+] Created role: {role.name}", "green")

            # Send messages with the created role
            for _ in range(message_count):
                try:
                    # Sending a message that mentions the role
                    await guild.default_channel.send(f"Role spam: {role.mention}")
                    print(f"[+] Sent message with role: {role.name}", "green")
                except Exception as e:
                    print(f"[-] Error sending message with role {role.name}: {e}", "red")
        except Exception as e:
            print(f"[-] Error creating role {role_name}-{i+1}: {e}", "red")
