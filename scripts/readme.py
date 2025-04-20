"""
**{fir_name}**

* [ ] [{file_name}}](https://github.com/LIghtJUNction/Napcat-PythonSDK/blob/main/{file_path 例如 src/napcat/api/account/set_qq_avatar.py})

"""
from pathlib import Path

api = Path(__file__).parent.parent / "src" / "napcat" / "api" 
output = Path(__file__).parent / "output.md"

def generate_readme(path: Path):
    for dir in path.iterdir():
        if dir.is_dir() and dir.name != "__pycache__":
            with open(output, "a", encoding="utf-8") as f:
                f.write(f"** {dir.name} **\n")
            generate_readme(dir)
        if dir.is_file() and dir.name.endswith(".py"):
            with open(output, "a", encoding="utf-8") as f:
                f.write(f"* [ ] [{dir.name}](https://github.com/LIghtJUNction/Napcat-PythonSDK/blob/main/{dir.relative_to(api).as_posix()})\n")

generate_readme(api)