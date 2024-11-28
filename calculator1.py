# Calculator for multiple operations
print("Enter a mathematical expression (e.g., 5+3-2*4/2):")

# Take input from the user
expression = input()

try:
    # Evaluate the expression
    result = eval(expression)
    print("Result:", result)
except Exception as e:
    # Handle invalid input
    print("Invalid input:", e)