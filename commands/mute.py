import discord
from discord import app_commands

async def mute(interaction: discord.Interaction, member: discord.Member):
    mute_role = discord.utils.get(interaction.guild.roles, name="Muted")
    if not mute_role:
        mute_role = await interaction.guild.create_role(name="Muted")
        for channel in interaction.guild.channels:
            await channel.set_permissions(mute_role, speak=False, send_messages=False)
    await member.add_roles(mute_role)
    await interaction.response.send_message(f"{member.mention} has been muted.")

async def setup(bot):
    bot.tree.add_command(
        app_commands.Command(
            name="mute",
            description="Mute a member in the server",
            callback=mute
        )
    )
