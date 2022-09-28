import discord
import asyncio
import robloxapi
from discord.ext import commands

class Promote_System(commands.Cog):

    def __init__(self, Bot):
        self.Bot = Bot
        self.client = robloxapi.Client(cookie="")

    @commands.command()
    @commands.has_role('Discord Moderator')
    async def promote(self, ctx, d_member:discord.Member, *, roblox_group=None):
        if roblox_group is None or d_member is None:
            await ctx.send(f"{ctx.author.mention} please provide a valid group or member.")
        else:
            if roblox_group == 5324371:
                await ctx.send(f"You cannot promote people in the Republic!")
            else:
                guild_id = str(ctx.guild.id)
                user_id = str(d_member.id)
                author_user_id = str(ctx.author.id)
                author_r_user = await self.Bot.pg_con.fetch("SELECT * FROM verification_database WHERE user_id = $1 AND guild_id = $2", author_user_id, guild_id)
                r_user = await self.Bot.pg_con.fetch("SELECT * FROM verification_database WHERE user_id = $1 AND guild_id = $2", user_id, guild_id)
                author_r_user_name = author_r_user[0]['r_user']
                r_user_name = r_user[0]['r_user']
                if not r_user:
                    await ctx.send(f"{ctx.author.mention} user is not registered.")
                else:
                    r_user_id = await self.client.get_user_by_username(roblox_name=r_user_name)

                    targetted_group = await self.client.get_group(int(roblox_group))
                    async for member in targetted_group.get_members():
                        if r_user_name == member.name:
                            if  author_r_user_name == member.name:
                                await targetted_group.change_rank(r_user_id, 5)
                                break
                            else:
                                await ctx.send(f"{ctx.author.mention} is not apart of that group.")
                                break
                        else:
                            await ctx.send(f"{ctx.author.mention} Failed to promote {d_member.name}#{d_member.discriminator}.")
                            break

def setup(Bot):
    Bot.add_cog(Promote_System(Bot))