
from discord.ext import commands
import discord

# Local imports
from modules import globals, utils


class Fun(commands.Cog,
          description="Commands for them squad lols"):
    def __init__(self, bot):
        self.bot = bot

    @utils.hybcommand(globals.bot,
                      name="herb",
                      description="Roll someone a G+G+G blunt (cosmetic, no rewards)",
                      usage="{prfx}herb [ user ]",
                      help="user: the user to give a blunt to (ping, name, id) (optional)",
                      aliases=["blunt", "based",])
    async def cookie(self, ctx, user: discord.Member = None):
        if user and user.id != ctx.author.id:
            await utils.embed_reply(ctx,
                                    content=f"<@!{user.id}>",
                                    title="🍪🌿 Herb!",
                                    description=f"<@!{ctx.author.id}> just rolled you a G+G+G blunt of the greenest herb🌿!\n"
                                                "A mixture of 3 Green Herbs. Completely restores health.",
                                    thumbnail="https://cdn.discordapp.com/emojis/762601822979358751.png")
        else:
            await utils.embed_reply(ctx,
                                    title="🌿 Herb!",
                                    description=f"<@!{ctx.author.id}> found some funny looking plant and decided to smoke it🌿!\n"
                                                "Herb that restores partial health.",
                                    thumbnail="https://cdn.discordapp.com/emojis/762601822979358751.png")

    @utils.hybcommand(globals.bot,
                      name="chocobar",
                      description="Treat someone with a delicious SewerChocolate™️ (cosmetic, no rewards)",
                      usage="{prfx}chocobar [ user ]",
                      help="user: the user to give a choco bar to (ping, name, id) (optional)",
                      aliases=["chocolatebar", "sewerchocolate", "choco", "sewerchoco"])
    async def burrito(self, ctx, user: discord.Member = None):
        if user and user.id != ctx.author.id:
            await utils.embed_reply(ctx,
                                    content=f"<@!{user.id}>",
                                    title="🍫 Sewer Chocolate™️!",
                                    description=f"<@!{ctx.author.id}> just delivered you a delicious 🍫 Sewer Chocolate™️🍫!\n"
                                                "Just don't look at the expiration date...",
                                    thumbnail="https://cdn.discordapp.com/emojis/888191417556561980.png")
        else:
            await utils.embed_reply(ctx,
                                    title="🍫 Sewer Chocolate™️!",
                                    description=f"<@!{ctx.author.id}> found some 🍫 chocolate bar looking thing while exploring the sewers.\n"
                                                "Are you really considering eating that?",
                                    thumbnail="https://cdn.discordapp.com/emojis/888191417556561980.png")

    @utils.hybcommand(globals.bot,
                      name="pat",
                      description="Pat someone (cosmetic, no rewards)",
                      usage="{prfx}pat [ user ]",
                      help="user: the user to pat (ping, name, id) (optional)",
                      aliases=["pet", "patpat"])
    async def pat(self, ctx, user: discord.Member = None):
        if user and user.id != ctx.author.id:
            await utils.embed_reply(ctx,
                                    content=f"<@!{user.id}>",
                                    title="<a:PatPatPat:836341685952184388> \\*PatPat\\*",
                                    description=f"<@!{ctx.author.id}> just delivered you a truckload of heartfelt pats!\n"
                                                "Cheer up pal, you're a wonderful person!",
                                    thumbnail="https://cdn.discordapp.com/emojis/889187488915128421.gif")
        else:
            await utils.embed_reply(ctx,
                                    title="<a:PatPatPat:836341685952184388> \\*PatPat\\*",
                                    description=f"<@!{ctx.author.id}> doesn't have any friends yet so they tried consoling themselves with a few pats!\n"
                                                "Cheer up pal, life gets better!",
                                    thumbnail="https://cdn.discordapp.com/emojis/889190978001465476.gif")

    @utils.hybcommand(globals.bot,
                      name="noises_Plugin_REEM",
                      description="",
                      usage="{prfx}noisesplugin",
                      help="",
                      aliases=["noises"])
    async def noisesplugin(self, ctx):
        desc = "A plugin for Rich Whitehouse's Noises to import and export\n RE Engine Meshes and Textures."
        await utils.embed_reply(ctx,
                                title="Noises Plugin - REEM Noises CMD",
                                description=desc,
                                fields=[
                                    ["🔗 Link:",          "[Noises Plugin - GitHub](https://www.youtube.com/watch?v=t0I4mTEdAf8)",                                                                                                                                          True],
                                    ["💻 Developer", "alphaOmega",                                                                                                                                          True],
                                ],
                                thumbnail="https://cdn.discordapp.com/emojis/994124668690767912.png")


async def setup(bot):
    await bot.add_cog(Fun(bot))
