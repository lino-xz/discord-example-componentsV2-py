import sys
import asyncio
from datetime import datetime, timedelta, timezone
import discord
from discord import ui
from discord.ext import commands

TOKEN = "bot_token"
PREFIX = "$"
intents = discord.Intents.all()
VN_TZ = timezone(timedelta(hours=7))


class InfoView(ui.LayoutView):
    def __init__(self, footer: str):
        super().__init__(timeout=None)
        container = ui.Container()

        # Header
        container.add_item(ui.TextDisplay("## Components V2 Test"))
        container.add_item(ui.Separator())
        container.add_item(ui.TextDisplay("-# Vanish Club"))
        container.add_item(ui.Separator())

        # Content
        container.add_item(ui.TextDisplay(
            "### Text\n"
            "- **Text 1:** Text 1\n"
            "- **Text 2:** Text 2\n"
            "- **Text 3:** Text 3"
        ))
        container.add_item(ui.Separator())
        container.add_item(ui.TextDisplay(
            "### Commands\n"
            "- `$info` - Cool\n"
            "- `$test` - Cool"
        ))

        # Footer + buttons
        container.add_item(ui.Separator())
        container.add_item(ui.TextDisplay(footer))
        container.add_item(ui.Separator())
        container.add_item(ui.ActionRow(
            ui.Button(label="Server", style=discord.ButtonStyle.link, url="https://discord.gg/your-invite"),
            ui.Button(label="YouTube", style=discord.ButtonStyle.link, url="https://youtube.com/@your-channel")
        ))

        self.add_item(container)


bot = commands.Bot(command_prefix=PREFIX, intents=intents, help_command=None)


@bot.event
async def on_ready():
    print(f"[+] Logged in as {bot.user} | ID: {bot.user.id}")


@bot.command(name="info", aliases=["test"])
async def info(ctx: commands.Context):
    timestamp = datetime.now(VN_TZ).strftime("%d/%m/%Y %H:%M")
    footer = f"-# Requested by {ctx.author.name} • {timestamp}"
    await ctx.send(view=InfoView(footer))


if __name__ == "__main__":
    if not TOKEN or TOKEN == "bot_token":
        print("[!] Bot token is not configured!")
        sys.exit(1)

    try:
        asyncio.run(bot.start(TOKEN))
    except discord.LoginFailure:
        print("[!] Invalid bot token!")
        sys.exit(1)
    except KeyboardInterrupt:
        print("\n[!] Bot stopped!")
        