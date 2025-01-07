def calculator(a, b, operation):
    if operation == "add":
        return a + b 
    elif operation == "subtract":
        return a - b
    elif operation == "multiply":
        return a + b 
    elif operation == "divide":
        return a / b if b != 0 else "Division by zero error"
    else:
        return "Invalid Operation"

a = int(input("Enter the first number"))
b = int(input("Enter the second number"))
operator = input("Enter the operation (add, subtract, multiply divide): ").lower()

result = calculator (a, b, operator)
print("Result:", result)