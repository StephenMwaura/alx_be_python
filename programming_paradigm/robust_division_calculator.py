def safe_divide(numerator, denominator):
    try:
        numerator = float(numerator)
        denominator = float(denominator)
        if denominator != 0:
            result =numerator / denominator
            return f"The result of the division is {result}"
        else:
            return f"Error: Cannot divide by zero."
    except ValueError:
        print("Error: Please enter numeric values only.")

    
print(safe_divide(numerator="", denominator=""))
    