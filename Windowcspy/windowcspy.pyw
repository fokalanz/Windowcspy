import tkinter as tk
import ctypes
from ctypes import wintypes
import os

#适配于初级的窗口确认，包含进程、标题、类
# --- Windows API 准备 ---
user32 = ctypes.windll.user32
kernel32 = ctypes.windll.kernel32
PROCESS_QUERY_LIMITED_INFORMATION = 0x1000

def get_process_name(hwnd):
    pid = wintypes.DWORD()
    user32.GetWindowThreadProcessId(hwnd, ctypes.byref(pid))
    hProcess = kernel32.OpenProcess(PROCESS_QUERY_LIMITED_INFORMATION, False, pid)
    if hProcess:
        buffer = ctypes.create_unicode_buffer(260)
        size = wintypes.DWORD(260)
        if kernel32.QueryFullProcessImageNameW(hProcess, 0, buffer, ctypes.byref(size)):
            kernel32.CloseHandle(hProcess)
            return os.path.basename(buffer.value).lower()
        kernel32.CloseHandle(hProcess)
    return "未知"

def get_window_title(hwnd):
    length = user32.GetWindowTextLengthW(hwnd)
    if length > 0:
        buffer = ctypes.create_unicode_buffer(length + 1)
        user32.GetWindowTextW(hwnd, buffer, length + 1)
        return buffer.value
    return "无标题"

def get_class_name(hwnd):
    buffer = ctypes.create_unicode_buffer(256)
    user32.GetClassNameW(hwnd, buffer, 256)
    return buffer.value

# --- 图形界面主程序 ---
class WindowSpyApp:
    def __init__(self, root):
        self.root = root
        self.root.title("🕵️ Window Spy")
        self.root.geometry("380x180")
        
        # 核心特性：窗口永远置顶，且微微透明
        self.root.attributes("-topmost", True)
        self.root.attributes("-alpha", 0.95)
        
        self.is_paused = False
        
        # 界面布局设定
        self.root.configure(padx=15, pady=15)
        
        # 变量绑定
        self.var_process = tk.StringVar(value="等待抓取...")
        self.var_class = tk.StringVar(value="等待抓取...")
        self.var_title = tk.StringVar(value="等待抓取...")

        self.create_row("📦 进程名 (Process):", self.var_process, 0)
        self.create_row("🧬 窗口类 (Class):", self.var_class, 1)
        self.create_row("🏷️ 窗口标题 (Title):", self.var_title, 2)
        
        # 暂停/继续 按钮 (方便停下来复制)
        self.btn_pause = tk.Button(self.root, text="⏸️ 冻结本工具画面 (方便复制)", command=self.toggle_pause, relief="groove")
        self.btn_pause.grid(row=3, column=0, columnspan=2, pady=10, sticky="we")

        # 启动实时监控循环
        self.update_info()

    def create_row(self, label_text, text_var, row):
        """创建一个标签 + 可复制的只读输入框"""
        lbl = tk.Label(self.root, text=label_text, font=("Microsoft YaHei", 9, "bold"))
        lbl.grid(row=row, column=0, sticky="e", pady=5)
        
        # 使用 Entry 组件，设置 readonly，这样用户可以直接用鼠标划选并 Ctrl+C 复制
        entry = tk.Entry(self.root, textvariable=text_var, width=25, font=("Consolas", 10), state="readonly")
        entry.grid(row=row, column=1, sticky="w", padx=10, pady=5)

    def toggle_pause(self):
        self.is_paused = not self.is_paused
        if self.is_paused:
            self.btn_pause.config(text="▶️ 继续实时监控", fg="green")
        else:
            self.btn_pause.config(text="⏸️ 冻结画面 (方便复制)", fg="black")

    def update_info(self):
        if not self.is_paused:
            hwnd = user32.GetForegroundWindow()
            if hwnd != 0:
                self.var_process.set(get_process_name(hwnd))
                self.var_class.set(get_class_name(hwnd))
                self.var_title.set(get_window_title(hwnd))
                
        # 每 200 毫秒刷新一次
        self.root.after(200, self.update_info)

if __name__ == "__main__":
    root = tk.Tk()
    # 禁用窗口拉伸
    root.resizable(False, False)
    app = WindowSpyApp(root)
    root.mainloop()
