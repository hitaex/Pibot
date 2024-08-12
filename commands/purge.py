import discord
from discord import app_commands
from discord.ext import commands

class PurgeUserCommand(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="purge_user", description="Purge messages from a specific user.")
    async def purge_user(self, interaction: discord.Interaction, member: discord.Member, limit: int = 100):
        # Check if the user has permission to manage messages
        if not interaction.user.guild_permissions.manage_messages:
            await interaction.response.send_message("You don't have permission to use this command.", ephemeral=True)
            return

        deleted = 0
        async for message in interaction.channel.history(limit=limit):
            if message.author == member:
                await message.delete()
                deleted += 1

        await interaction.response.send_message(f"Purged {deleted} message(s) from {member.mention}.")

async def setup(bot):
    await bot.add_cog(PurgeUserCommand(bot))
