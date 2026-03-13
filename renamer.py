import os
import sys
from datetime import datetime
from PIL import Image
from PIL.ExifTags import TAGS

def get_photo_date(filepath):
    """从照片 EXIF 中提取拍摄时间，若无则用文件修改时间"""
    try:
        image = Image.open(filepath)
        exifdata = image.getexif()
        if exifdata is not None:
            for tag_id, value in exifdata.items():
                tag = TAGS.get(tag_id, tag_id)
                if tag == "DateTimeOriginal":
                    # EXIF 时间格式: "2024:05:17 14:30:22"
                    dt = datetime.strptime(value, "%Y:%m:%d %H:%M:%S")
                    return dt
    except Exception as e:
        print(f"读取 {filepath} 的 EXIF 失败: {e}")

    # 回退到文件修改时间
    mtime = os.path.getmtime(filepath)
    return datetime.fromtimestamp(mtime)

def rename_photos(folder_path):
    """重命名指定文件夹中的照片"""
    if not os.path.isdir(folder_path):
        print(f"错误: {folder_path} 不是一个有效文件夹！")
        return

    # 支持的图片格式
    extensions = ('.jpg', '.jpeg', '.png', '.JPG', '.JPEG', '.PNG')
    files = [f for f in os.listdir(folder_path)
             if f.lower().endswith(extensions)]

    if not files:
        print("该文件夹中没有找到 JPG/PNG 照片。")
        return

    renamed_count = 0
    for filename in sorted(files):
        old_path = os.path.join(folder_path, filename)
        try:
            # 获取拍摄时间
            dt = get_photo_date(old_path)
            new_name = f"IMG_{dt.strftime('%Y%m%d_%H%M%S')}{os.path.splitext(filename)[1].lower()}"
            new_path = os.path.join(folder_path, new_name)

            # 避免重名（加序号）
            counter = 1
            while os.path.exists(new_path):
                name, ext = os.path.splitext(new_name)
                new_name = f"{name}_{counter}{ext}"
                new_path = os.path.join(folder_path, new_name)
                counter += 1

            # 重命名
            os.rename(old_path, new_path)
            print(f"✅ {filename} → {new_name}")
            renamed_count += 1

        except Exception as e:
            print(f"❌ 重命名 {filename} 失败: {e}")

    print(f"\n🎉 完成！共重命名 {renamed_count} 张照片。")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("用法: python renamer.py <照片文件夹路径>")
        print("示例: python renamer.py ~/Pictures/Vacation")
        sys.exit(1)

    folder = sys.argv[1]
    rename_photos(folder)
