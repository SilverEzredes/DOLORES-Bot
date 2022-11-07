from discord.ext import commands

# Local imports
from modules import globals, utils


class REtools(commands.Cog,
          description="Commands for RE Engine tools."):
    def __init__(self, bot):
        self.bot = bot

    @utils.hybcommand(globals.bot,
                      name="reframework",
                      description="",
                      usage="{prfx}reframework",
                      help="",
                      aliases=["ref"],
                      slash_aliases=False)
    async def reframework(self, ctx):
        desc = "A mod framework, scripting platform, and modding tool for\n RE Engine games."
        await utils.embed_reply(ctx,
                                title="REFramework",
                                description=desc,
                                fields=[
                                    ["🔗 Link:",          "[REFramework - GitHub](https://github.com/praydog/REFramework-nightly/releases)",                                                                                                                                          True],
                                    ["💻 Developer", "Praydog",                                                                                                                                          True],
                                    ["📖 More Info:",       "[REF - GitBook](https://cursey.github.io/reframework-book/)",                                                                                                                                           True],
                                ],
                                thumbnail="https://cdn.discordapp.com/emojis/994126039246700544.png")

    @utils.hybcommand(globals.bot,
                      name="noesisplugin",
                      description="",
                      usage="{prfx}noesisplugin",
                      help="",
                      aliases=["noesis", "reem", "plugin", "fmt", "fmtremesh", "newms"],
                      slash_aliases=False)
    async def noesisplugin(self, ctx):
        desc = "A plugin for Rich Whitehouse's Noesis to import and export\n RE Engine Meshes and Textures."
        await utils.embed_reply(ctx,
                                title="Noesis Plugin - REEM Noesis CMD",
                                description=desc,
                                fields=[
                                    ["🔗 Link:",          "[Noesis Plugin - GitHub](https://github.com/alphazolam/fmt_RE_MESH-Noesis-Plugin)",                                                                                                                                          True],
                                    ["💻 Developer", "alphaZomega",                                                                                                                                          True],
                                ],
                                thumbnail="https://cdn.discordapp.com/emojis/994124668690767912.png")

    @utils.hybcommand(globals.bot,
                      name="retool",
                      description="",
                      usage="{prfx}retool",
                      help="",
                      aliases=["unpak"],
                      slash_aliases=False)
    async def retool(self, ctx):
        desc = "A tool used for extracting the embedded game files from every\n RE Engine game's PAK files."
        await utils.embed_reply(ctx,
                                title="REtool",
                                description=desc,
                                fields=[
                                    ["🔗 Link:",          "[REtool](https://residentevilmodding.boards.net/thread/10567/pak-tex-editing-tool)",                                                                                                                                          True],
                                    ["💻 Developer", "FluffyQuack",                                                                                                                                          True],
                                ],
                                thumbnail="https://cdn.discordapp.com/emojis/994126946680176751.png")

    @utils.hybcommand(globals.bot,
                      name="fluffymodmanager",
                      description="",
                      usage="{prfx}fluffymodmanager",
                      help="",
                      aliases=["fmm", "modmanager", "fluffy", "sockpuppet"],
                      slash_aliases=False)
    async def fluffymodmanager(self, ctx):
        desc = "Fluffy Manager 5000 lets you manage mods for various titles,\n such as most Resident Evil titles, Devil May Cry 5, SoulCalibur VI, and more."
        await utils.embed_reply(ctx,
                                title="Fluffy Mod Manager 5000",
                                description=desc,
                                fields=[
                                    ["🔗 Link:",          "[Fluffy Mod Manager](https://www.fluffyquack.com/)",                                                                                                                                          True],
                                    ["💻 Developer", "FluffyQuack",                                                                                                                                          True],
                                ],
                                thumbnail="https://cdn.discordapp.com/emojis/994126946680176751.png")

    @utils.hybcommand(globals.bot,
                      name="010-re_rsz",
                      description="",
                      usage="{prfx}010-re_rsz",
                      help="",
                      aliases=["rsz", "re_rsz", "holytemplate", "010rsz"],
                      slash_aliases=False)
    async def re_rsz(self, ctx):
        desc = "010 Editor Binary Template for editing RE Engine game files contiaining RSZ data."
        await utils.embed_reply(ctx,
                                title="RE RSZ",
                                description=desc,
                                fields=[
                                    ["🔗 Link:",          "[RE RSZ - GitHub](https://github.com/alphazolam/RE_RSZ)",                                                                                                                                          True],
                                    ["💻 Developer", "alphaZomega",                                                                                                                                          True],
                                    ["📖 More Info:",       "[RE RSZ - Thread](https://discord.com/channels/718224210270617702/930092288330309683/932644761028939816)",                                                                                                                                           True]
                                ],
                                thumbnail="https://cdn.discordapp.com/emojis/955607176674697276.png")

    @utils.hybcommand(globals.bot,
                      name="3dsmax--re_3dsmaxmesh",
                      description="",
                      usage="{prfx}3dsmax--re_3dsmaxmesh",
                      help="",
                      aliases=["3ds", "re_3dsmaxmesh", "3dsmesh", "maxscript", "ogms"],
                      slash_aliases=False)
    async def re_3dsmaxmesh(self, ctx):
        desc = "The original Maxscript created for importing and modifying\n RE2 mesh files, now works for all RE Engine games."
        await utils.embed_reply(ctx,
                                title="3DSmax MESH Script - RE-ENGINE MESH TOOL",
                                description=desc,
                                fields=[
                                    ["🔗 Link:",          "[3DSmax MESH - Thread](https://discord.com/channels/718224210270617702/930092288330309683/932645540599046204)",                                                                                                                                          True],
                                    ["💻 Developers", "Maliwei777, alphaZomega, MarioKart64n, Shigu and others",                                                                                                                                          True],
                                ],
                                thumbnail="https://cdn.discordapp.com/emojis/994125244212199424.png")

    @utils.hybcommand(globals.bot,
                      name="3dsmax--alphazomegatool",
                      description="",
                      usage="{prfx}3dsmax--alphazomegatool",
                      help="",
                      aliases=["3dsalpha", "alphazomegatool", "maxscriptalpha", "msalpha", "azt"],
                      slash_aliases=False)
    async def alphazomegatool(self, ctx):
        desc = "Alpha's Maxscript tool for 3DSmax is a kind of multi-tool used for various mesh-modding related tasks."
        await utils.embed_reply(ctx,
                                title="alphaZomega Tool",
                                description=desc,
                                fields=[
                                    ["🔗 Link:",          "[alphaZomega Tool - Thread](https://discord.com/channels/718224210270617702/930092288330309683/932645657364287519)",                                                                                                                                          True],
                                    ["💻 Developer", "alphaZomega",                                                                                                                                          True],
                                ],
                                thumbnail="https://cdn.discordapp.com/emojis/994125244212199424.png")

    @utils.hybcommand(globals.bot,
                      name="3dsmax--resetmesh",
                      description="",
                      usage="{prfx}3dsmax--resetmesh",
                      help="",
                      aliases=["3dsreset", "resetmesh", "maxscriptreset", "msreset", "reset"],
                      slash_aliases=False)
    async def resetmesh(self, ctx):
        desc = "ResetMesh is an older 3dsmax script Alpha made to fix broken meshing without needing to re-import the mesh through Noesis."
        await utils.embed_reply(ctx,
                                title="ResetMesh",
                                description=desc,
                                fields=[
                                    ["🔗 Link:",          "[ResetMesh - Thread](https://discord.com/channels/718224210270617702/930092288330309683/932645788826353705)",                                                                                                                                          True],
                                    ["💻 Developer", "alphaZomega",                                                                                                                                          True],
                                ],
                                thumbnail="https://cdn.discordapp.com/emojis/994125244212199424.png")

    @utils.hybcommand(globals.bot,
                      name="010--offsetfixer",
                      description="",
                      usage="{prfx}010--offsetfixer",
                      help="",
                      aliases=["010offset", "offsetbt"],
                      slash_aliases=False)
    async def offsetfixer(self, ctx):
        desc = "This universal script can instantly update thousands of offsets in any file."
        await utils.embed_reply(ctx,
                                title="Alpha's Offset Fixer",
                                description=desc,
                                fields=[
                                    ["🔗 Link:",          "[Alpha's Offset Fixer - GitHub](https://github.com/alphazolam/Alpha-Offset-Fixer)",                                                                                                                                          True],
                                    ["💻 Developer", "alphaZomega",                                                                                                                                          True],
                                    ["📖 More Info:",       "[Offset Fixer - Thread](https://discord.com/channels/718224210270617702/930092288330309683/932646362795868240)",                                                                                                                                           True],
                                ],
                                thumbnail="https://cdn.discordapp.com/emojis/955607176674697276.png")

    @utils.hybcommand(globals.bot,
                      name="3dsmax--motlisttool",
                      description="",
                      usage="{prfx}3dsmax--motlisttool",
                      help="",
                      aliases=["3dsmot", "3dsmotlist", "msmot"],
                      slash_aliases=False)
    async def motlisttool(self, ctx):
        desc = "The motlist tool is a Maxscript that can export animations imported by RevilMax back to the game format, for full animation modding."
        await utils.embed_reply(ctx,
                                title="Motlist Tool",
                                description=desc,
                                fields=[
                                    ["🔗 Link:",          "[Motlist Tool - Thread](https://discord.com/channels/718224210270617702/930092288330309683/932646688370331768)",                                                                                                                                          True],
                                    ["💻 Developer", "alphaZomega",                                                                                                                                          True],
                                ],
                                thumbnail="https://cdn.discordapp.com/emojis/994125244212199424.png")

    @utils.hybcommand(globals.bot,
                      name="010--motlisttemplate",
                      description="",
                      usage="{prfx}010--motlisttemplate",
                      help="",
                      aliases=["010mot", "motlisttemplate", "010motlist", "motlistbt", "motbt"],
                      slash_aliases=False)
    async def motlisttemplate(self, ctx):
        desc = "The motlist template is a helpful tool for editing RE Engine animations and their associated actions and effects."
        await utils.embed_reply(ctx,
                                title="Motlist Template",
                                description=desc,
                                fields=[
                                    ["🔗 Link:",          "[Motlist Template - Thread](https://discord.com/channels/718224210270617702/930092288330309683/932647093208760330)",                                                                                                                                          True],
                                    ["💻 Developers", "alphaZomega, che, Jackal",                                                                                                                                          True],
                                ],
                                thumbnail="https://cdn.discordapp.com/emojis/955607176674697276.png")

    @utils.hybcommand(globals.bot,
                      name="010--motbanktemplate",
                      description="",
                      usage="{prfx}010--motbanktemplate",
                      help="",
                      aliases=["010bank", "motbanktemplate", "010motbank", "motbankbt", "bankbt"],
                      slash_aliases=False)
    async def motbanktemplate(self, ctx):
        desc = "The motbank template is used to edit motbank files from all RE Engine games."
        await utils.embed_reply(ctx,
                                title="Motbank Template",
                                description=desc,
                                fields=[
                                    ["🔗 Link:",          "[Motbank Template - Thread](https://discord.com/channels/718224210270617702/930092288330309683/932647199974752256)",                                                                                                                                          True],
                                    ["💻 Developer", "alphaZomega",                                                                                                                                          True],
                                ],
                                thumbnail="https://cdn.discordapp.com/emojis/955607176674697276.png")

    @utils.hybcommand(globals.bot,
                      name="010--meshtemplate",
                      description="",
                      usage="{prfx}010--meshtemplate",
                      help="",
                      aliases=["010mesh", "meshtemplate", "meshbt"],
                      slash_aliases=False)
    async def meshtemplate(self, ctx):
        desc = "The MESH template can edit RE Engine MESH model files, allowing you to do such things as edit/rename individual bones."
        await utils.embed_reply(ctx,
                                title="Mesh Template",
                                description=desc,
                                fields=[
                                    ["🔗 Link:",          "[Mesh Template - Thread](https://discord.com/channels/718224210270617702/930092288330309683/932647646244507679)",                                                                                                                                          True],
                                    ["💻 Developers", "che, alphaZomega, Darkness",                                                                                                                                          True],
                                ],
                                thumbnail="https://cdn.discordapp.com/emojis/955607176674697276.png")

    @utils.hybcommand(globals.bot,
                      name="010--mdftemplate",
                      description="",
                      usage="{prfx}010--mdftemplate",
                      help="",
                      aliases=["010mdf", "mdftemplate", "mdfbt"],
                      slash_aliases=False)
    async def mdftemplate(self, ctx):
        desc = "The MDF template allows you to edit the texture locations, material flags and parameters of each material."
        await utils.embed_reply(ctx,
                                title="MDF Template",
                                description=desc,
                                fields=[
                                    ["🔗 Link:",          "[MDF Template - Thread](https://discord.com/channels/718224210270617702/930092288330309683/932648376221171832)",                                                                                                                                          True],
                                    ["💻 Developers", "che, alphaZomega, Darkness",                                                                                                                                          True],
                                ],
                                thumbnail="https://cdn.discordapp.com/emojis/955607176674697276.png")

    @utils.hybcommand(globals.bot,
                      name="010--chaintemplate",
                      description="",
                      usage="{prfx}010--chaintemplate",
                      help="",
                      aliases=["010chain", "chaintemplate", "chainbt"],
                      slash_aliases=False)
    async def chaintemplate(self, ctx):
        desc = "The Chain template can be used to edit the properties of RE Engine chain physics files."
        await utils.embed_reply(ctx,
                                title="Chain Template",
                                description=desc,
                                fields=[
                                    ["🔗 Link:",          "[Chain Template - Thread](https://discord.com/channels/718224210270617702/930092288330309683/932648576398540860)",                                                                                                                                          True],
                                    ["💻 Developer", "alphaZomega",                                                                                                                                          True],
                                ],
                                thumbnail="https://cdn.discordapp.com/emojis/955607176674697276.png")

    @utils.hybcommand(globals.bot,
                      name="010--gpuctemplate",
                      description="",
                      usage="{prfx}010--gpuctemplate",
                      help="",
                      aliases=["010gpuc", "gpuctemplate", "gpucbt"],
                      slash_aliases=False)
    async def gpuctemplate(self, ctx):
        desc = "The GPUC template for 010 lets you edit the properties of physics cloth files."
        await utils.embed_reply(ctx,
                                title="GPUC Template",
                                description=desc,
                                fields=[
                                    ["🔗 Link:",          "[GPUC Template - Thread](https://discord.com/channels/718224210270617702/930092288330309683/932648669956681739)",                                                                                                                                          True],
                                    ["💻 Developer", "alphaZomega",                                                                                                                                          True],
                                ],
                                thumbnail="https://cdn.discordapp.com/emojis/955607176674697276.png")

    @utils.hybcommand(globals.bot,
                      name="010--cliptmltemplate",
                      description="",
                      usage="{prfx}010--cliptmltemplate",
                      help="",
                      aliases=["010clip", "cliptmltemplate", "010tml", "tmlbt", "clipbt"],
                      slash_aliases=False)
    async def cliptmltemplate(self, ctx):
        desc = "The TML template edits RE engine timeline files (tml and clip)."
        await utils.embed_reply(ctx,
                                title="CLIP-TML Template",
                                description=desc,
                                fields=[
                                    ["🔗 Link:",          "[CLIP-TML Template - Thread](https://discord.com/channels/718224210270617702/930092288330309683/932648812596588594)",                                                                                                                                          True],
                                    ["💻 Developer", "alphaZomega",                                                                                                                                          True],
                                ],
                                thumbnail="https://cdn.discordapp.com/emojis/955607176674697276.png")

    @utils.hybcommand(globals.bot,
                      name="010--guitemplate",
                      description="",
                      usage="{prfx}010--guitemplate",
                      help="",
                      aliases=["010gui", "guitemplate", "guibt"],
                      slash_aliases=False)
    async def guitemplate(self, ctx):
        desc = "The GUI template can show you the properties of gui Graphical User Interface files."
        await utils.embed_reply(ctx,
                                title="GUI Template",
                                description=desc,
                                fields=[
                                    ["🔗 Link:",          "[GUI Template - Thread](https://discord.com/channels/718224210270617702/930092288330309683/932648939541389352)",                                                                                                                                          True],
                                    ["💻 Developer", "alphaZomega",                                                                                                                                          True],
                                ],
                                thumbnail="https://cdn.discordapp.com/emojis/955607176674697276.png")

    @utils.hybcommand(globals.bot,
                      name="010--fbxskeltemplate",
                      description="",
                      usage="{prfx}010--fbxskeltemplate",
                      help="",
                      aliases=["010fbx", "fbxskeltemplate", "fbxbt", "010skel", "skelbt"],
                      slash_aliases=False)
    async def fbxskeltemplate(self, ctx):
        desc = "The fbxskel template is used for editing fbxskel skeleton files from all RE Engine games."
        await utils.embed_reply(ctx,
                                title="FBXskel Template",
                                description=desc,
                                fields=[
                                    ["🔗 Link:",          "[FBXskel Template - Thread](https://discord.com/channels/718224210270617702/930092288330309683/932649195674935336)",                                                                                                                                          True],
                                    ["💻 Developers", "che, alphaZomega",                                                                                                                                          True],
                                ],
                                thumbnail="https://cdn.discordapp.com/emojis/955607176674697276.png")

    @utils.hybcommand(globals.bot,
                      name="010--textemplate",
                      description="",
                      usage="{prfx}010--textemplate",
                      help="",
                      aliases=["010tex", "textemplate", "texbt"],
                      slash_aliases=False)
    async def textemplate(self, ctx):
        desc = "The TEX template shows how the RE Engine tex texture format works."
        await utils.embed_reply(ctx,
                                title="TEX Template",
                                description=desc,
                                fields=[
                                    ["🔗 Link:",          "[TEX Template - Thread](https://discord.com/channels/718224210270617702/930092288330309683/932649305536364635)",                                                                                                                                          True],
                                    ["💻 Developers", "che, alphaZomega",                                                                                                                                          True],
                                ],
                                thumbnail="https://cdn.discordapp.com/emojis/955607176674697276.png")

    @utils.hybcommand(globals.bot,
                      name="010--efxtemplate",
                      description="",
                      usage="{prfx}010--efxtemplate",
                      help="",
                      aliases=["010efx", "efxtemplate", "efxbt", "010fx", "fxbt"],
                      slash_aliases=False)
    async def efxtemplate(self, ctx):
        desc = "The EFX template lets you change effects in RE Engine EFX files."
        await utils.embed_reply(ctx,
                                title="EFX Template",
                                description=desc,
                                fields=[
                                    ["🔗 Link:",          "[EFX Template - Thread](https://discord.com/channels/718224210270617702/930092288330309683/932649426328125500)",                                                                                                                                          True],
                                    ["💻 Developer", "Darkness",                                                                                                                                          True],
                                ],
                                thumbnail="https://cdn.discordapp.com/emojis/955607176674697276.png")

    @utils.hybcommand(globals.bot,
                      name="010--uvartemplate",
                      description="",
                      usage="{prfx}010--uvartemplate",
                      help="",
                      aliases=["010uvar", "uvartemplate", "uvarbt"],
                      slash_aliases=False)
    async def uvartemplate(self, ctx):
        desc = "The UVAR template allows you to edit uvar 'uvariables' files from all RE Engine games."
        await utils.embed_reply(ctx,
                                title="UVAR Template",
                                description=desc,
                                fields=[
                                    ["🔗 Link:",          "[UVAR Template - Thread](https://discord.com/channels/718224210270617702/930092288330309683/932650247312769094)",                                                                                                                                          True],
                                    ["💻 Developer", "alphaZomega",                                                                                                                                          True],
                                ],
                                thumbnail="https://cdn.discordapp.com/emojis/955607176674697276.png")

    @utils.hybcommand(globals.bot,
                      name="mdfmanager",
                      description="",
                      usage="{prfx}mdfmanager",
                      help="",
                      aliases=["mdf", "mdftool"],
                      slash_aliases=False)
    async def mdfmanager(self, ctx):
        desc = "MDF Manager is a great tool for editing material files in all RE Engine games."
        await utils.embed_reply(ctx,
                                title="MDF Manager",
                                description=desc,
                                fields=[
                                    ["🔗 Link:",          "[MDF Manager - GitHub](https://github.com/Silvris/MDF-Manager)",                                                                                                                                          True],
                                    ["💻 Developer", "Silvris",                                                                                                                                          True],
                                    ["📖 More Info:",       "[MDF Manager - Thread](https://discord.com/channels/718224210270617702/930092288330309683/932648163251191819)",                                                                                                                                           True],
                                ],
                                thumbnail="https://cdn.discordapp.com/emojis/994146859327172689.png")

    @utils.hybcommand(globals.bot,
                      name="ringingbloom",
                      description="",
                      usage="{prfx}ringingbloom",
                      help="",
                      aliases=["audiotool", "bnk", "rb"],
                      slash_aliases=False)
    async def ringingbloom(self, ctx):
        desc = "RingingBloom is a helpful tool for audio modding in RE Engine games, editing PCK, BNK, wem and wwise files in a streamlined application."
        await utils.embed_reply(ctx,
                                title="Ringing Bloom",
                                description=desc,
                                fields=[
                                    ["🔗 Link:",          "[Ringing Bloom - GitHub](https://github.com/Silvris/RingingBloom)",                                                                                                                                          True],
                                    ["💻 Developer", "Silvris",                                                                                                                                          True],
                                    ["📖 More Info:",       "[Ringing Bloom - Thread](https://discord.com/channels/718224210270617702/930092288330309683/932648013300654131)",                                                                                                                                           True],
                                ],
                                thumbnail="https://cdn.discordapp.com/emojis/994146859327172689.png")

    @utils.hybcommand(globals.bot,
                      name="3dsmax--fbxskeltool",
                      description="",
                      usage="{prfx}3dsmax--fbxskeltool",
                      help="",
                      aliases=["3dsfbx", "fbxskeltool", "3dsfbxskel", "msfbx", "msskel"],
                      slash_aliases=False)
    async def fbxskeltool(self, ctx):
        desc = "The fbxskel tool is Maxscript for 3dsmax that can import and export fbxskel skeleton files from all RE Engine games."
        await utils.embed_reply(ctx,
                                title="Fbxskel Tool",
                                description=desc,
                                fields=[
                                    ["🔗 Link:",          "[Fbxskel Tool - Thread](https://discord.com/channels/718224210270617702/930092288330309683/932649107091247195)",                                                                                                                                          True],
                                    ["💻 Developer", "alphaZomega",                                                                                                                                          True],
                                ],
                                thumbnail="https://cdn.discordapp.com/emojis/994125244212199424.png")

    @utils.hybcommand(globals.bot,
                      name="msgtool",
                      description="",
                      usage="{prfx}msgtool",
                      help="",
                      aliases=["msg"],
                      slash_aliases=False)
    async def msgtool(self, ctx):
        desc = "The MSG Tool allows you to extract, edit and replace the contents of RE Engine MSG Files."
        await utils.embed_reply(ctx,
                                title="MSG Tool",
                                description=desc,
                                fields=[
                                    ["🔗 Link:",          "[MSG Tool - Thread](https://discord.com/channels/718224210270617702/930092288330309683/940772924531552257)",                                                                                                                                          True],
                                    ["💻 Developer", "ponaromixxx",                                                                                                                                          True],
                                ],
                                thumbnail=globals.bot.user.display_avatar.url)

    @utils.hybcommand(globals.bot,
                      name="emvengine",
                      description="",
                      usage="{prfx}emv",
                      help="",
                      aliases=["emvengine", "console", "refconsole"],
                      slash_aliases=False)
    async def emv(self, ctx):
        desc = "Alpha's REFramework scripts, which include an interactive Lua Console that can access your global script variables, useful for script development.\n Also includes: Gravity Gun, Console, Enhanced Model Viewer and Enemy Spawner."
        await utils.embed_reply(ctx,
                                title="EMV Engine",
                                description=desc,
                                fields=[
                                    ["🔗 Link:",          "[EMV Engine - GitHub](https://github.com/alphazolam/REFramework-Scripts)",                                                                                                                                          True],
                                    ["💻 Developer", "alphaZomega",                                                                                                                                          True],
                                    ["📖 More Info:",       "[EMV Engine - Thread](https://discord.com/channels/718224210270617702/930092288330309683/993612146413928448)",                                                                                                                                           True],
                                ],
                                thumbnail="https://cdn.discordapp.com/emojis/994124668690767912.png")

    @utils.hybcommand(globals.bot,
                      name="blenderplugin",
                      description="",
                      usage="{prfx}blenderplugin",
                      help="",
                      aliases=["blender", "wrapper"],
                      slash_aliases=False)
    async def blenderplugin(self, ctx):
        desc = "This useful Blender addon utilizes the Noesis MESH plugin to let you to seamlessly import and export RE Engine MESH models directly from Blender."
        await utils.embed_reply(ctx,
                                title="Blender Wrapper",
                                description=desc,
                                fields=[
                                    ["🔗 Link:",          "[Blender Wrapper - GitHub](https://github.com/NSACloud/Blender-RE-Mesh-Noesis-Wrapper)",                                                                                                                                          True],
                                    ["💻 Developer", "NSA Cloud",                                                                                                                                          True],
                                    ["📖 More Info:",       "[Blender Wrapper - Thread](https://discord.com/channels/718224210270617702/930092288330309683/993614546054938686)",                                                                                                                                           True],
                                ],
                                thumbnail="https://cdn.discordapp.com/emojis/994151478065373225.png")

    @utils.hybcommand(globals.bot,
                      name="relit",
                      description="",
                      usage="{prfx}relit",
                      help="",
                      aliases=["lights", "rel"],
                      slash_aliases=False)
    async def relit(self, ctx):
        desc = "It allows you to spawn lights in a scene for screenshotting purposes."
        await utils.embed_reply(ctx,
                                title="RELit",
                                description=desc,
                                fields=[
                                    ["🔗 Link:",          "[RELit - GitHub]( https://github.com/originalnicodr/RELit)",                                                                                                                                          True],
                                    ["💻 Developer", "originalnicodr, Otis_inf",                                                                                                                                          True],
                                    ["📖 More Info:",       "[RELit - Thread](https://discord.com/channels/718224210270617702/930092288330309683/993615154845581323)",                                                                                                                                           True],
                                ],
                                thumbnail=globals.bot.user.display_avatar.url)

    @utils.hybcommand(globals.bot,
                      name="list",
                      description="",
                      usage="{prfx}list",
                      help="",
                      aliases="",
                      slash_aliases=False)
    async def list(self, ctx):
        desc = ".list files for REtool or REE.Unpacker"
        await utils.embed_reply(ctx,
                                title="List",
                                description=desc,
                                fields=[
                                    ["🔗 Link:",          "[List - GitHub]( https://github.com/Ekey/REE.PAK.Tool)",                                                                                                                                          True],
                                    ["💻 Developer", "Ekey",                                                                                                                                          True],
                                ],
                                thumbnail="https://cdn.discordapp.com/emojis/1039083967401435136.png")

async def setup(bot):
    await bot.add_cog(REtools(bot))