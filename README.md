# Windowcspy
基于Python制作的一个小工具，用来捕获窗口的标题名、进程名、类名

## 📖 简介 (Introduction)
**WinInfo Catcher** 是一个简洁的实用程序，旨在帮助开发者快速获取当前活动窗口的元数据。无论你是在编写自动化脚本、调试 GUI 程序，还是进行系统分析，它都能为你提供帮助。

## ✨ 功能特性 (Features)
* **实时捕获**：快速锁定目标窗口。
* **信息全面**：同时提取以下三个关键属性：
    * **进程名 (Process Name)**：定位后台运行的可执行文件。
    * **类名 (Window Class)**：用于 Win32 API 调用或自动化识别。
    * **标题 (Window Title)**：窗口显示的文本内容。
* **无需环境**：提供已打包好的 `.exe` 文件，开箱即用。

## 🚀 快速开始 (Quick Start)

### 方案 A：直接运行（推荐）
1. 前往 [Releases](https://github.com/fokalanz/Windowcspy/releases/tag/windowspy) 页面。
2. 下载最新版本的 `xxx.exe`。
3. 双击运行即可开始捕获。

### 方案 B：源码运行
如果你想自行编译或修改：
本项目的 `Windowcspy/windowcspy.pyw` 即为你需要的源码，可自行复制、下载使用
