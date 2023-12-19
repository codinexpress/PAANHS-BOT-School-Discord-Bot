import discord
import logging
from logging.handlers import RotatingFileHandler
import os
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()

# Get the bot token from the environment variable
bot_token = os.getenv("DISCORD_TOKEN")

# Create the "logs" directory if it doesn't exist
log_dir = "logs"
os.makedirs(log_dir, exist_ok=True)

# Create a rotating file handler for the bot's logger
handler = RotatingFileHandler(
    filename=os.path.join(log_dir, "panhs_bot.log"),
    encoding='utf-8',
    maxBytes=12 * 1024 * 1024,  # 12 MiB
    backupCount=8,  # Rotate through 8 files
)

# Add the handler to the logger
logger = logging.getLogger('panhs_bot')
logger.addHandler(handler)

# Create an instance of the auto-sharded bot
intents = discord.Intents.all()
bot = discord.AutoShardedClient(intents=intents)

# Function to load all cogs listed in cogs.txt
def load_cogs():
    cog_dir = "cogs"
    
    with open("cogs.txt", "r") as file:
        cogs = [line.strip() for line in file.readlines()]

    for cog in cogs:
        cog_path = os.path.join(cog_dir, cog + ".py")
        try:
            bot.load_extension(cog_path)
            logger.info(f"Cog '{cog}' loaded successfully.")
        except Exception as e:
            logger.error(f"Error loading cog '{cog}': {e}")

# Load all cogs before the bot starts
load_cogs()

# Event triggered when the bot is ready
@bot.event
async def on_ready():
    logger.info(f'Logged in as {bot.user.name} (ID: {bot.user.id})')
    logger.info('------')

# Run the bot
bot.run(BOT_TOKEN)
