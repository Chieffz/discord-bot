import discord
import json
import asyncio
from discord.ext import commands

class Warning_System(commands.Cog):

    def __init__(self, client):
        self.client = client

        #Loads all the data in the file warning_database.json and loads it into the variable self.users
        with open('./databases/warning_database.json', 'r') as f:
            self.users = json.load(f)
        
        
    #This whole function is made to open warning_database.json only when the bot is both ready and not closed.
    #It then takes the self.users variable and writes it to the .json file.
    #The Variable self.users may have been modified by the warn() and warnings() so we call this function to save data we may have in self.users to the .json file this is timed as well
    async def save_users(self):
        await self.client.wait_until_ready()
        while not self.client.is_closed():
            with open('./databases/warning_database.json', 'w') as f:
                json.dump(self.users, f, indent=4)
            
            await asyncio.sleep(60)

    @commands.command()
    @commands.has_role('Discord Moderator')
    async def warn(self, ctx, member : discord.Member = None):
        if member is None:
            await ctx.send(f'{ctx.author.mention} please mention a valid member.')
            return
        else:
            member_id = str(member.id)

            #self.users is all the file contents in warning_database.json and checks to make sure the current member being warned is in self.users
            if member_id not in self.users:
                self.users[member_id] = {}
                self.users[member_id]['warn'] = 0
                self.users[member_id]['max_warns'] = 0

            if self.users[member_id]['warn'] == 3:

                self.users[member_id]['max_warns'] = 1
                channel = self.client.get_channel(770638991623061534)
                embed=discord.Embed(timestamp=ctx.message.created_at)
                embed.title="Warn Limit Reached"
                embed.description=f'{member.name}#{member.discriminator} has reached the max amount of warns!'
                embed.set_thumbnail(url=member.avatar_url)
                embed.set_footer(text="Antalon Moderation", icon_url=ctx.author.avatar_url)
                embed.color=0xff0000
                await channel.send(embed=embed)
                await ctx.send(embed=embed)
                await self.save_users()
            else:
                #Adds on 1 to the member's warn value
                self.users[member_id]['warn'] += 1
            #Sends a discord embed to both log channel and the channel the command was called also calls the function save_uvers() which basically just loops through warning_database.json
            channel = self.client.get_channel(770638991623061534)
            embed=discord.Embed(timestamp=ctx.message.created_at)
            embed.title="Warning"
            embed.description=f"{ctx.author} has warned {member.name}#{member.discriminator}."
            embed.add_field(name='Appeal', value=f"Contact the {ctx.author} for appeals if he's away, contact Chief#4797", inline=False)
            embed.set_thumbnail(url=member.avatar_url)
            embed.set_footer(text="Antalon Moderation", icon_url=ctx.author.avatar_url)
            embed.color=0xff0000
            await channel.send(embed=embed)
            await ctx.send(embed=embed)
            await self.save_users()

    @commands.command()
    @commands.has_role('Discord Moderator')
    async def warnings(self, ctx, member : discord.Member = None):
        if member is None:
            await ctx.send(f'{ctx.author.mention} has not specified a member to view warnings of.')
        else:
            member_id = str(member.id)
            if member_id not in self.users:
                self.users[member_id] = {}
                self.users[member_id]['warn'] = 0
                self.users[member_id]['max_warns'] = 0
            
            member_warnings = self.users[member_id]['warn']
            member_max_warnings = self.users[member_id]['max_warns']

            channel = self.client.get_channel(770638991623061534)
            embed=discord.Embed(timestamp=ctx.message.created_at)
            embed.title="Current Warns"
            embed.description=f"{member.name}#{member.discriminator} has {member_warnings} warning(s)."
            embed.add_field(name='Max Warning Limit Reached?', value=f'{member_max_warnings}')
            embed.add_field(name='Appeal', value=f"Contact the {ctx.author} for appeals if he's away, contact Chief#4797", inline=False)
            embed.set_thumbnail(url=member.avatar_url)
            embed.set_footer(text="Antalon Moderation", icon_url=ctx.author.avatar_url)
            embed.color=0xff0000
            await channel.send(embed=embed)
            await ctx.send(embed=embed)
            await self.save_users()

def setup(client):
    client.add_cog(Warning_System(client))