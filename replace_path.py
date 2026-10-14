import os
# ---- Cấu hình ----
old_path = "/home/chienle"   	#máy của thằng build
new_path = "/home/haibotlab"		#máy của tao
workspace_root = "/home/haibotlab/nav2_ws"  # Khu vực tìm kiếm path để đổi tên

def replace_in_file(filepath, old_path, new_path):
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()
        if old_path in content:
            content = content.replace(old_path, new_path)
            with open(filepath, "w", encoding="utf-8") as f:
                f.write(content)
            print(f"[✓] Updated: {filepath}")
    except (UnicodeDecodeError, PermissionError):
        # Skip binary files or permission errors
        pass

def walk_and_replace(workspace_root, old_path, new_path):
    for root, _, files in os.walk(workspace_root):
        for file in files:
            filepath = os.path.join(root, file)
            replace_in_file(filepath, old_path, new_path)

if __name__ == "__main__":
    print("🔍 Starting path replacement...")
    walk_and_replace(workspace_root, old_path, new_path)
    print("✅ Done.") 
