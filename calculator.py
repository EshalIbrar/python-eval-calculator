# Simple CLI Calculator
# WARNING: Uses eval(). For educational purposes only.

print("Simple Calculator")
print("Enter a mathematical expression like: 5 + 3 * 2")

expression = input(">>> ")

try:
    result = eval(expression)
    print("Result:", result)
except:
    print("Invalid expression")
