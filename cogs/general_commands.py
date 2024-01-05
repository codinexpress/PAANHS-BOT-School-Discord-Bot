import discord
from discord.ext import commands
import requests
import wikipedia

class GeneralCommands(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def joke(self, ctx):
        response = requests.get('https://official-joke-api.appspot.com/random_joke')
        joke = response.json()
        await ctx.send(joke['setup'] + "\n" + joke['punchline'])

    @commands.command()
    async def wiki(self, ctx, *, search: str):
        summary = wikipedia.summary(search, sentences=3)
        await ctx.send(summary)
