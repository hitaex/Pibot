import discord
from discord.ext import commands

class TicketCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("TicketCog is ready!")

    @discord.app_commands.command(name="ticket", description="Create a ticket")
    async def ticket(self, interaction: discord.Interaction):
        # Embed for ticket creation
        embed = discord.Embed(
            title="Create Ticket",
            description="Click on the button below to create a ticket.",
            color=discord.Color.from_rgb(255, 255, 255)
        )
        embed.set_footer(text="By @t4em")

        # Embed for ticket confirmation
        embed2 = discord.Embed(
            title="An admin will be with you shortly!",
            description="If you wish to close the ticket click on the button below.",
            color=discord.Color.from_rgb(255, 255, 255)
        )
        embed2.set_footer(text="by @t4em")

        # Button for creating a ticket
        create = discord.ui.Button(style=discord.ButtonStyle.green, label="Create Ticket 📩")
        # Button for closing a ticket
        close = discord.ui.Button(style=discord.ButtonStyle.danger, label="Close ticket 🔒")

        # Button callbacks
        async def create_ticket(interaction: discord.Interaction):
            guild = interaction.guild
            perms = {
                guild.default_role: discord.PermissionOverwrite(view_channel=False),
                interaction.user: discord.PermissionOverwrite(view_channel=True)
            }
            channel = await guild.create_text_channel(f"{interaction.user}'s ticket", overwrites=perms)
            await interaction.response.send_message(f"Ticket created! <#{channel.id}>", ephemeral=True)
            await channel.send(f"{interaction.user.mention}", embed=embed2, view=view2)

        async def close_ticket(interaction: discord.Interaction):
            await interaction.channel.delete()

        # Setting callbacks for the buttons
        create.callback = create_ticket
        close.callback = close_ticket

        # Views for the buttons
        view = discord.ui.View()
        view.add_item(create)
        view2 = discord.ui.View()
        view2.add_item(close)

        await interaction.response.send_message(embed=embed, view=view)

async def setup(bot):
    await bot.add_cog(TicketCog(bot))
