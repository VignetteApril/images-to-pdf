import argparse
from PIL import Image
import os
import re
from datetime import datetime

def natural_sort_key(s):
    """自然排序键函数，用于处理文件名中的数字"""
    return [
        int(part) if part.isdigit() else part.lower()
        for part in re.split(r'(\d+)', s)
    ]

def main():
    # 解析命令行参数
    parser = argparse.ArgumentParser(description='将多个图片合并为PDF')
    parser.add_argument('input_dir', type=str, help='图片所在目录')
    parser.add_argument('-o', '--output', type=str, default='output.pdf', help='输出文件名（默认：output.pdf）')
    parser.add_argument('-e', '--ext', type=str, default='jpg', help='图片扩展名，多个用逗号分隔（默认：jpg）')
    parser.add_argument('--sort-by', choices=['name', 'mtime'], default='name',
                       help='排序方式：name=文件名排序 | mtime=修改时间排序（默认：name）')
    
    args = parser.parse_args()

    try:
        # 验证输入目录
        if not os.path.isdir(args.input_dir):
            raise ValueError(f"目录不存在：{args.input_dir}")

        # 获取支持的图片格式列表
        extensions = [ext.strip().lower() for ext in args.ext.split(',')]
        valid_extensions = {ext for ext in extensions if ext in {'jpg', 'jpeg', 'png', 'bmp', 'webp', 'tiff'}}

        # 收集所有符合条件的图片文件
        images = []
        for f in os.listdir(args.input_dir):
            file_ext = os.path.splitext(f)[1][1:].lower()
            if file_ext in valid_extensions:
                images.append(os.path.join(args.input_dir, f))

        if not images:
            raise ValueError(f"未找到支持的图片文件（扩展名：{', '.join(valid_extensions)}）")

        # 文件排序逻辑
        if args.sort_by == 'name':
            images.sort(key=lambda x: natural_sort_key(os.path.basename(x)))
        elif args.sort_by == 'mtime':
            images.sort(key=lambda x: os.path.getmtime(x))

        # 转换并保存为PDF
        pdf_images = []
        for idx, img_path in enumerate(images):
            with Image.open(img_path) as img:
                # 转换图片模式为RGB（PDF需要）
                if img.mode in ('RGBA', 'LA'):
                    img = img.convert('RGB')
                elif img.mode != 'RGB':
                    img = img.convert('RGB')
                pdf_images.append(img)

        # 保存PDF文件
        if pdf_images:
            first_image = pdf_images[0]
            first_image.save(
                args.output,
                save_all=True,
                append_images=pdf_images[1:],
                resolution=200.0,   # 设置DPI
                quality=95         # 图像质量（1-100）
            )
            print(f"成功生成 {len(pdf_images)} 页PDF文件：{os.path.abspath(args.output)}")
            
    except Exception as e:
        print(f"错误发生：{str(e)}")
        exit(1)

if __name__ == '__main__':
    main()
