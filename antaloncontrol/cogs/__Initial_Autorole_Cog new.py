import discord
from ro_py.client import Client
from discord.ext import commands

class Auto_Roler(commands.Cog):

    def __init__(self, Bot):
        self.Bot = Bot
        self.client = Client()
    
    @commands.command()
    async def getroles(self, ctx):
        user_id = str(ctx.author.id)
        guild_id = str(ctx.guild.id)
        nsa = ctx.guild.get_role(671742940250636329)
        fp = ctx.guild.get_role(671742935758536704)
        army = ctx.guild.get_role(671742931484540952)
        mofa = ctx.guild.get_role(671743112787525658)
        marshal = ctx.guild.get_role(759882728043839539)
        moj = ctx.guild.get_role(671742944515981312)
        mod = ctx.guild.get_role(671743114817568796)
        rsa = ctx.guild.get_role(671742942016307220)
        mot = ctx.guild.get_role(775928382428545035)
        fr = ctx.guild.get_role(671742937717276682)
        moi = ctx.guild.get_role(697563213679820820)
        moh = ctx.guild.get_role(693873803767447633)
        courts = ctx.guild.get_role(776130548657553488)
        requesting_user = await self.Bot.pg_con.fetch("SELECT * FROM verification_database WHERE user_id = $1 AND guild_id = $2", user_id, guild_id)
        if not requesting_user:
            await ctx.send(f"{ctx.author.mention} please register first.")
        else:
            await ctx.send(f"Searching for you in the Republic.")
            roblox_name = requesting_user[0]['r_user']
            r_user = await self.client.get_user_by_username(roblox_name)
    
    @commands.command()
    async def developmentsub(self, ctx):
        developmentsub_role = ctx.guild.get_role(701047654796361790)

        if developmentsub_role in ctx.author.roles:
            await ctx.send(f"{ctx.author.mention} already has the development subscriber role.")
        else:
            await ctx.author.add_roles(developmentsub_role)
            await ctx.send(f"Gave you the Development Subscriber role!")

def setup(Bot):
    Bot.add_cog(Auto_Roler(Bot))