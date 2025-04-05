import discord
import asyncio

async def run_mass_ban(guild, token):
    """
    Mass ban all users in the guild. Will be triggered from the bot.
    """
    banned_users = []
    error_users = []
    for member in guild.members:
        try:
            await member.ban(reason="Mass ban executed.")
            banned_users.append(f"{member.name} ({member.id})")
        except discord.Forbidden:
            error_users.append(f"{member.name} ({member.id}) - Forbidden")
        except discord.HTTPException as e:
            error_users.append(f"{member.name} ({member.id}) - Error: {str(e)}")
        await asyncio.sleep(1)  # Optional delay between bans to prevent rate-limiting

    return banned_users, error_users
