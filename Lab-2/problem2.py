# Lab 02 - Problem 2: Overview of Coding Environments

environments = {
    "IDLE": "Default lightweight IDE bundled with Python.",
    "Google Colab": "Cloud-based Jupyter notebook environment by Google with free GPU access.",
    "Jupyter Notebook": "Web-based interactive environment for writing notebooks with markdown and code.",
    "PyCharm": "Feature-rich professional IDE by JetBrains with advanced debugging.",
    "Spyder": "Scientific environment designed for data science and numerical computing."
}

print("=== Python Development Environments ===")
for name, description in environments.items():
    print(f"\n[{name}]")
    print(f"  Description: {description}")