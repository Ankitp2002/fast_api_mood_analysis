import os
import sys
args = sys.argv[1::]


def create_init(path):
    # createfile init.py
    if not os.path.exists(path):
        with open(path, 'w') as f:
            f.write("# This is an auto-generated __init__.py file\n")


for dir in args:
    os.makedirs(f"./apis/{dir}/schema", exist_ok=True)
    create_init(f"./apis/{dir}/schema/__init__.py")
    os.makedirs(f"./apis/{dir}/views", exist_ok=True)
    create_init(f"./apis/{dir}/views/__init__.py")
    create_init(f"./apis/{dir}/models.py")
