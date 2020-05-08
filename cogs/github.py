import aiohttp
import discord
from discord.ext import commands
import asyncio

class Github(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="깃허브")
    async def _github(self, ctx, *, search):
        URL = f"https://api.github.com/search/repositories?q={search}"
        async with aiohttp.ClientSession() as cs:
            async with cs.get(URL) as r:
                response = await r.json()
                count = response['total_count']
                item = response['items']
                itemlist = [im['full_name'] for im in item]
                sortitemlist =[str(index) + ". " + im for index, im in enumerate(itemlist, 1)]
                embed = discord.Embed(title="요청하신 내용입니다.",description=f"검색 결과:{count}개")
                embed.add_field(name="레포지토리 이름",value='\n'.join(sortitemlist))
                info = await ctx.send(embed=embed)
                await info.add_reaction("🔍")
                channel = ctx.channel
                def check(reaction, user):
                    return user == ctx.author and str(reaction.emoji) == '🔍'
                def check2(m):
                    return m.channel == channel
                reaction, user = await self.bot.wait_for('reaction_add', check=check, timeout=300)
                await ctx.send("30초이내에 번호를 입력하세요", delete_after=5)
                try:
                    respon = await self.bot.wait_for('message', check=check2, timeout=30)
                except asyncio.TimeoutError:
                    await ctx.send("시간 초과입니다.")
                else:
                    if ctx.author == respon.author:
                        fetmsg = await ctx.fetch_message(respon.id)
                    temp_item = item[int(fetmsg.content) - 1]
                    name = temp_item['full_name']
                    url = temp_item['html_url']
                    desc = temp_item['description']
                    star = temp_item['stargazers_count']
                    fork = temp_item['forks_count']
                    lang = temp_item['language']
                    owner = temp_item['owner']
                    ownerlogin = owner['login']
                    avatar = owner['avatar_url']
                    lic = temp_item['license']
                    licen = lic['name']
                    embed = discord.Embed(title=name,description=desc,url=url)
                    embed.set_thumbnail(url=avatar)
                    embed.add_field(name="Owner",value=ownerlogin)
                    embed.add_field(name="Language",value=lang)
                    embed.add_field(name="License",value=licen)
                    embed.add_field(name="Star",value=star)
                    embed.add_field(name="Fork",value=fork)
                    await info.edit(embed = embed)
                    await info.clear_reaction("🔍")
                    await fetmsg.delete()

def setup(bot):
    bot.add_cog(Github(bot))