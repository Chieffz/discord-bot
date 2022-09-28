import discord
import asyncio
import random
from discord.ext import commands

class Warning_System(commands.Cog):

    def __init__(self, Bot):
        self.Bot = Bot

    @commands.command()
    @commands.has_role('Discord Moderator')
    async def warn(self, ctx, member : discord.Member = None, *,reason=None):
        if member is None or reason is None:
            await ctx.send(f'{ctx.author.mention} please give a valid member and/or reason.')
            return
        else:
            user_id = str(member.id)
            guild_id = str(ctx.guild.id)
            warn_reason = str(reason)
            warn_id = int(random.uniform(0,1000000))

            user = await self.Bot.pg_con.fetch("SELECT * FROM warning_database WHERE user_id = $1 AND guild_id = $2", user_id, guild_id)
            if not user:
                await self.Bot.pg_con.execute("INSERT INTO warning_database (user_id, guild_id, warns, warn_id) VALUES ($1, $2, $3, $4)", user_id, guild_id, warn_reason, warn_id)
                channel = self.Bot.get_channel(770687289948635156)
                embed=discord.Embed(timestamp=ctx.message.created_at)
                embed.title="Warning"
                embed.description=f"{ctx.author} has warned {member.name}#{member.discriminator}."
                embed.add_field(name='Appeal', value=f"Contact Moderator {ctx.author} for appeals if he's away, contact Chief#4797", inline=False)
                embed.set_thumbnail(url=member.avatar_url)
                embed.set_footer(text="Antalon Moderation", icon_url=ctx.author.avatar_url)
                embed.color=0xff0000
                await channel.send(embed=embed)
                await ctx.send(embed=embed)
            else:
                await self.Bot.pg_con.execute("INSERT INTO warning_database (user_id, guild_id, warns, warn_id) VALUES ($1, $2, $3, $4)", user_id, guild_id, warn_reason, warn_id)
                channel = self.Bot.get_channel(770687289948635156)
                embed=discord.Embed(timestamp=ctx.message.created_at)
                embed.title="Warning"
                embed.description=f"{ctx.author} has warned {member.name}#{member.discriminator}."
                embed.add_field(name='Reason', value=f"{reason}")
                embed.add_field(name='Appeal', value=f"Contact Moderator {ctx.author} for appeals if he's away, contact Chief#4797", inline=False)
                embed.set_thumbnail(url=member.avatar_url)
                embed.set_footer(text="Antalon Moderation", icon_url=ctx.author.avatar_url)
                embed.color=0xff0000
                await channel.send(embed=embed)
                await ctx.send(embed=embed)

    @commands.command()
    @commands.has_role('Discord Moderator')
    async def delwarn(self, ctx, member: discord.Member, Warn_ID=None):
        if member is None or Warn_ID is None:
            await ctx.send(f'{ctx.author.mention} has not given a valid member to remove warns from or valid warn number.')
        else:
            user_id = str(member.id)
            guild_id = str(ctx.guild.id)
            warn_id = int(Warn_ID)

            user = await self.Bot.pg_con.fetch("SELECT * FROM warning_database WHERE user_id = $1 AND guild_id = $2", user_id, guild_id)

            if not user:
                ctx.send(f'{member.name}#{member.discriminator} has no warns to remove.')
            else:
                user = await self.Bot.pg_con.fetchrow("SELECT * FROM warning_database WHERE user_id = $1 AND guild_id = $2 AND warn_id = $3", user_id, guild_id, warn_id)
                await self.Bot.pg_con.execute("DELETE FROM warning_database WHERE user_id = $1 AND guild_id = $2 AND warn_id = $3", user_id, guild_id, warn_id)
                channel = self.Bot.get_channel(770687289948635156)
                embed=discord.Embed(timestamp=ctx.message.created_at)
                embed.title="Delete Warn"
                embed.description=f"{ctx.author} has removed warning ID: {warn_id} from {member.name}#{member.discriminator}."
                embed.set_thumbnail(url=member.avatar_url)
                embed.set_footer(text="Antalon Moderation", icon_url=ctx.author.avatar_url)
                embed.color=0xff0000
                await channel.send(embed=embed)
                await ctx.send(embed=embed)

    @commands.command()
    @commands.has_role('Discord Moderator')
    async def warnings(self, ctx, member : discord.Member = None):
        if member is None:
            await ctx.send(f'{ctx.author.mention} has not specified a member to view warnings of.')
        else:
            user_id = str(member.id)
            guild_id = str(ctx.guild.id)

            user = await self.Bot.pg_con.fetch("SELECT * FROM warning_database WHERE user_id = $1 AND guild_id = $2", user_id, guild_id)
            if not user:
                await ctx.send(f"{member.name}#{member.discriminator} has no warnings to view.")
            else:
                current_warns = await self.Bot.pg_con.fetch("SELECT warns, warn_id FROM warning_database WHERE user_id = $1 AND guild_id = $2", user_id, guild_id)
                channel = self.Bot.get_channel(770687289948635156)
                embed=discord.Embed(timestamp=ctx.message.created_at)
                embed.title="Current Warns"
                embed.description=f"{member.name}#{member.discriminator}"
                for x in current_warns:
                        embed.add_field(name=f"Warning ID:{x['warn_id']}", value=f"{x['warns']}", inline=False)
                embed.set_thumbnail(url=member.avatar_url)
                embed.set_footer(text="Antalon Moderation", icon_url=ctx.author.avatar_url)
                embed.color=0xff0000
                await channel.send(embed=embed)
                await ctx.send(embed=embed)

def setup(Bot):
    Bot.add_cog(Warning_System(Bot))