import os
import discord
import json
import asyncpg
import ssl
import robloxapi
import asyncio
from discord.ext import commands


#ro-py pip (pip install git+git://github.com/rbx-libdev/ro.py.git)
#Function that retrieves the command prefix by looking for the guilds.id tag in the .json file
def get_prefix(Bot, message):
    with open('prefixes.json', 'r') as f:
        prefixes = json.load(f)

    return prefixes[str(message.guild.id)]

Bot = commands.Bot(command_prefix = get_prefix)
client = robloxapi.Client()

async def create_db_pool():
    ctx = ssl.create_default_context(cafile='./rds-combined-ca-bundle.pem')
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE
    Bot.pg_con = await asyncpg.create_pool(dsn='postgres://jsdggwwzggaaks:eca3f28b5a916440d9b21d594e978f061fa7baaa5d951dd512284430e8df779a@ec2-107-20-15-85.compute-1.amazonaws.com:5432/daoje3etos9o08', ssl=ctx)
@Bot.event
async def on_guild_join(guild):
    with open('prefixes.json', 'r') as f:
        prefixes = json.load(f)
        Bot

    prefixes[str(guild.id)] = '.'

    with open('prefixes.json', 'w') as f:
        json.dump(prefixes, f, indent=4)

@Bot.event
async def on_guild_remove(guild):
    with open('prefixes.json', 'r') as f:
        prefixes = json.load(f)

    prefixes.pop[str(guild.id)]

    with open('prefixes.json', 'w') as f:
        json.dump(prefixes, f, indent=4)

@Bot.command()
async def changeprefix(ctx, new_prefix):
    with open('prefixes.json', 'r') as f:
        prefixes = json.load(f)

    prefixes[str(ctx.guild.id)] = new_prefix

    with open('prefixes.json', 'w') as f:
        json.dump(prefixes, f, indent=4)

@Bot.command()
async def load(ctx, extension):
    Bot.load_extension(f'cogs.{extension}')
    await ctx.send(f'Loading {extension}!')

@Bot.command()
async def unload(ctx, extension):
    Bot.unload_extension(f'cogs.{extension}')
    await ctx.send(f'Unloading {extension}!')

@Bot.command()
async def reload(ctx, extension):
    Bot.load_extension(f'cogs.{extension}')
    Bot.unload_extension(f'cogs.{extension}')
    await ctx.send(f'Reloading {extension}!')

for filename in os.listdir('./cogs'):
    if filename.endswith('.py') and not filename.startswith("_"):
        Bot.load_extension(f'cogs.{filename[:-3]}')
        print(f'Loading cogs.{filename[:-3]}')

Bot.loop.run_until_complete(create_db_pool())
Bot.run('NzcwMDYyMDU3NDcwNTU4MjE4.X5YGLQ.6EFHhTgeKOPKu5ExM1l1VzRWr8E')