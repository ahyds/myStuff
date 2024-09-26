# 自动化解决方案作为Python编程专家，
# 我为朋友提供了一个自动化解决方案。通过编写Python脚本，我们可以快速批量地给图片添加水印，大大提升工作效率。

# 实现步骤
# 读取指定文件夹中的图片：打开存储图片的文件夹。
# 添加水印：在图片右上角加上指定的水印内容。
# 保存新图片：将添加水印后的图片另存为新文件

import os
from PIL import Image, ImageDraw, ImageFont

# 设置水印内容和样式
watermark_text = "数据来源：数海丹心公众号"
font_size = 10.5  # 五号字体大约对应10.5pt
font_color = (255, 0, 0)  # 红色
font_path = r"./simhei.ttf"
font = ImageFont.truetype(font_path, font_size)

# 打开文件夹并遍历文件夹中的所有png图片
folder_path = r"./extracted_images"
for filename in os.listdir(folder_path):
    if filename.endswith(".png"):
        print(f"处理文件: {filename}")
        img_path = os.path.join(folder_path, filename)
        img = Image.open(img_path)
        draw = ImageDraw.Draw(img)
        img_width, img_height = img.size
        text_bbox = draw.textbbox((0, 0), watermark_text, font=font)
        text_width = text_bbox[2] - text_bbox[0]
        x = img_width - text_width - 10
        y = 10  # 右上角位置
        draw.text((x, y), watermark_text, font=font, fill=font_color)
        new_filename = f"{filename[:-4]}_watermark.png"
        new_img_path = os.path.join(folder_path, new_filename)
        img.save(new_img_path)
        print(f"已保存: {new_filename}")

print("所有图片处理完成")

