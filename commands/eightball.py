import discord
import random
from discord import app_commands

async def eight_ball(interaction: discord.Interaction, question: str):
    responses = [
        "It is certain.", "It is decidedly so.", "Without a doubt.",
        "Yes – definitely.", "You may rely on it.", "As I see it, yes.",
        "Most likely.", "Outlook good.", "Yes.", "Signs point to yes.",
        "Reply hazy, try again.", "Ask again later.", "Better not tell you now.",
        "Cannot predict now.", "Concentrate and ask again.", "Don't count on it.",
        "My reply is no.", "My sources say no.", "Outlook not so good.",
        "Very doubtful."
    ]
    response = random.choice(responses)
    await interaction.response.send_message(f"🎱 {response}")

async def setup(bot):
    bot.tree.add_command(
        app_commands.Command(
            name="8ball",
            description="Ask the magic 8-ball a question",
            callback=eight_ball
        )
    )
