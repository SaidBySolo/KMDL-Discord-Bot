import discord
from discord.ext import commands

class Events(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.send("권한이 부족합니다.", delete_after=5)
        
    @commands.Cog.listener()
    async def on_message(self, message):
        time = message.created_at
        channel = self.bot.get_channel(709231709392207953)
        embed = discord.Embed(title="Log", description=f'DID:``{message.author.id}``\nFull Name:``{message.author}``')
        embed.set_thumbnail(url=message.author.avatar_url)
        embed.add_field(name="Name",value=message.author.mention)
        embed.add_field(name="Channel name",value=f"{message.channel.mention}")
        embed.add_field(name="Timestamp",value=f"{str(time.year)}-{str(time.month)}-{str(time.day)}\n{str(time.hour)}:{str(time.minute)}:{str(time.second)}")
        embed.add_field(name="Content", value=message.content)
        await channel.send(embed=embed)
        await self.bot.process_commands(message)

def setup(bot):
    bot.add_cog(Events(bot))