import discord
from discord.ext import commands
import wikipedia
from datetime import datetime

# Create an auto-sharded bot instance with a command prefix and 5 shards
intents = discord.Intents.all()
bot = commands.AutoShardedBot(command_prefix='!', shards=5, intents=intents)

@bot.event
async def on_ready():
    """Event triggered when the bot is ready."""
    print(f'{bot.user} has connected to Discord!')

@bot.command(name='hello', aliases=['hi'], help='Greet the user')
async def hello(ctx: commands.Context):
    """Command to greet the user."""
    await ctx.send(f'Hello {ctx.author.name}!')

@bot.command(name='botinfo', aliases=['info'], help='Display bot information')
async def botinfo(ctx: commands.Context):
    """Command to display bot information."""
    bot_info = f'Bot Name: {bot.user.name}\nBot ID: {bot.user.id}\nNumber of Shards: {bot.shard_count}'
    await ctx.send(bot_info)

@bot.command(name='wikipedia', aliases=['wiki'], help='Get a summary from Wikipedia')
async def wikipedia_summary(ctx: commands.Context, *, query: str):
    """Command to get a Wikipedia summary for a given query."""
    try:
        summary = wikipedia.summary(query, sentences=3)
        await ctx.send(f'**Wikipedia Summary for {query}:**\n{summary}')
    except wikipedia.exceptions.DisambiguationError as e:
        await ctx.send(f'Multiple results found. Please be more specific.\nOptions: {", ".join(e.options)}')
    except wikipedia.exceptions.PageError:
        await ctx.send(f'No results found for {query}.')

@bot.command(name='serverinfo', aliases=['sinfo'], help='Display server information')
async def serverinfo(ctx: commands.Context):
    """Command to display information about the server using an embed."""
    server = ctx.guild
    embed = discord.Embed(title=f'Server Information - {server.name}', color=discord.Color.blue())
    embed.add_field(name='Server ID', value=server.id, inline=False)
    embed.add_field(name='Members', value=server.member_count, inline=False)
    embed.add_field(name='Owner', value=server.owner.name, inline=False)
    embed.add_field(name='Created At', value=server.created_at.strftime('%Y-%m-%d %H:%M:%S'), inline=False)
    await ctx.send(embed=embed)

@bot.command(name='userinfo', aliases=['uinfo'], help='Display user information')
async def userinfo(ctx: commands.Context, user: discord.Member = None):
    """Command to display information about a user using an embed."""
    user = user or ctx.author
    embed = discord.Embed(title=f'User Information - {user.name}', color=discord.Color.green())
    embed.set_thumbnail(url=user.avatar.url)
    embed.add_field(name='User ID', value=user.id, inline=False)
    embed.add_field(name='Joined Server', value=user.joined_at.strftime('%Y-%m-%d %H:%M:%S'), inline=False)
    embed.add_field(name='Joined Discord', value=user.created_at.strftime('%Y-%m-%d %H:%M:%S'), inline=False)
    await ctx.send(embed=embed)

bot.run('MTE3NzYwMTMyMDc1NzIzMTYxNg.GnXFeA.WBUZFHbcOxQzoc4bl6BLtFWp0JaTHW7qtAbAyM')
