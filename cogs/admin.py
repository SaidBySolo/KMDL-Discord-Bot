import discord
import asyncio
from discord.ext import commands


class Admin(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.has_permissions(administrator=True)
    @commands.command(name='뮤트')
    async def _mute(self, ctx, user: discord.Member, day=None, hour=None, minute=None, *, check: str = None):
        timelist = [day,hour,minute]

        timeday = timelist[0]
        timehour = timelist[1]
        timeminute = timelist[2]

        getRole = discord.utils.get(ctx.guild.roles, name="Mute")
        if getRole is None:
            muteRole = await ctx.guild.create_role(name="Mute")
            getRole = discord.utils.get(ctx.guild.roles, name="Mute")
            for channel in ctx.guild.channels:
                await channel.set_permissions(getRole, send_messages=False, read_messages=True, read_message_history=True)

        if timeday is not None and timehour is not None and timeminute is not None:
            resulttime = (int(timeday) * 86400)+(int(timehour) * 3600)+(int(timeminute) * 60)
            if resulttime == 0:
                getRole = discord.utils.get(ctx.guild.roles, name="Mute")
                await user.add_roles(getRole)
                embed = discord.Embed(color=0xf10e0e, title="처벌내역",description=f"디스코드 정보: {user.mention}\n\n디스코드 ID: ``{user.id}``\n\n처벌수위: ``뮤트/영구``\n\n처벌사유: ``{check}``\n\n처리한 관리자: {ctx.author.mention}")
                await ctx.send(embed=embed)
            else:
                getRole = discord.utils.get(ctx.guild.roles, name="Mute")
                await user.add_roles(getRole)
                embed = discord.Embed(color=0xf10e0e, title="처벌내역",description=f"디스코드 정보: {user.mention}\n\n디스코드 ID: ``{user.id}``\n\n처벌수위: ``뮤트/{round(resulttime/60)}분``\n\n처벌사유: ``{check}``\n\n처리한 관리자: {ctx.author.mention}")
                await ctx.send(embed=embed)
                await asyncio.sleep(resulttime)
                await user.remove_roles(getRole)
        elif timeday == '해제':
            getRole = discord.utils.get(ctx.guild.roles, name="Mute")
            await user.remove_roles(getRole)
            await ctx.send("\U00002705",delete_after=5)


def setup(bot):
    bot.add_cog(Admin(bot))
