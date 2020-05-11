import discord
import asyncio
from discord.ext import commands
import datetime

n = datetime.datetime.now()
now = f'{n.year}. {n.month}. {n.day}.'


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
                await channel.set_permissions(getRole, send_messages=False,add_reactions=False)

        if timeday is not None and timehour is not None and timeminute is not None:
            resulttime = (int(timeday) * 86400)+(int(timehour) * 3600)+(int(timeminute) * 60)
            if resulttime == 0:
                getRole = discord.utils.get(ctx.guild.roles, name="Mute")
                await user.add_roles(getRole)
                embed = discord.Embed(color=0xf10e0e, title="처벌내역",description=f"디스코드 정보: {user.mention}\n\n디스코드 ID: ``{user.id}``\n\n처벌수위: ``뮤트/영구``\n\n처벌사유: ``{check}``\n\n처리한 관리자: {ctx.author.mention}")
                await ctx.send(embed=embed)
                channel = self.bot.get_channel(706489228619546654)
                await channel.send(embed=embed)
            else:
                getRole = discord.utils.get(ctx.guild.roles, name="Mute")
                await user.add_roles(getRole)
                embed = discord.Embed(color=0xf10e0e, title="처벌내역",description=f"디스코드 정보: {user.mention}\n\n디스코드 ID: ``{user.id}``\n\n처벌수위: ``뮤트/{timeday}일{timehour}시간{timeminute}분``\n\n처벌사유: ``{check}``\n\n처리한 관리자: {ctx.author.mention}")
                await ctx.send(embed=embed)
                channel = self.bot.get_channel(706489228619546654)
                await channel.send(embed=embed)
                await asyncio.sleep(resulttime)
                await user.remove_roles(getRole)
        if timeday == '해제':
            getRole = discord.utils.get(ctx.guild.roles, name="Mute")
            await user.remove_roles(getRole)
            await ctx.send("\U00002705",delete_after=5)
        if timeday == '리로드':
            chlist = []
            if user == ctx.author:
                overwrite = discord.PermissionOverwrite()
                overwrite.send_messages=False
                overwrite.add_reactions=False
                wait = await ctx.send(embed=discord.Embed(title="처리중 입니다.",descriptsion="잠시만기다려주세요...."))
                for channel in ctx.guild.channels:
                    chlist.append(channel)
                    await channel.set_permissions(getRole, overwrite=overwrite)
                await wait.edit(embed=discord.Embed(title=f"완료 총{len(chlist)}개"))
                channel = self.bot.get_channel(706489228619546654)
                await channel.send(f"{ctx.author}가 채널 재설정을 완료했습니다.")
            else:
                await ctx.send(embed=discord.Embed(color=0xf10e0e,title="채널 재설정을 시도하시나요?",description="확인을 위해 자신을 맨션해주세요"))

    @commands.has_permissions(administrator=True)
    @commands.command(name="밴")
    async def _ban(self, ctx, user, day=None, hour=None, minute=None, *, check: str = None):
        
        timelist = [day,hour,minute]

        timeday = timelist[0]
        timehour = timelist[1]
        timeminute = timelist[2]

        async def replacemention(user):
            replace1 = user.replace("<","")
            replace2 = replace1.replace(">","")
            replace3 = replace2.replace("@","")
            replace4 = replace3.replace("!","")
            iduser = await self.bot.fetch_user(replace4)
            return iduser

        if timeday is not None and timehour is not None and timeminute is not None:
            resulttime = (int(timeday) * 86400)+(int(timehour) * 3600)+(int(timeminute) * 60)
            if resulttime == 0:
                iduser = await replacemention(user)
                embed = discord.Embed(color=0xf10e0e, title="처벌내역",description=f"디스코드 정보: {iduser.mention}\n\n디스코드 ID: ``{iduser.id}``\n\n처벌수위: ``밴/영구``\n\n처벌사유: ``{check}``\n\n처리한 관리자: {ctx.author.mention}")
                channel = self.bot.get_channel(706489228619546654)
                await channel.send(embed=embed)
                await ctx.send(embed=embed)
                await ctx.guild.ban(iduser)
        
            else:
                iduser = await replacemention(user)
                embed = discord.Embed(color=0xf10e0e, title="처벌내역",description=f"디스코드 정보: {iduser.mention}\n\n디스코드 ID: ``{iduser.id}``\n\n처벌수위: ``밴/{timeday}일{timehour}시간{timeminute}분``\n\n처벌사유: ``{check}``\n\n처리한 관리자: {ctx.author.mention}")
                await ctx.send(embed=embed)
                await ctx.guild.ban(iduser)
                channel = self.bot.get_channel(706489228619546654)
                await channel.send(embed=embed)
                await asyncio.sleep(resulttime)
                await ctx.guild.unban(iduser)
        elif timeday == '해제':
            iduser = await replacemention(user)
            await ctx.guild.unban(iduser)
            await ctx.send("\U00002705",delete_after=5)
    
    @commands.has_permissions(administrator=True)
    @commands.command(name="역할지급")
    async def _addrole(self, ctx):
        SearchRole = discord.utils.get(ctx.guild.roles, name="🎉디스코드 인원 200명 달성 기념🎉")
        asdf = [member for member in ctx.guild.members]
        for x in SearchRole.members:
            asdf.remove(x)
        for s in asdf:
            print("포문진입")
            await ctx.send(f"{s}지급")
            print("역할지급시작")
            await s.add_roles(SearchRole)
            print("지급완료")
        
    @commands.has_permissions(administrator=True)
    @commands.command(name="역할제거")
    async def _removerole(self, ctx, getrole:discord.Role):
        SearchRole = discord.utils.get(ctx.guild.roles, name=getrole.name)
        for member in ctx.guild.members:
            if SearchRole in member.roles:
                await member.remove_roles(SearchRole)
                print(f"{member}제거")
    
    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def 삭제(self, ctx, number: int = 1):
        author = ctx.author
        if number < 101:
            await ctx.channel.purge(limit = number + 1)
            await ctx.send(f"{author.mention}님이 메시지 ``{number}개``를 삭제했어요", delete_after=5)
        else:
            await ctx.send(f"{author.mention}님이 제한을 초과했습니다.", delete_after=5)

    @commands.command(name="공지")
    @commands.has_permissions(administrator=True)
    async def _notice(self, ctx, *, dec):
        channel = self.bot.get_channel(706482546048761919)
        embed=discord.Embed(title="📢공지사항", description=dec)
        embed.set_thumbnail(url="https://media.discordapp.net/attachments/704515498087284797/708127524944871424/2020-05-08_10_25_01.png")
        embed.set_footer(icon_url=ctx.author.avatar_url,text=f"공지 작성자: {ctx.author} • {now}")
        await channel.send(embed=embed)


    @commands.command(name="전체공지")
    @commands.has_permissions(administrator=True)
    async def _allnotice(self, ctx, *, dec):
        channel = self.bot.get_channel(706482546048761919)
        embed=discord.Embed(title="📢공지사항", description=dec)
        embed.set_thumbnail(url="https://media.discordapp.net/attachments/704515498087284797/708127524944871424/2020-05-08_10_25_01.png")
        embed.set_footer(icon_url=ctx.author.avatar_url,text=f"공지 작성자: {ctx.author} • {now}")
        await channel.send("@everyone")
        await channel.send(embed=embed)

def setup(bot):
    bot.add_cog(Admin(bot))
