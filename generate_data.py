import os
import json

def generate_file_list():
    # 需要排除的文件夹
    exclude_dirs = {'.git', '.github', 'assets', '__pycache__'}
    # 结果字典
    file_system = {}

    # 遍历当前目录
    for item in os.listdir('.'):
        if os.path.isdir(item) and item not in exclude_dirs:
            # 获取该目录下所有的 html 文件
            html_files = [f for f in os.listdir(item) if f.endswith('.html')]
            if html_files:
                file_system[item] = sorted(html_files)

    # 将结果写入 data.json
    with open('data.json', 'w', encoding='utf-8') as f:
        json.dump(file_system, f, ensure_ascii=False, indent=2)
    
    print("Success: data.json has been generated.")

if __name__ == "__main__":
    generate_file_list()
