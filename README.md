# Replace-path
A Python script to replace hardcoded absolute file paths in a ROS2/Nav2 workspace.

---

## Tutorial 

1. Open the script (`replace_paths.py` or your script name) and configure the paths at the top:
```python
old_path = "/home/old_user"          # Original path to replace 
new_path = "/home/your_user"          # Your new path
workspace_root = "/home/your_user/workspace_name"  # Path to your workspace
```

2. Run the script
```bash
python3 replace_path.py
```

