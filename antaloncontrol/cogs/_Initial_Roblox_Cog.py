import discord
import asyncio
from discord.ext import commands
from ro_py.client import Client

class Roblox_Systems(commands.Cog):

    def __init__(self, Bot):
        self.Bot = Bot
        self.client = Client()
        authenticate_prompt(self.client)

def setup(Bot):
    Bot.add_cog(Roblox_Systems(Bot))