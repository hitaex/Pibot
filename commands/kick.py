import discord
from discord import app_commands

async def kick(interaction: discord.Interaction, member: discord.Member, reason: str = None):
    await member.kick(reason=reason)
    await interaction.response.send_message(f"{member.mention} has been kicked. Reason: {reason}")

async def setup(bot):
    bot.tree.add_command(
        app_commands.Command(
            name="kick",
            description="Kick a member from the server",
            callback=kick
        )
    )
