"""
Python_Learn —— Python 自学项目入口

使用方式：
    python main.py          # 运行交互式菜单
    python main.py --help   # 查看帮助

本仓库记录了从零学习 Python 的完整历程，包含：
  - Code/OnlieTask/   在线直播课作业
  - Code/TaskFile/    教材课后习题
  - Code/TestFile/    日常代码测试
  - Note/write_note/  学习笔记
"""

import sys
import subprocess
import os


def show_menu():
    """显示项目功能选择菜单"""
    menu = """
╔══════════════════════════════════════╗
║      Python 自学项目 · 启动菜单       ║
╠══════════════════════════════════════╣
║  1. 🎁  年会抽奖系统                  ║
║  2. 🃏  扑克牌比大小                  ║
║  3. ✖️  九九乘法表                    ║
║  4. 🐢  Turtle 绘图                  ║
║  5. 🌐  网页下载工具（Selenium）      ║
║  6. 🤖  通义千问 API 调用             ║
║  0. 🚪  退出                         ║
╚══════════════════════════════════════╝
请选择 (0-6): """
    return input(menu)


def run_script(relative_path):
    """运行指定路径的 Python 脚本"""
    script_path = os.path.join(os.path.dirname(__file__), relative_path)
    if os.path.exists(script_path):
        print(f"\n▶ 正在运行: {relative_path}\n")
        subprocess.run([sys.executable, script_path])
    else:
        print(f"❌ 文件不存在: {script_path}")


def main():
    """主入口函数"""
    scripts = {
        "1": ("Code/TestFile/Day_stu_file.py", "年会抽奖系统"),
        "2": ("Code/TestFile/pokerank.py", "扑克牌比大小"),
        "3": ("Code/TestFile/chengfa.py", "九九乘法表"),
        "4": ("Code/TaskFile/2unit/01.py", "Turtle 绘图"),
        "5": ("Code/TestFile/filketx.py", "Selenium 网页下载"),
        "6": ("Code/TestFile/ainle.py", "通义千问 API 调用"),
    }

    while True:
        choice = show_menu()
        if choice == "0":
            print("👋 再见！继续加油学习 Python！")
            break
        elif choice in scripts:
            path, desc = scripts[choice]
            print(f"\n📌 启动: {desc}")
            run_script(path)
            input("\n按 Enter 键继续...")
        else:
            print("⚠️ 无效选择，请重新输入。")


if __name__ == "__main__":
    if "--help" in sys.argv or "-h" in sys.argv:
        print(__doc__)
    else:
        main()
