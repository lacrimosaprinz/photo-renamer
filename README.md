# Photo Renamer

自动将照片按**拍摄时间**重命名为 `IMG_YYYYMMDD_HHMMSS.jpg` 格式。

## 功能

- 优先读取照片 EXIF 中的拍摄时间
- 若无 EXIF，则使用文件修改时间
- 自动处理重名文件（添加序号后缀）
- 支持 JPG/JPEG/PNG 格式

## 安装

```bash
pip install Pillow
```

## 使用

```bash
python renamer.py /path/to/your/photo/folder
```

## 示例

```bash
python renamer.py ~/Pictures/Vacation
```

## 注意

- 请先备份重要照片！
- 脚本直接重命名原文件（不复制）
