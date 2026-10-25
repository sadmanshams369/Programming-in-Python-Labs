# Lab 02 - Problem 1: Installation & Version Demonstration
import platform
import sys

print("=== Python Installation & System Info ===")
print("Python Version  :", platform.python_version())
print("Executable Path :", sys.executable)
print("Operating System:", platform.system(), platform.release())
print("=========================================")
print("Python installation verified successfully!")