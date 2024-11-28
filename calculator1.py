# Calculator for multiple operations
print("Enter a mathematical expression (e.g., 1+2*2/3):")

# Take input from the user
expression = input()

try:
    # Evaluate the expression
    result = eval(expression)
    print("Result:", result)
except Exception as e:
    # Handle invalid input
    print("Invalid input:", e)
