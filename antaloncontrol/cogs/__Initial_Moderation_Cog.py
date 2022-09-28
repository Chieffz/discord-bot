import discord
import json
import asyncio
from discord.ext import commands

class Moderation_Commands(commands.Cog):


    def __init__(self, client):
        self.client = client

        with open('./databases/moderation_database.json', 'r') as f:
            self.users = json.load(f)

    @commands.command()
    @commands.has_role('Discord Moderator')
    async def kick(self,ctx, member : discord.Member = None, *,reason=None):
        if member is None:
            await ctx.send(f'{ctx.author.mention} has not specified a member to kick.')
            return
        else:
            user_id = str(member.id)
            guild_id = str(ctx.guild.id)

            user = await self.client.pg_con.fetch("SELECT * FROM moderation_database WHERE user_id = $1 AND guild_id = $2", user_id, guild_id)

            if not user:
                self.client.pg_con.execute("INSERT INTO moderation_database (user_id, guild_id, kicks, bans) VALUES ($1, $2, 0, 0)", user_id, guild_id)
                channel = self.client.get_channel(770638991623061534)
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
                user = await self.client.pg_con.fetchrow("SELECT * FROM moderation_database WHERE user_id = $1 AND guild_id = $2", user_id, guild_id)
                await self.client.pg_con.execute("UPDATE moderation_database SET kicks = $1 WHERE user_id = $2 AND guild_id = $3", user['kicks'] + 1, user_id, guild_id)

                channel = self.client.get_channel(770638991623061534)
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
        if member is None:
            await ctx.send(f'{ctx.author.mention} has not specified a member to ban.')
            return
        else:
            user_id = str(member.id)
            guild_id = str(ctx.guild.id)

            user = await self.client.pg_con.fetch("SELECT * FROM moderation_database WHERE user_id = $1 AND guild_id = $2", user_id, guild_id)

            if not user:
                self.client.pg_con.execute("INSERT INTO moderation_database (user_id, guild_id, kicks, bans) VALUES ($1, $2, 0, 0)", user_id, guild_id)
                channel = self.client.get_channel(770638991623061534)
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
                user = await self.client.pg_con.fetchrow("SELECT * FROM moderation_database WHERE user_id = $1 AND guild_id = $2", user_id, guild_id)
                await self.client.pg_con.execute("UPDATE moderation_database SET bans = $1 WHERE user_id = $2 AND guild_id = $3", user['bans'] + 1, user_id, guild_id)
                channel = self.client.get_channel(770638991623061534)
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
            channel = self.client.get_channel(770638991623061534)
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
            channel = self.client.get_channel(770638991623061534)
            embed=discord.Embed(timestamp=ctx.message.created_at)
            embed.title="Voice Unmute"
            embed.description=f"{ctx.author} has voice unmuted {member.name}#{member.discriminator}."
            embed.add_field(name='Appeal', value=f"Contact Moderator {ctx.author} for appeals if he's away, contact Chief#4797", inline=False)
            embed.set_thumbnail(url=member.avatar_url)
            embed.set_footer(text="Antalon Moderation", icon_url=ctx.author.avatar_url)
            embed.color=0xff0000
            await channel.send(embed=embed)
            await ctx.send(embed=embed)

    @commands.command()
    @commands.has_role('Discord Moderator')
    async def mute(self, ctx, member : discord.Member = None, *, reason=None):
        muted_role = ctx.guild.get_role(770608074963812363)
        if member is None:
            await ctx.send(f'{ctx.author.mention} has not specified a member to mute.')
            return
        else:
            await member.add_roles(muted_role)
            channel = self.client.get_channel(770638991623061534)
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
        muted_role = ctx.guild.get_role(770608074963812363)
        if member is None:
            await ctx.send(f'{ctx.author.mention} has not specified a member to unmute.')
            return
        else:
            await member.remove_roles(muted_role)
            channel = self.client.get_channel(770638991623061534)
            embed=discord.Embed(timestamp=ctx.message.created_at)
            embed.title="Unmute"
            embed.description=f"{ctx.author} has unmuted {member.name}#{member.discriminator}."
            embed.add_field(name='Appeal', value=f"Contact Moderator {ctx.author} for appeals if he's away, contact Chief#4797", inline=False)
            embed.set_thumbnail(url=member.avatar_url)
            embed.set_footer(text="Antalon Moderation", icon_url=ctx.author.avatar_url)
            embed.color=0xff0000
            await channel.send(embed=embed)
            await ctx.send(embed=embed)

    @commands.command()
    @commands.has_role('Discord Moderator')
    async def clear(self, ctx, amount=10):
        await ctx.channel.purge(limit=amount+1)
        channel = self.client.get_channel(770638991623061534)
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

                channel = self.client.get_channel(770638991623061534)
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
    async def mod_logs(self, ctx, member:discord.Member=None):
        if member is None:
            await ctx.send(f'{ctx.author.mention} has not specified a member to unban.')
        else:
        
            user_id = str(member.id)
            guild_id = str(ctx.guild.id)
            user = await self.client.pg_con.fetch("SELECT * FROM moderation_database WHERE user_id = $1 AND guild_id = $2", user_id, guild_id)
            if not user:
                user = await self.client.pg_con.execute("INSERT INTO moderation_database (user_id, guild_id, kicks, bans) VALUES ($1, $2, 0, 0)", user_id, guild_id)
                channel = self.client.get_channel(770638991623061534)
                embed=discord.Embed(timestamp=ctx.message.created_at)
                embed.title="Mod Logs"
                embed.description=f"Moderator logs for: {member.name}#{member.discriminator}"
                embed.add_field(name='Kicks', value=f"{user[0]['kicks']}", inline=True)
                embed.add_field(name='Bans', value=f"{user[0]['bans']}", inline=True)
                embed.set_thumbnail(url=member.avatar_url)
                embed.set_footer(text="Antalon Moderation", icon_url=ctx.author.avatar_url)
                embed.color=0xff0000
                await channel.send(embed=embed)
                await ctx.send(embed=embed)
            else:
            
                channel = self.client.get_channel(770638991623061534)
                embed=discord.Embed(timestamp=ctx.message.created_at)
                embed.title="Mod Logs"
                embed.description=f"Moderator logs for: {member.name}#{member.discriminator}"
                embed.add_field(name='Kicks', value=f"{user[0]['kicks']}", inline=True)
                embed.add_field(name='Bans', value=f"{user[0]['bans']}", inline=True)
                embed.set_thumbnail(url=member.avatar_url)
                embed.set_footer(text="Antalon Moderation", icon_url=ctx.author.avatar_url)
                embed.color=0xff0000
                await channel.send(embed=embed)
                await ctx.send(embed=embed)

def setup(client):
    client.add_cog(Moderation_Commands(client))