import os
import discord
from discord import ui
from discord.ext import commands

BOT_TOKEN: str = "YOUR_BOT_TOKEN"
COMMAND_PREFIX: str = "!"
gateway_intents: discord.Intents = discord.Intents.default()
gateway_intents.message_content = True


class CustomView(ui.LayoutView):
    def __init__(self, footer_text: str) -> None:
        super().__init__(timeout=None)
        container = ui.Container(accent_color=None)  # Tạo Container + xoá viền bên trái
        container.add_item(ui.TextDisplay("## Components V2 Test"))  # Tiêu đề lớn
        container.add_item(ui.Separator())  # Chèn đường kẻ ngang
        container.add_item(ui.TextDisplay("-# Đẹp trai vl"))  # Ghi chú
        container.add_item(ui.Separator())  # Chèn đường kẻ ngang
        
        main_content = (  # Nội dung
            "### Text\n"  # Tiêu đề nhỏ
            "- **Text 1:** Text 1\n"
            "- **Text 2:** Text 2\n"
            "- **Text 3:** Text 3\n\n"
            "### Commands\n"  # Tiêu đề nhỏ
            "- `!dz` - Đẹp trai\n"
            "- `!alpha` - Đẹp trai\n"
            "- `!beta` - Đẹp trai\n"
            "- `!deptrai` - Đẹp trai"
        )
        
        container.add_item(ui.TextDisplay(main_content))  # Nạp nội dung vào Container
        container.add_item(ui.Separator())  # Chèn đường kẻ ngang
        container.add_item(ui.TextDisplay(footer_text))  # Thêm footer vào dưới cùng
        container.add_item(ui.Separator())  # Chèn đường phân cách nằm giữa footer và hàng nút bấm
        
        action_row = ui.ActionRow(  # Tạo khay chứa hàng ngang để sắp xếp các nút bấm
            ui.Button(label="Server Support", style=discord.ButtonStyle.link, url="https://discord.gg/your-invite"),
            ui.Button(label="Your Channel", style=discord.ButtonStyle.link, url="https://youtube.com/@your-channel")
        )
        
        container.add_item(action_row)  # Thêm khay chứa hàng ngang ActionRow vào bên trong khối Container
        self.add_item(container)  # Nạp toàn bộ item Container vào cấu trúc cây hiển thị của LayoutView
        

class CoreBot(commands.Bot):
    def __init__(self) -> None:
        super().__init__(
            command_prefix=COMMAND_PREFIX, 
            intents=gateway_intents, 
            help_command=None 
        )

    async def on_ready(self) -> None:
        print(f"==================================================")
        print(f"✅ Bot logged in as: {self.user} | ID: {self.user.id}")
        print(f"==================================================")

bot = CoreBot()

@bot.command(name="dz", aliases=["alpha", "beta", "deptrai"])
async def dz_command(ctx: commands.Context) -> None:
    formatted_time: str = discord.utils.utcnow().strftime("%d/%m/%Y %H:%M")
    footer_text: str = f"-# Requested by {ctx.author.name} • {formatted_time}"
    await ctx.send(view=CustomView(footer_text=footer_text))
    

if __name__ == "__main__":
    if BOT_TOKEN == "YOUR_BOT_TOKEN_HERE" or not BOT_TOKEN:
        raise ValueError("ERROR: Sai token. Nhập lại 'BOT_TOKEN'.")
    bot.run(BOT_TOKEN)
    