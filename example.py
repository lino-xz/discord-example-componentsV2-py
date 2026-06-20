import os
import discord
from discord import ui
from discord.ext import commands

BOT_TOKEN: str = "YOUR_BOT_TOKEN_HERE"
COMMAND_PREFIX: str = "!"
gateway_intents: discord.Intents = discord.Intents.default()
gateway_intents.message_content = True


class CustomView(ui.LayoutView):
    def __init__(self, footer_text: str) -> None:
        super().__init__(timeout=None)
        container = ui.Container(accent_color=None)  # Tạo embed + gỡ bỏ đường viền bên trái
        container.add_item(ui.TextDisplay("## Components V2 Test"))  # Chèn tiêu đề dạng Heading 2 vào khối Container
        container.add_item(ui.Separator())  # Chèn một đường kẻ ngang
        container.add_item(ui.TextDisplay("-# Đẹp trai vl"))  # Thêm dòng ghi chú
        container.add_item(ui.Separator())  # Chèn một đường kẻ ngang
        
        main_content = (  # Tạo văn bản chứa nội dung hiển thị
            "### Text\n"  # Định dạng tiêu đề dạng Heading 3 phần 1
            "- **Text 1:** Text 1\n"
            "- **Text 2:** Text 2\n"
            "- **Text 3:** Text 3\n\n"
            "### Commands\n"  # Định dạng tiêu đề dạng Heading 3 phần 2
            "- `!dz` - Đẹp trai\n"
            "- `!alpha` - Đẹp trai\n"
            "- `!beta` - Đẹp trai\n"
            "- `!deptrai` - Đẹp trai"
        )  # Kết thúc khai báo văn bản cho nội dung
        
        container.add_item(ui.TextDisplay(main_content))  # Nạp toàn bộ khối văn bản đã gom nhóm vào Container
        container.add_item(ui.Separator())  # Chèn một đường kẻ ngang
        container.add_item(ui.TextDisplay(footer_text))  # Cho footer vào dưới cùng
        container.add_item(ui.Separator())  # Chèn một đường phân cách nằm giữa footer và hàng nút bấm
        
        action_row = ui.ActionRow(  # Tạo khay chứa hàng ngang để sắp xếp các nút bấm
            ui.Button(label="Server Support", style=discord.ButtonStyle.link, url="https://discord.gg/your-invite"),  # Tạo nút bấm chứa liên kết đến server Discord
            ui.Button(label="Your Channel", style=discord.ButtonStyle.link, url="https://youtube.com/@your-channel")  # Tạo nút bấm chứa liên kết đến kênh YouTube
        )  # Kết thúc quá trình cấu hình danh sách phần tử cho khay ActionRow
        
        container.add_item(action_row)  # Đẩy khay chứa hàng ngang ActionRow vào bên trong khối Container
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

@bot.command(name="dz", aliases=["alpha", "beta", "deptrai"])  # Đăng ký lệnh + bí danh lệnh
async def dz_command(ctx: commands.Context) -> None:  # Khai báo hàm xử lý lệnh dz
    formatted_time: str = discord.utils.utcnow().strftime("%d/%m/%Y %H:%M")  # Format: ngày/tháng/năm giờ:phút UTC
    footer_text: str = f"-# Requested by {ctx.author.name} • {formatted_time}"  # Thiết lập text footer chứa tên và thời gian
    await ctx.send(view=CustomView(footer_text=footer_text))  # Gửi phản hồi kèm giao diện View phẳng không viền dọc
    

if __name__ == "__main__":
    if BOT_TOKEN == "YOUR_BOT_TOKEN_HERE" or not BOT_TOKEN:
        raise ValueError("CRITICAL_ERROR: Sai token. Vui lòng nhập đúng 'BOT_TOKEN'.")
    bot.run(BOT_TOKEN)
    