import os

username = os.getenv("USERNAME", "Guest")
city = os.getenv("CITY", "Unknown")

print("=== Greeting Script ===")
print(f"Hello {username} from {city}!")
