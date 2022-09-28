import discord
import asyncio
import random
from discord.ext import commands

class Moderation_Commands(commands.Cog):


    def __init__(self, Bot):
        self.Bot = Bot

    @commands.command()
    @commands.has_role('Discord Moderator')
    async def kick(self,ctx, member : discord.Member = None, *,reason=None):
        if member is None or reason is None:
            await ctx.send(f'{ctx.author.mention} has not given a valid member to kick or a valid reason.')
            return
        else:
            user_id = str(member.id)
            guild_id = str(ctx.guild.id)
            kick_reason = str(reason)
            kick_id = int(random.uniform(0,1000000))

            user = await self.Bot.pg_con.fetch("SELECT * FROM moderation_database WHERE user_id = $1 AND guild_id = $2", user_id, guild_id)
            if not user:
                await self.Bot.pg_con.execute("INSERT INTO moderation_database (user_id, guild_id, kicks, kick_id) VALUES ($1, $2, $3, $4)", user_id, guild_id, kick_reason, kick_id)

                channel = self.Bot.get_channel(770687289948635156)
                embed=discord.Embed(timestamp=ctx.message.created_at)
                embed.title="Kick"
                embed.description=f"{ctx.author} has kicked {member.name}#{member.discriminator}."
                embed.add_field(name='Appeal', value=f"Contact Moderator {ctx.author} for appeals if he's away, contact Chief#4797", inline=False)
                embed.set_thumbnail(url=member.avatar_url)
                embed.set_footer(text="Antalon Moderation", icon_url=ctx.author.avatar_url)
                embed.color=0xff0000
                await channel.send(embed=embed)
                await ctx.send(embed=embed)
                await member.kick(reason=reason)
            else:
                await self.Bot.pg_con.execute("INSERT INTO moderation_database (user_id, guild_id, kicks, kick_id) VALUES ($1, $2, $3, $4)", user_id, guild_id, kick_reason, kick_id)

                channel = self.Bot.get_channel(770687289948635156)
                embed=discord.Embed(timestamp=ctx.message.created_at)
                embed.title="Kick"
                embed.description=f"{ctx.author} has kicked {member.name}#{member.discriminator}."
                embed.add_field(name='Appeal', value=f"Contact Moderator {ctx.author} for appeals if he's away, contact Chief#4797", inline=False)
                embed.set_thumbnail(url=member.avatar_url)
                embed.set_footer(text="Antalon Moderation", icon_url=ctx.author.avatar_url)
                embed.color=0xff0000
                await channel.send(embed=embed)
                await ctx.send(embed=embed)
                await member.kick(reason=reason)
    
    @commands.command()
    @commands.has_role('Discord Moderator')
    async def ban(self, ctx, member : discord.Member = None, *, reason=None):
        if member is None or reason is None:
            await ctx.send(f'{ctx.author.mention} has not given a valid member to ban or a valid reason.')
            return
        else:
            user_id = str(member.id)
            guild_id = str(ctx.guild.id)
            ban_reason = str(reason)
            ban_id = int(random.uniform(0,1000000))

            user = await self.Bot.pg_con.fetch("SELECT * FROM moderation_database WHERE user_id = $1 AND guild_id = $2", user_id, guild_id)
            if not user:
                await self.Bot.pg_con.execute("INSERT INTO moderation_database (user_id, guild_id, bans, ban_id) VALUES ($1, $2, $3, $4)", user_id, guild_id, ban_reason, ban_id)
                channel = self.Bot.get_channel(770687289948635156)
                embed=discord.Embed(timestamp=ctx.message.created_at)
                embed.title="Ban"
                embed.description=f"{ctx.author} has banned {member.name}#{member.discriminator}."
                embed.add_field(name='Appeal', value=f"Contact Moderator {ctx.author} for appeals if he's away, contact Chief#4797", inline=False)
                embed.set_thumbnail(url=member.avatar_url)
                embed.set_footer(text="Antalon Moderation", icon_url=ctx.author.avatar_url)
                embed.color=0xff0000
                await channel.send(embed=embed)
                await ctx.send(embed=embed)
                await member.ban(reason=reason)
            else:
                await self.Bot.pg_con.execute("INSERT INTO moderation_database (user_id, guild_id, bans, ban_id) VALUES ($1, $2, $3, $4)", user_id, guild_id, ban_reason, ban_id)
                channel = self.Bot.get_channel(770687289948635156)
                embed=discord.Embed(timestamp=ctx.message.created_at)
                embed.title="Ban"
                embed.description=f"{ctx.author} has banned {member.name}#{member.discriminator}."
                embed.add_field(name='Appeal', value=f"Contact Moderator {ctx.author} for appeals if he's away, contact Chief#4797", inline=False)
                embed.set_thumbnail(url=member.avatar_url)
                embed.set_footer(text="Antalon Moderation", icon_url=ctx.author.avatar_url)
                embed.color=0xff0000
                await channel.send(embed=embed)
                await ctx.send(embed=embed)
                await member.ban(reason=reason)

    @commands.command()
    @commands.has_role('Discord Moderator')
    async def v_mute(self, ctx, member : discord.Member = None, *, reason=None):
        if member is None:
            await ctx.send(f'{ctx.author.mention} has not specified a member to voice mute.')
            return
        else:
            await member.edit(mute=True)
            channel = self.Bot.get_channel(770687289948635156)
            embed=discord.Embed(timestamp=ctx.message.created_at)
            embed.title="Voice Mute"
            embed.description=f"{ctx.author} has voice muted {member.name}#{member.discriminator}."
            embed.add_field(name='Appeal', value=f"Contact Moderator {ctx.author} for appeals if he's away, contact Chief#4797", inline=False)
            embed.set_thumbnail(url=member.avatar_url)
            embed.set_footer(text="Antalon Moderation", icon_url=ctx.author.avatar_url)
            embed.color=0xff0000
            await channel.send(embed=embed)
            await ctx.send(embed=embed)

    @commands.command()
    @commands.has_role('Discord Moderator')
    async def v_unmute(self, ctx, member : discord.Member = None, *, reason=None):
        if member is None:
            await ctx.send(f'{ctx.author.mention} has not specified a member to unvoice mute.')
            return
        else:
            await member.edit(mute=False)
            channel = self.Bot.get_channel(770687289948635156)
            embed=discord.Embed(timestamp=ctx.message.created_at)
            embed.title="Voice Unmute"
            embed.description=f"{ctx.author} has voice unmuted {member.name}#{member.discriminator}."
            embed.set_thumbnail(url=member.avatar_url)
            embed.set_footer(text="Antalon Moderation", icon_url=ctx.author.avatar_url)
            embed.color=0xff0000
            await channel.send(embed=embed)
            await ctx.send(embed=embed)

    @commands.command()
    @commands.has_role('Discord Moderator')
    async def mute(self, ctx, member : discord.Member = None, *, reason=None):
        muted_role = ctx.guild.get_role(679094535770603521)
        if member is None:
            await ctx.send(f'{ctx.author.mention} has not specified a member to mute.')
            return
        else:
            await member.add_roles(muted_role)
            channel = self.Bot.get_channel(770687289948635156)
            embed=discord.Embed(timestamp=ctx.message.created_at)
            embed.title="Mute"
            embed.description=f"{ctx.author} has muted {member.name}#{member.discriminator}."
            embed.add_field(name='Appeal', value=f"Contact Moderator {ctx.author} for appeals if he's away, contact Chief#4797", inline=False)
            embed.set_thumbnail(url=member.avatar_url)
            embed.set_footer(text="Antalon Moderation", icon_url=ctx.author.avatar_url)
            embed.color=0xff0000
            await channel.send(embed=embed)
            await ctx.send(embed=embed)


    @commands.command()
    @commands.has_role('Discord Moderator')
    async def unmute(self, ctx, member : discord.Member = None, *, reason=None):
        muted_role = ctx.guild.get_role(679094535770603521)
        if member is None:
            await ctx.send(f'{ctx.author.mention} has not specified a member to unmute.')
            return
        else:
            await member.remove_roles(muted_role)
            channel = self.Bot.get_channel(770687289948635156)
            embed=discord.Embed(timestamp=ctx.message.created_at)
            embed.title="Unmute"
            embed.description=f"{ctx.author} has unmuted {member.name}#{member.discriminator}."
            embed.set_thumbnail(url=member.avatar_url)
            embed.set_footer(text="Antalon Moderation", icon_url=ctx.author.avatar_url)
            embed.color=0xff0000
            await channel.send(embed=embed)
            await ctx.send(embed=embed)

    @commands.command()
    @commands.has_role('Discord Moderator')
    async def clear(self, ctx, amount=10):
        await ctx.channel.purge(limit=amount+1)
        channel = self.Bot.get_channel(770687289948635156)
        embed=discord.Embed(timestamp=ctx.message.created_at)
        embed.title="Clear"
        embed.description=f"{ctx.author} has cleared {amount} message(s)."
        embed.set_thumbnail(url=ctx.author.avatar_url)
        embed.set_footer(text="Antalon Moderation", icon_url=ctx.author.avatar_url)
        embed.color=0xff0000
        await channel.send(embed=embed)
        await ctx.send(embed=embed)

    @commands.command()
    @commands.has_role('Discord Moderator')
    async def unban(self, ctx, *, member = None):
        if member is None:
            await ctx.send(f'{ctx.author.mention} has not specified a member to unban.')
            return

        else:
            banned_users = await ctx.guild.bans()
            member_name, member_discriminator = member.split('#')

            for ban_entry in banned_users:
                user = ban_entry.user

            if (user.name, user.discriminator) == (member_name, member_discriminator):
                await ctx.guild.unban(user)

                channel = self.Bot.get_channel(770687289948635156)
                embed=discord.Embed(timestamp=ctx.message.created_at)
                embed.title="Member Unbanned"
                embed.description=f"{user.name}#{user.discriminator} was unbanned."
                embed.set_thumbnail(url=ctx.author.avatar_url)
                embed.set_footer(text="Antalon Moderation", icon_url=ctx.author.avatar_url)
                embed.color=0xff0000
                await channel.send(embed=embed)
                await ctx.send(embed=embed)
    
    @commands.command()
    @commands.has_role('Discord Moderator')
    async def modlogs(self, ctx, member:discord.Member=None):
        if member is None:
            await ctx.send(f'{ctx.author.mention} has not specified a member to view mod_logs of.')
        else:
        
            user_id = str(member.id)
            guild_id = str(ctx.guild.id)

            user = await self.Bot.pg_con.fetch("SELECT * FROM moderation_database WHERE user_id = $1 AND guild_id = $2", user_id, guild_id)
            if not user:
                await ctx.send(f"{member.name}#{member.discriminator} has no moderation history to view.")
            else:
                current_kicks = await self.Bot.pg_con.fetch("SELECT kicks, kick_id FROM moderation_database WHERE user_id = $1 AND guild_id = $2", user_id, guild_id)
                current_bans = await self.Bot.pg_con.fetch("SELECT bans, ban_id FROM moderation_database WHERE user_id = $1 AND guild_id = $2", user_id, guild_id)
                channel = self.Bot.get_channel(770687289948635156)
                embed=discord.Embed(timestamp=ctx.message.created_at)
                embed.title="Mod Logs"
                embed.description=f"Moderator logs for: {member.name}#{member.discriminator}"
                for x in current_bans:
                        embed.add_field(name=f"Ban Moderation ID:{x['ban_id']}", value=f"{x['bans']}", inline=False)
                for x in current_kicks:
                        embed.add_field(name=f"Kick Moderation ID:{x['kick_id']}", value=f"{x['kicks']}", inline=False)
                embed.set_thumbnail(url=member.avatar_url)
                embed.set_footer(text="Antalon Moderation", icon_url=ctx.author.avatar_url)
                embed.color=0xff0000
                await channel.send(embed=embed)
                await ctx.send(embed=embed)

def setup(Bot):
    Bot.add_cog(Moderation_Commands(Bot))