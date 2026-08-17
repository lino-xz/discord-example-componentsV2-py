import sys
from datetime import datetime, timedelta, timezone
import discord
from discord import ui
from discord.ext import commands

TOKEN = "YOUR_BOT_TOKEN"
PREFIX = "$"

intents = discord.Intents.all()
VN_TZ = timezone(timedelta(hours=7))


class InfoView(ui.LayoutView):
    def __init__(self, footer: str):
        super().__init__(timeout=None)

        # Container
        container = ui.Container()

        # Header
        container.add_item(ui.TextDisplay("## Components V2 Test"))
        container.add_item(ui.Separator())
        container.add_item(ui.TextDisplay("-# Vanish Club"))
        container.add_item(ui.Separator())

        # Text
        container.add_item(ui.TextDisplay(
            "### Text\n"
            "- **Text 1:** Text 1\n"
            "- **Text 2:** Text 2\n"
            "- **Text 3:** Text 3"
        ))

        container.add_item(ui.Separator())

        # Commands
        container.add_item(ui.TextDisplay(
            "### Commands\n"
            "- `$dz` - Cool\n"
            "- `$alpha` - Cool\n"
            "- `$beta` - Cool\n"
            "- `$deptrai` - Cool"
        ))

        # Footer
        container.add_item(ui.Separator())
        container.add_item(ui.TextDisplay(footer))
        container.add_item(ui.Separator())

        # Link buttons
        container.add_item(ui.ActionRow(
            ui.Button(
                label="Server",
                style=discord.ButtonStyle.link,
                url="https://discord.gg/your-invite"
            ),
            ui.Button(
                label="YouTube",
                style=discord.ButtonStyle.link,
                url="https://youtube.com/@your-channel"
            )
        ))

        self.add_item(container)


class Bot(commands.Bot):
    def __init__(self):
        super().__init__(
            command_prefix=PREFIX,
            intents=intents,
            help_command=None
        )

    async def on_ready(self):
        print("=" * 50)
        print(f"[+] Logged in as {self.user} | ID: {self.user.id}")
        print("=" * 50)


bot = Bot()


# Command
@bot.command(name="dz", aliases=["alpha", "beta", "deptrai"])
async def dz(ctx: commands.Context):
    timestamp = datetime.now(VN_TZ).strftime("%d/%m/%Y %H:%M")
    footer = f"-# Requested by {ctx.author.name} • {timestamp}"

    await ctx.send(view=InfoView(footer))


if __name__ == "__main__":
    if not TOKEN or TOKEN == "YOUR_BOT_TOKEN":
        print("[!] Bot token is not configured!")
        sys.exit(1)

    try:
        bot.run(TOKEN)
    except discord.LoginFailure:
        print("[!] Invalid bot token!")
        sys.exit(1)
    except KeyboardInterrupt:
        print("\n[!] Bot stopped!")
        