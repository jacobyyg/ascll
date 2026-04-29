import pyfiglet

def generate_ascii_art(text, font="slant"):
    """
    常用字体: 'slant', 'banner3-D', 'block', 'bubble', 'digital', 'shadow'
    """
    try:
        # 创建 Figlet 对象
        result = pyfiglet.figlet_format(text, font=font)
        print(f"--- 字体风格: {font} ---")
        print(result)
        
        # 也可以保存到文件，方便粘贴到 GitHub
        with open("ascii_art.txt", "w", encoding="utf-8") as f:
            f.write(result)
        print("✅ 艺术字已保存至 ascii_art.txt")
        
    except Exception as e:
        print(f"❌ 生成失败: {e}")

if __name__ == "__main__":
    user_input = input("请输入要转换的英文单词: ") or "DEV BOX"
    # 你可以尝试更换 font 参数来改变风格
    generate_ascii_art(user_input, font="slant")
