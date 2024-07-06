def perform_operation(num1:float, num2:float , operation:str):
    for x in operation:
        if operation == "add":
            result = num1 + num2
            print(result)

        elif operation == "subtract":
            result = num1 - num2
            print(result)
        elif operation == "multiply":
            result = num1 * num2
            print(result)
        elif operation == "divide":
            if num2 == 0:
                print("Cannot divide")
            elif num2 > 0:
                result = num1 / num2
                print(result)
        return
    
