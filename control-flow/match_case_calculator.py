num1 = int(input("Enter the first number:"))
num2 = int(input("Enter the second number:"))
operation = input("Choose the operation (+, -, *, /):")

result = None
match operation :
     case "+":
        result = num1 + num2
     case "-":
        result = num1 - num2
     case "*":
        result = num1 * num2
     case "/":
        if num2 != 0:
           result = num1 / num2
        else:
           print("Cannot divide by zero.")
     case _:
        print("Cannot divide zero")

if result is not None:
   print("The result is:", result)
