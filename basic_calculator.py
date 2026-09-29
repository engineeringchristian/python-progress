operator = input("Enter an operator(+ - * /): ")
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

if operator == "+":
    result = num1 + num2
    action = "sum"
elif operator == "-":
    result = num1 - num2
    action = "difference"
elif operator == "*":
    result = num1 * num2
    action = "product"
elif operator == "/":
    result = num1 / num2
    action = "quotient"
else:
    print("Calculation couldn't be performed")
    exit()

print(f"The {action} is {result:.2f}")
