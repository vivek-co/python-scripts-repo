import platform
import os

print("=== System Information ===")
print("Operating System :", platform.system())
print("Machine          :", platform.machine())
print("Python Version   :", platform.python_version())
print("Working Directory:", os.getcwd())
