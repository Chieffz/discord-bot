import discord
import asyncio
import random
from ro_py.client import Client
from discord.ext import commands

class Verification_System(commands.Cog):

    def __init__(self, Bot):
        self.Bot = Bot
        self.client = Client()

    @commands.command()
    async def register(self, ctx, *, roblox_name=None):
        if roblox_name is None:
            await ctx.send(f"{ctx.author.mention} failed to provide a roblox username!")
        else:
            await ctx.send(f"Checking to see if you're verified...")
            user_id = str(ctx.author.id)
            guild_id = str(ctx.guild.id)
            verified_user = await self.Bot.pg_con.fetch("SELECT * FROM verification_database WHERE user_id = $1 AND guild_id = $2", user_id, guild_id)

            if not verified_user:
                verified_role = ctx.guild.get_role(775746108294430772)
                roblox_user = str(roblox_name)
                word_list = ['boat', 'sea', 'sail', 'ride', 'fair', 'pay', 'play', 'mail', 'share', 'wait']
                selected_word = random.choice(word_list)
                await ctx.send(f"Please put this string of characters in your roblox user's blurb or about section *{str(selected_word)}*. You have 30 seconds; Please make sure that only the string of numbers is in your blurb and nothing else!")
                await asyncio.sleep(30)
                r_user = await self.client.get_user_by_username(roblox_user)
                r_blurb = r_user.description
                if (r_blurb) == selected_word:
                    await self.Bot.pg_con.execute("INSERT INTO verification_database (user_id, guild_id, r_user) VALUES ($1, $2, $3)", user_id, guild_id, roblox_user)
                    await ctx.send(f"{ctx.author.mention} You're now registered!")
                    await ctx.author.add_roles(verified_role)
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