我来帮你完成这三件事！让我为你的 Photo Renamer 项目打造完整的推广方案。

## 🚀 GitHub项目简介 - Photo Renamer

<div align="center">
  <h1>📸 Photo Renamer</h1>
  <p><strong>智能照片重命名神器 - 让每一张照片都有故事的时间戳</strong></p>

  [![Python](https://img.shields.io/badge/Python-3.7+-blue.svg)](https://www.python.org/downloads/)
  [![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
  [![Stars](https://img.shields.io/github/stars/lacrimosaprinz/photo-renamer?style=social)](https://github.com/lacrimosaprinz/photo-renamer)

  <p>
    <a href="#-features">✨ 特性</a> •
    <a href="#-quick-start">🚀 快速开始</a> •
    <a href="#-installation">📦 安装</a> •
    <a href="#-usage">📖 使用</a> •
    <a href="#-contributing">🤝 贡献</a>
  </p>
</div>

---

## ✨ 核心特性

<div align="center">
  <table>
    <tr>
      <td><b>🎯 智能识别</b></td>
      <td><b>⚡ 极速处理</b></td>
      <td><b>🎨 自定义格式</b></td>
    </tr>
    <tr>
      <td>自动读取EXIF时间戳</td>
      <td>批量处理上千张照片</td>
      <td>支持多种命名模板</td>
    </tr>
    <tr>
      <td><b>📱 多格式支持</b></td>
      <td><b>🔒 安全备份</b></td>
      <td><b>🌍 跨平台</b></td>
    </tr>
    <tr>
      <td>JPG/PNG/HEIC/RAW</td>
      <td>自动备份原文件</td>
      <td>Windows/Mac/Linux</td>
    </tr>
  </table>
</div>

## 🎯 为什么选择 Photo Renamer？

告别混乱的文件名！告别手动重命名的痛苦！Photo Renamer 让你的照片管理变得如此简单：

- **📅 时间轴整理**：按拍摄时间自动重命名，完美还原生活轨迹
- **🎭 智能识别**：即使文件名被修改，也能从EXIF数据找回真实时间
- **⚡ 批量处理**：一键处理整个文件夹，支持子目录递归
- **🎨 个性化命名**：支持自定义格式，如 `2024-03-15_15-30-25_IMG_001.jpg`
- **🔐 零风险操作**：自动备份，可一键恢复原文件名

## 🚀 快速开始

### 📦 安装

```bash
# 克隆项目
git clone https://github.com/lacrimosaprinz/photo-renamer.git
cd photo-renamer

# 安装依赖
pip install -r requirements.txt

# 直接运行
python photo_renamer.py --help
```

### 🎯 一键使用

```bash
# 基础使用 - 重命名当前目录所有照片
python photo_renamer.py

# 指定目录
python photo_renamer.py /path/to/photos

# 自定义格式
python photo_renamer.py --format "%Y-%m-%d_%H-%M-%S" --backup

# 包含子目录
python photo_renamer.py --recursive --backup
```

## 📖 使用示例

### 🎨 命名格式模板

支持丰富的命名格式：
```bash
# 默认格式：20240315_153025.jpg
python photo_renamer.py

# 详细格式：2024-03-15_15-30-25_IMG_001.jpg
python photo_renamer.py --format "%Y-%m-%d_%H-%M-%S_IMG_{counter:03d}"

# 包含相机型号：20240315_153025_iPhone12.jpg
python photo_renamer.py --format "%Y%m%d_%H%M%S_{camera}"
```

### 🔧 高级功能

```bash
# 处理特定格式
python photo_renamer.py --formats jpg,png,heic

# 保留原文件备份
python photo_renamer.py --backup --backup-dir ./backup

# 模拟运行（预览效果）
python photo_renamer.py --dry-run

# 详细日志
python photo_renamer.py --verbose
```

## 🛠️ 技术栈

- **Python 3.7+** - 核心语言
- **Pillow** - 图像处理与EXIF读取
- **exifread** - EXIF数据解析
- **click** - 命令行界面
- **tqdm** - 进度条显示


## 🤝 贡献指南

欢迎贡献！请查看 [CONTRIBUTING.md](CONTRIBUTING.md) 了解如何参与。

### 🌟 贡献者

感谢所有贡献者！你们的支持让这个项目变得更好。

<a href=\"https://github.com/lacrimosaprinz/photo-renamer/graphs/contributors\">\n  <img src=\"https://contrib.rocks/image?repo=lacrimosaprinz/photo-renamer\" />\n</a>

---

## 📄 许可证

本项目基于 [MIT License](LICENSE) 开源，可自由使用和修改。

---

## 💬 支持

- 🐛 [报告问题](https://github.com/lacrimosaprinz/photo-renamer/issues)
- 💡 [功能建议](https://github.com/lacrimosaprinz/photo-renamer/discussions)
- 📧 联系：lacrimosaprinz@gmail.com
