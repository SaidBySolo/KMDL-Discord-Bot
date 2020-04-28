import discord
from discord.ext import commands

class Admin(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.has_permissions(administrator=True)
    @commands.command(name='뮤트')
    async def _mute(self, ctx, user:discord.Member, *, check: str = None):
        getRole = discord.utils.get(ctx.guild.roles, name="Mute")
        if getRole is None:
            perms = discord.Permissions(send_tts_messages=False,send_messages=False, read_messages=True)
            muteRole = await ctx.guild.create_role(name="Mute", permissions=perms)
            getRole = discord.utils.get(ctx.guild.roles, name="Mute")
            for channel in ctx.guild.channels:
                await channel.set_permissions(getRole, send_messages=False, read_messages=True, read_message_history=True)
            await user.add_roles(muteRole)

        if check is None:
            getRole = discord.utils.get(ctx.guild.roles, name="Mute")
            await user.add_roles(getRole)
            embed = discord.Embed(color=0xf10e0e, title="처벌내역",description=f"디스코드 정보: {user.mention}\n\n디스코드 ID: ``{user.id}``\n\n처벌수위: ``뮤트``\n\n처벌사유: ``지정되지 않았습니다.``\n\n처리한 관리자: {ctx.author.mention}")
            await ctx.send(embed=embed)

        if check is not None:
            if check == '해제':
                getRole = discord.utils.get(ctx.guild.roles, name="Mute")
                await user.remove_roles(getRole)
                await ctx.send("\U00002705",delete_after=5)
            else:
                getRole = discord.utils.get(ctx.guild.roles, name="Mute")
                await user.add_roles(getRole)
                embed = discord.Embed(color=0xf10e0e, title="처벌내역",description=f"디스코드정보: {user.mention}\n\n디스코드 ID: ``{user.id}``\n\n처벌수위: ``뮤트``\n\n처벌사유: ``{check}``\n\n처리한 관리자: {ctx.author.mention}")
                await ctx.send(embed=embed)
        
def setup(bot):
    bot.add_cog(Admin(bot))