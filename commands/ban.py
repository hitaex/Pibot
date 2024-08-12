import discord
from discord import app_commands
from discord.ext import commands

class BanCommand(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="ban", description="Ban a user from the server.")
    async def ban(self, interaction: discord.Interaction, member: discord.Member, reason: str = "No reason provided"):
        if not interaction.user.guild_permissions.ban_members:
            await interaction.response.send_message("You don't have permission to use this command.", ephemeral=True)
            return

        await member.ban(reason=reason)
        await interaction.response.send_message(f"{member.mention} has been banned for: {reason}")

async def setup(bot):
    await bot.add_cog(BanCommand(bot))
