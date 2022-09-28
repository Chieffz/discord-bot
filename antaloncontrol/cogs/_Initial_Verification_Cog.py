import discord
import asyncio
import robloxapi
import random
from discord.ext import commands

class Verification_System(commands.Cog):

    def __init__(self, Bot):
        self.Bot = Bot
        self.client = robloxapi.Client(cookie="")

    @commands.command()
    async def register(self, ctx, *, roblox_name=None):
        await ctx.send(f"Checking to see if you're verified...")
        user_id = str(ctx.author.id)
        guild_id = str(ctx.guild.id)
        verified_user = await self.Bot.pg_con.fetch("SELECT * FROM verification_database WHERE user_id = $1 AND guild_id = $2", user_id, guild_id)
        if not verified_user:
            verified_role = ctx.guild.get_role(775746108294430772)
            rablox_user = str(roblox_name)
            random_number = int(random.uniform(0,1000000))
            group = await self.client.get_group(8186803)
            r_user = await self.client.get_user_by_username(roblox_name=rablox_user)
            async for member in group.get_members():
                if rablox_user == member.name:
                    await ctx.send(f"Please put this string of numbers your roblox user's blurb *{random_number}*. You have 30 seconds; Please make sure that only the string of numbers is in your blurb and nothing else!")
                    await asyncio.sleep(30)
                    r_user_detailed = await r_user.get_detailed_user()
                    r_blurb = r_user_detailed.blurb
                    if int(r_blurb) == random_number:
                        await self.Bot.pg_con.execute("INSERT INTO verification_database (user_id, guild_id, r_user) VALUES ($1, $2, $3)", user_id, guild_id, rablox_user)
                        await ctx.send(f"{ctx.author.mention} You're now registered!")
                        await ctx.author.add_roles(verified_role)
                        break
                    else:
                        await ctx.send(f"{ctx.author.mention} has failed to provide the correct numbers in his/her's blurb!")
        else:
            await ctx.send(f"You're already registered to your roblox account.")
    
    @commands.command()
    async def unregister(self, ctx):
        await ctx.send(f"Please wait...")
        user_id = str(ctx.author.id)
        guild_id = str(ctx.guild.id)
        verified_role = ctx.guild.get_role(775746108294430772)
        verified_user = await self.Bot.pg_con.fetch("SELECT * FROM verification_database WHERE user_id = $1 AND guild_id = $2", user_id, guild_id)
        if not verified_user:
            await ctx.send(f"You're not even registered!")
        else:
            await self.Bot.pg_con.execute("DELETE FROM verification_database WHERE user_id = $1 AND guild_id = $2", user_id, guild_id)
            await ctx.author.remove_roles(verified_role)
            await ctx.send(f"{ctx.author.mention} you're now unregistered!")

    @commands.command()
    @commands.has_role('Discord Moderator')
    async def f_unregister(self, ctx, member:discord.Member):
        await ctx.send(f"Looking for {member.name}#{member.discriminator}...")
        user_id = str(member.id)
        guild_id = str(ctx.guild.id)
        verified_role = ctx.guild.get_role(775746108294430772)
        verified_user = await self.Bot.pg_con.fetch("SELECT * FROM verification_database WHERE user_id = $1 AND guild_id = $2", user_id, guild_id)
        if not verified_user:
            await ctx.send(f"{member.name}#{member.discriminator} is not even registered!")
        else:
            await self.Bot.pg_con.execute("DELETE FROM verification_database WHERE user_id = $1 AND guild_id = $2", user_id, guild_id)
            await member.remove_roles(verified_role)
            await ctx.send(f"{member.mention} you've been forced to unregister!")


def setup(Bot):
    Bot.add_cog(Verification_System(Bot))