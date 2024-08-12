import discord
import random
from discord import app_commands
import datetime
import requests
import pytz
import pyfiglet

# 1. Ping command
async def ping(interaction: discord.Interaction):
    await interaction.response.send_message("Pong!")

# 2. Echo command
async def echo(interaction: discord.Interaction, message: str):
    await interaction.response.send_message(message)

# 3. Say hello command
async def say_hello(interaction: discord.Interaction):
    await interaction.response.send_message(f"Hello, {interaction.user.mention}!")

# 4. Server info command
async def server_info(interaction: discord.Interaction):
    guild = interaction.guild
    embed = discord.Embed(title=guild.name, description=f"Server Info for {guild.name}")
    embed.add_field(name="Server ID", value=guild.id)
    embed.add_field(name="Owner", value=guild.owner)
    embed.add_field(name="Member Count", value=guild.member_count)
    await interaction.response.send_message(embed=embed)

# 5. Roll command
async def roll(interaction: discord.Interaction):
    result = random.randint(1, 100)
    await interaction.response.send_message(f"🎲 You rolled a {result}")

# 6. Flip a coin command
async def flipcoin(interaction: discord.Interaction):
    result = random.choice(["Heads", "Tails"])
    await interaction.response.send_message(f"🪙 The coin landed on {result}")

# 7. User info command
async def userinfo(interaction: discord.Interaction, member: discord.Member):
    embed = discord.Embed(title=f"User Info for {member.name}")
    embed.add_field(name="User ID", value=member.id)
    embed.add_field(name="Joined", value=member.joined_at.strftime("%Y-%m-%d %H:%M:%S"))
    embed.add_field(name="Roles", value=", ".join([role.name for role in member.roles]))
    await interaction.response.send_message(embed=embed)

# 8. Create a poll command
async def poll(interaction: discord.Interaction, question: str, option1: str, option2: str):
    embed = discord.Embed(title="Poll", description=question)
    embed.add_field(name="1️⃣", value=option1)
    embed.add_field(name="2️⃣", value=option2)
    message = await interaction.response.send_message(embed=embed)
    await message.add_reaction("1️⃣")
    await message.add_reaction("2️⃣")

# 9. Reminder command
async def remindme(interaction: discord.Interaction, time: int, *, task: str):
    await interaction.response.send_message(f"I will remind you about '{task}' in {time} seconds.")
    await discord.utils.sleep_until(discord.utils.utcnow() + datetime.timedelta(seconds=time))
    await interaction.followup.send(f"⏰ Reminder: {task}")

# 10. Avatar command
async def avatar(interaction: discord.Interaction, member: discord.Member):
    await interaction.response.send_message(f"{member.name}'s avatar: {member.avatar.url}")

# 11. Clear command
async def clear(interaction: discord.Interaction, amount: int):
    deleted = await interaction.channel.purge(limit=amount)
    await interaction.response.send_message(f"Deleted {len(deleted)} messages.", ephemeral=True)

# 12. Dice command
async def dice(interaction: discord.Interaction):
    result = random.randint(1, 6)
    await interaction.response.send_message(f"🎲 You rolled a {result}")

# 13. Weather command
async def weather(interaction: discord.Interaction, city: str):
    api_key = "YOUR_OPENWEATHERMAP_API_KEY"  # Replace with your actual API key
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url).json()
    if response["cod"] != "404":
        weather_desc = response["weather"][0]["description"]
        temperature = response["main"]["temp"]
        await interaction.response.send_message(f"The weather in {city} is {weather_desc} with a temperature of {temperature}°C.")
    else:
        await interaction.response.send_message("City not found.")

# 14. Joke command
async def joke(interaction: discord.Interaction):
    jokes = [
        "Why don’t skeletons fight each other? They don’t have the guts.",
        "What do you call cheese that isn't yours? Nacho cheese.",
        "Why couldn’t the bicycle stand up by itself? It was two-tired."
    ]
    await interaction.response.send_message(random.choice(jokes))

# 15. Quote command
async def quote(interaction: discord.Interaction):
    quotes = [
        "The greatest glory in living lies not in never falling, but in rising every time we fall. - Nelson Mandela",
        "The way to get started is to quit talking and begin doing. - Walt Disney",
        "Your time is limited, so don't waste it living someone else's life. - Steve Jobs"
    ]
    await interaction.response.send_message(random.choice(quotes))

# 16. Fact command
async def fact(interaction: discord.Interaction):
    facts = [
        "Honey never spoils.",
        "Bananas are berries, but strawberries aren't.",
        "A group of flamingos is called a 'flamboyance'."
    ]
    await interaction.response.send_message(random.choice(facts))

# 17. Define command
async def define(interaction: discord.Interaction, word: str):
    url = f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}"
    response = requests.get(url).json()
    if isinstance(response, list):
        definition = response[0]["meanings"][0]["definitions"][0]["definition"]
        await interaction.response.send_message(f"**{word}**: {definition}")
    else:
        await interaction.response.send_message(f"No definition found for {word}.")

# 18. Translate command
async def translate(interaction: discord.Interaction, word: str, target_language: str):
    url = f"https://api.mymemory.translated.net/get?q={word}&langpair=en|{target_language}"
    response = requests.get(url).json()
    translation = response["responseData"]["translatedText"]
    await interaction.response.send_message(f"Translation: {translation}")

# 19. Time command
async def time(interaction: discord.Interaction, timezone: str):
    try:
        tz = pytz.timezone(timezone)
        current_time = datetime.datetime.now(tz).strftime("%Y-%m-%d %H:%M:%S")
        await interaction.response.send_message(f"The current time in {timezone} is {current_time}")
    except pytz.UnknownTimeZoneError:
        await interaction.response.send_message("Unknown timezone")

# 20. Calculate command
async def calc(interaction: discord.Interaction, expression: str):
    try:
        result = eval(expression)
        await interaction.response.send_message(f"The result is {result}")
    except Exception as e:
        await interaction.response.send_message(f"Error: {str(e)}")

# 21. ASCII art command
async def ascii_art(interaction: discord.Interaction, text: str):
    result = pyfiglet.figlet_format(text)
    await interaction.response.send_message(f"```{result}```")

# 22. Meme command
async def meme(interaction: discord.Interaction):
    url = "https://meme-api.herokuapp.com/gimme"
    response = requests.get(url).json()
    await interaction.response.send_message(response["url"])

async def setup(bot):
    commands = [
        app_commands.Command(name="ping", description="Ping the bot", callback=ping),
        app_commands.Command(name="echo", description="Echo the message", callback=echo),
        app_commands.Command(name="say_hello", description="Say hello to the user", callback=say_hello),
        app_commands.Command(name="server_info", description="Get server information", callback=server_info),
        app_commands.Command(name="roll", description="Roll a random number between 1 and 100", callback=roll),
        app_commands.Command(name="flipcoin", description="Flip a coin", callback=flipcoin),
        app_commands.Command(name="userinfo", description="Get information about a user", callback=userinfo),
        app_commands.Command(name="poll", description="Create a poll", callback=poll),
        app_commands.Command(name="remindme", description="Set a reminder", callback=remindme),
        app_commands.Command(name="avatar", description="Display a user's avatar", callback=avatar),
        app_commands.Command(name="clear", description="Clear a number of messages", callback=clear),
        app_commands.Command(name="dice", description="Roll a dice", callback=dice),
        app_commands.Command(name="weather", description="Get the current weather", callback=weather),
        app_commands.Command(name="joke", description="Tell a random joke", callback=joke),
        app_commands.Command(name="quote", description="Get a random quote", callback=quote),
        app_commands.Command(name="fact", description="Get a random fact", callback=fact),
        app_commands.Command(name="define", description="Get the definition of a word", callback=define),
        app_commands.Command(name="translate", description="Translate a word or sentence", callback=translate),
        app_commands.Command(name="time", description="Get the current time in a specific timezone", callback=time),
        app_commands.Command(name="calc", description="Calculate an expression", callback=calc),
        app_commands.Command(name="ascii_art", description="Convert text to ASCII art", callback=ascii_art),
        app_commands.Command(name="meme", description="Get a random meme", callback=meme)
    ]

    for command in commands:
        bot.tree.add_command(command)
