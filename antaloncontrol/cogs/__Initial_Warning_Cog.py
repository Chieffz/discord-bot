import discord
import asyncio
from discord.ext import commands

class Warning_System(commands.Cog):

    def __init__(self, client):
        self.client = client

    async def warn_limit(self, user):
        cur_warns = user['warns']
        cur_max_warns = user['max_warns']

        if cur_warns == 3:
            await self.client.pg_con.execute("UPDATE warning_database SET max_warns = $1 WHERE user_id = $2 AND guild_id = $3", cur_max_warns + 1, user['user_id'], user['guild.id'])
            return True
        else:
            return False

    @commands.command()
    @commands.has_role('Discord Moderator')
    async def warn(self, ctx, member : discord.Member = None):
        if member is None:
            await ctx.send(f'{ctx.author.mention} please mention a valid member.')
            return
        else:
            user_id = str(member.id)
            guild_id = str(ctx.guild.id)

            user = await self.client.pg_con.fetch("SELECT * FROM warning_database WHERE user_id = $1 AND guild_id = $2", user_id, guild_id)
            
            if not user:
                await self.client.pg_con.execute("INSERT INTO warning_database (user_id, guild_id, warns, max_warns) VALUES ($1, $2, 0, 0)", user_id, guild_id)

            user = await self.client.pg_con.fetchrow("SELECT * FROM warning_database WHERE user_id = $1 AND guild_id = $2", user_id, guild_id)
            await self.client.pg_con.execute("UPDATE warning_database SET warns = $1 WHERE user_id = $2 AND guild_id = $3", user['warns'] + 1, user_id, guild_id)

            if await self.warn_limit(user):
                await ctx.send(f'{member.name}#{member.discriminator} has reached the max warn limit by having 3 warns.')

            channel = self.client.get_channel(770638991623061534)
            embed=discord.Embed(timestamp=ctx.message.created_at)
            embed.title="Warning"
            embed.description=f"{ctx.author} has warned {member.name}#{member.discriminator}."
            embed.add_field(name='Appeal', value=f"Contact Moderator {ctx.author} for appeals if he's away, contact Chief#4797", inline=False)
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

            user = await self.client.pg_con.fetch("SELECT * FROM warning_database WHERE user_id = $1 AND guild_id = $2", user_id, guild_id)
            if not user:
                user = await self.client.pg_con.execute("INSERT INTO warning_database (user_id, guild_id, warns, max_warns) VALUES ($1, $2, 0, 0)", user_id, guild_id)

            channel = self.client.get_channel(770638991623061534)
            embed=discord.Embed(timestamp=ctx.message.created_at)
            embed.title="Current Warns"
            embed.description=f"{member.name}#{member.discriminator} has {user[0]['warns']} warning(s)."
            embed.add_field(name='Max Warning Limit Reached?', value=user[0]['max_warns'])
            embed.add_field(name='Appeal', value=f"Contact Moderator {ctx.author} for appeals if he's away, contact Chief#4797", inline=False)
            embed.set_thumbnail(url=member.avatar_url)
            embed.set_footer(text="Antalon Moderation (0 = False, 1 = True)", icon_url=ctx.author.avatar_url)
            embed.color=0xff0000
            await channel.send(embed=embed)
            await ctx.send(embed=embed)

def setup(client):
    client.add_cog(Warning_System(client))