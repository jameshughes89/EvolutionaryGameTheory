import subprocess


def main():
    for tool in ["isort .", "black .", "mdformat .", "flake8 src test scripts", "mdformat --check src test *.md"]:
        print(f"running `{tool}`")
        subprocess.run(tool, shell=True)
