import os

num1 = int(os.getenv("NUM1", 0))
num2 = int(os.getenv("NUM2", 0))

print("=== Calculator Script ===")
print(f"NUM1 = {num1}")
print(f"NUM2 = {num2}")

print("Addition       :", num1 + num2)
print("Subtraction    :", num1 - num2)
print("Multiplication :", num1 * num2)

if num2 != 0:
    print("Division       :", num1 / num2)
else:
    print("Division       : Cannot divide by zero")
