import os

# 固定 CDN 前缀（不用改）
CDN_BASE = "https://cdn.jsdelivr.net/gh/abby-qi/network-engineering-img@main/"

# 你本地图片仓库的根目录（脚本就放在这个文件夹里，所以直接用当前目录）
ROOT_DIR = os.getcwd()

# 要识别的图片格式
IMG_EXTS = (".png", ".jpg", ".jpeg", ".webp", ".svg")

# 保存所有链接
all_links = []

for root, dirs, files in os.walk(ROOT_DIR):
    for file in files:
        # 只处理图片
        if file.lower().endswith(IMG_EXTS):
            # 得到相对路径
            abs_path = os.path.join(root, file)
            rel_path = os.path.relpath(abs_path, ROOT_DIR)
            # Windows 路径转 URL 路径
            rel_path = rel_path.replace("\\", "/")
            # 拼接最终链接
            url = CDN_BASE + rel_path
            # 记录
            all_links.append(f"{file} → {url}")

# 写入文件
with open("images_links.txt", "w", encoding="utf-8") as f:
    f.write("\n".join(all_links))

print(f"✅ 生成完成！共 {len(all_links)} 张图片链接")
print("📄 已保存到：images_links.txt")