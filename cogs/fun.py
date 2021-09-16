from discord.ext import commands
from typing import Union
import discord

# Local imports
from modules import globals, utils


class Fun(commands.Cog,
          description="Commands for them squad lols"):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="herb",
                      description="Roll someone a G+G+G blunt (cosmetic, no rewards)",
                      usage="{prfx}herb [ user ]",
                      help="user: the user to give a blunt to (ping, name, id) (optional)",
                      aliases=["blunt", "based",])
    async def cookie(self, ctx, target: Union[discord.Member, discord.User, int, str] = None):
        # Convert target input to discord.Member
        if not target:
            target = ctx.author
        if isinstance(target, int):
            target = ctx.guild.get_member(target)
        elif isinstance(target, str):
            target = await utils.get_best_member_match(ctx, target)
        elif isinstance(target, discord.User):
            target = ctx.guild.get_member(target.id)
        elif isinstance(target, discord.Member):
            pass
        else:
            await utils.embed_reply(ctx,
                                    title=f"💢 That is not a valid user!")
            return
        if not target:
            await utils.embed_reply(ctx,
                                    title=f"💢 That is not a valid user!")
            return
            return
        # Actual command
        if target.id != ctx.author.id:
            await utils.embed_reply(ctx,
                                    content=f"<@!{target.id}>",
                                    title=f"🌿 Herb!",
                                    description=f"<@!{ctx.author.id}> just rolled you a G+G+G blunt of the greenest herb🌿!\n"
                                                f"A mixture of 3 Green Herbs. Completely restores health.",
                                    thumbnail="https://cdn.discordapp.com/emojis/762601822979358751.png?v=1")
        else:
            await utils.embed_reply(ctx,
                                    title=f"🌿 Herb!",
                                    description=f"<@!{ctx.author.id}> found some funny looking plant and decided to smoke it🌿!\n"
                                                f"Herb that restores partial health.",
                                    thumbnail="https://cdn.discordapp.com/emojis/762601822979358751.png?v=1")

    @commands.command(name="burrito",
                      description="Deliver someone a SpaceBurrito (cosmetic, no rewards)",
                      usage="{prfx}burrito [ user ]",
                      help="user: the user to give a burrito to (ping, name, id) (optional)",
                      aliases=["spaceburrito", "galacticburrito"])
    async def burrito(self, ctx, target: Union[discord.Member, discord.User, int, str] = None):
        # Convert target input to discord.Member
        if not target:
            target = ctx.author
        if isinstance(target, int):
            target = ctx.guild.get_member(target)
        elif isinstance(target, str):
            target = await utils.get_best_member_match(ctx, target)
        elif isinstance(target, discord.User):
            target = ctx.guild.get_member(target.id)
        elif isinstance(target, discord.Member):
            pass
        else:
            await utils.embed_reply(ctx,
                                    title=f"💢 That is not a valid user!")
            return
        if not target:
            await utils.embed_reply(ctx,
                                    title=f"💢 That is not a valid user!")
            return
            return
        # Actual command
        if target.id != ctx.author.id:
            await utils.embed_reply(ctx,
                                    content=f"<@!{target.id}>",
                                    title=f"🌯 SpaceBurrito!",
                                    description=f"<@!{ctx.author.id}> just delivered you a delicious Space🌌Burrito🌯!\n"
                                                f"Eat it before it gets cold!",
                                    thumbnail="https://cdn.discordapp.com/emojis/779465397903949825.png")
        else:
            await utils.embed_reply(ctx,
                                    title=f"🌯 SpaceBurrito!",
                                    description=f"<@!{ctx.author.id}> doesn't have any friends yet so they bought themselves a delicious Space🌌Burrito🌯!\n"
                                                f"Time to eagerly enjoy it in complete silence!",
                                    thumbnail="https://cdn.discordapp.com/emojis/779465397903949825.png")


def setup(bot):
    bot.add_cog(Fun(bot))
