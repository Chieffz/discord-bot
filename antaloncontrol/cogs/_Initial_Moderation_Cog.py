import discord
import json
import asyncio
from discord.ext import commands

class Moderation_Commands(commands.Cog):


    def __init__(self, client):
        self.client = client

        with open('./databases/moderation_database.json', 'r') as f:
            self.users = json.load(f)

    #This whole function is made to open warning_database.json only when the bot is both ready and not closed.
    #It then takes the self.users variable and writes it to the .json file.
    #The Variable self.users may have been modified by the warn() and warnings() so we call this function to save data we may have in self.users to the .json file this is timed as well
    async def save_users(self):
        await self.client.wait_until_ready()
        while not self.client.is_closed():
            with open('./databases/moderation_database.json', 'w') as f:
                json.dump(self.users, f, indent=4)
            
            await asyncio.sleep(60)

    @commands.command()
    @commands.has_role('Discord Moderator')
    async def kick(self,ctx, member : discord.Member = None, *,reason=None):
        if member is None:
            await ctx.send(f'{ctx.author.mention} has not specified a member to kick.')
            return
        else:
            member_id = str(member.id)
            if member_id not in self.users:
                self.users[member_id] = {}
                self.users[member_id]['kicks'] = 0
                self.users[member_id]['bans'] = 0

            self.users[member_id]['kicks'] += 1

            await member.kick(reason=reason)
            channel = self.client.get_channel(770638991623061534)
            embed=discord.Embed(timestamp=ctx.message.created_at)
            embed.title="Kick"
            embed.description=f"{ctx.author} has kicked {member.name}#{member.discriminator}."
            embed.add_field(name='Appeal', value=f"Contact the {ctx.author} for appeals if he's away, contact Chief#4797", inline=False)
            embed.set_thumbnail(url=member.avatar_url)
            embed.set_footer(text="Antalon Moderation", icon_url=ctx.author.avatar_url)
            embed.color=0xff0000
            await channel.send(embed=embed)
            await ctx.send(embed=embed)
            await self.save_users()
    
    @commands.command()
    @commands.has_role('Discord Moderator')
    async def ban(self, ctx, member : discord.Member = None, *, reason=None):
        if member is None:
            await ctx.send(f'{ctx.author.mention} has not specified a member to ban.')
            return
        else:

            member_id = str(member.id)
            if member_id not in self.users:
                self.users[member_id] = {}
                self.users[member_id]['kicks'] = 0
                self.users[member_id]['bans'] = 0

            self.users[member_id]['bans'] += 1

            channel = self.client.get_channel(770638991623061534)
            embed=discord.Embed(timestamp=ctx.message.created_at)
            embed.title="Ban"
            embed.description=f"{ctx.author} has banned {member.name}#{member.discriminator}."
            embed.add_field(name='Appeal', value=f"Contact the {ctx.author} for appeals if he's away, contact Chief#4797", inline=False)
            embed.set_thumbnail(url=member.avatar_url)
            embed.set_footer(text="Antalon Moderation", icon_url=ctx.author.avatar_url)
            embed.color=0xff0000
            await channel.send(embed=embed)
            await ctx.send(embed=embed)
            await member.ban(reason=reason)
            await self.save_users()

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
            embed.add_field(name='Appeal', value=f"Contact the {ctx.author} for appeals if he's away, contact Chief#4797", inline=False)
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
            embed.add_field(name='Appeal', value=f"Contact the {ctx.author} for appeals if he's away, contact Chief#4797", inline=False)
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
            embed.add_field(name='Appeal', value=f"Contact the {ctx.author} for appeals if he's away, contact Chief#4797", inline=False)
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
            embed.add_field(name='Appeal', value=f"Contact the {ctx.author} for appeals if he's away, contact Chief#4797", inline=False)
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
        
            member_id = str(member.id)
            if member_id not in self.users:
                self.users[member_id] = {}
                self.users[member_id]['kicks'] = 0
                self.users[member_id]['bans'] = 0
            member_kicks = self.users[member_id]['kicks']
            member_bans = self.users[member_id]['kicks']
            channel = self.client.get_channel(770638991623061534)
            embed=discord.Embed(timestamp=ctx.message.created_at)
            embed.title="Mod Logs"
            embed.description=f"Moderator logs for: {member.name}#{member.discriminator}"
            embed.add_field(name='Kicks', value=f'{member_kicks}', inline=True)
            embed.add_field(name='Bans', value=f'{member_bans}', inline=True)
            embed.set_thumbnail(url=member.avatar_url)
            embed.set_footer(text="Antalon Moderation", icon_url=ctx.author.avatar_url)
            embed.color=0xff0000
            await channel.send(embed=embed)
            await ctx.send(embed=embed)
            await self.save_users()

def setup(client):
    client.add_cog(Moderation_Commands(client))