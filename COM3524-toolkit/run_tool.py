import subprocess
import sys
from pathlib import Path

TOOLS = {
    "1": Path("GA_Teaching_Tool/teaching_tool.py"),
    "2": Path("ACO_Teaching_Tool/antsp/app.py"),
    "3": Path("CAPyle_releaseV2/release/main.py")
}

print("\nSelect a tool to run:")
print("1. GA Teaching Tool")
print("2. ACO Ants Tool")
print("3. CAPyle Tool")

choice = input("Enter 1, 2, or 3: ").strip()
print(f"You entered: {choice}")

script = TOOLS.get(choice)

if not script or not script.exists():
    print("Invalid selection or script not found.")
    sys.exit(1)

try:
    subprocess.run([sys.executable, str(script)], check=True)
except subprocess.CalledProcessError as e:
    print(f"An error occurred while running the script: {e}")
#subprocess.run([sys.executable, str(script)], check=True)
