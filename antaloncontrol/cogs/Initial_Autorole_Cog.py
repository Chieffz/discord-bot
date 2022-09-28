import discord
import robloxapi
from discord.ext import commands

class Auto_Roler(commands.Cog):

    def __init__(self, Bot):
        self.Bot = Bot
        self.client = robloxapi.Client(cookie="")
    
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
            r_user = requesting_user[0]['r_user']
            state_marshal_group = await self.client.get_group(7336134)
            async for member in state_marshal_group.get_members():
                if r_user == member.name:
                    if marshal in ctx.author.roles:
                        break
                    else:
                        await ctx.author.add_roles(marshal)
                        await ctx.send(f"Added State Marshal Role to {ctx.author.mention}.")
                        break
            foreign_affairs_group = await self.client.get_group(5351885)
            async for member in foreign_affairs_group.get_members():
                if r_user == member.name:
                    if mofa in ctx.author.roles:
                        break
                    else:
                        await ctx.author.add_roles(mofa)
                        await ctx.send(f"Added MOFA Role to {ctx.author.mention}.")
                        break
            national_army_group = await self.client.get_group(5351873)
            async for member in national_army_group.get_members():
                if r_user == member.name:
                    if army in ctx.author.roles:
                        break
                    else:
                        await ctx.author.add_roles(army)
                        await ctx.send(f"Added National Army Role to {ctx.author.mention}.")
                        break
            national_security_group = await self.client.get_group(5324431)
            async for member in national_security_group.get_members():
                if r_user == member.name:
                    if nsa in ctx.author.roles:
                        break
                    else:
                        await ctx.author.add_roles(nsa)
                        await ctx.send(f"Added National Security Role to {ctx.author.mention}.")
                        break
            federal_police_group = await self.client.get_group(5324393)
            async for member in federal_police_group.get_members():
                if r_user == member.name:
                    if fp in ctx.author.roles:
                        break
                    else:
                        await ctx.author.add_roles(fp)
                        await ctx.send(f"Added Federal Police Role to {ctx.author.mention}.")
                        break
            justice_group = await self.client.get_group(5447461)
            async for member in justice_group.get_members():
                if r_user == member.name:
                    if moj in ctx.author.roles:
                        break
                    else:
                        await ctx.author.add_roles(moj)
                        await ctx.send(f"Added Justice Ministry Role to {ctx.author.mention}.")
                        break
            defense_group = await self.client.get_group(5351894)
            async for member in defense_group.get_members():
                if r_user == member.name:
                    if mod in ctx.author.roles:
                        break
                    else:
                        await ctx.author.add_roles(mod)
                        await ctx.send(f"Added Defense Ministry Role to {ctx.author.mention}.")
                        break
            roadside_assist_group = await self.client.get_group(5534806)
            async for member in roadside_assist_group.get_members():
                if r_user == member.name:
                    if rsa in ctx.author.roles:
                        break
                    else:
                        await ctx.author.add_roles(rsa)
                        await ctx.send(f"Added RSA Role to {ctx.author.mention}.")
                        break
            trade_group = await self.client.get_group(5535175)
            async for member in trade_group.get_members():
                if r_user == member.name:
                    if mot in ctx.author.roles:
                        break
                    else:
                        await ctx.author.add_roles(mot)
                        await ctx.send(f"Added Trade Ministry Role to {ctx.author.mention}.")
                        break
            fire_rescue_group = await self.client.get_group(5574529)
            async for member in fire_rescue_group.get_members():
                if r_user == member.name:
                    if fr in ctx.author.roles:
                        break
                    else:
                        await ctx.author.add_roles(fr)
                        await ctx.send(f"Added Fire & Rescue Role to {ctx.author.mention}.")
                        break
            information_group = await self.client.get_group(5778723)
            async for member in information_group.get_members():
                if r_user == member.name:
                    if moi in ctx.author.roles:
                        break
                    else:
                        await ctx.author.add_roles(moi)
                        await ctx.send(f"Added Information Ministry Role to {ctx.author.mention}.")
                        break
            health_group = await self.client.get_group(5827427)
            async for member in health_group.get_members():
                if r_user == member.name:
                    if moh in ctx.author.roles:
                        break
                    else:
                        await ctx.author.add_roles(moh)
                        await ctx.send(f"Added Health Ministry Role to {ctx.author.mention}.")
                        break
            national_courts = await self.client.get_group(5535197)
            async for member in national_courts.get_members():
                if r_user == member.name:
                    if courts in ctx.author.roles:
                        break
                    else:
                        await ctx.author.add_roles(courts)
                        await ctx.send(f"Added Judiciary Staff Role to {ctx.author.mention}.")
                        break
    
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