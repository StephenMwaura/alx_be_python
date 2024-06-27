Task = input("Input a task description: ")
Time_Bound = input("Is the time-bound (yes or no): ").strip().lower()
Priority = input("Is the task priority (high,medium,low):").strip().lower()
match Priority:
    case "high" | "medium" | "low":
        print("Reminder")
        if Time_Bound == "yes":
            print(f"{Task} is a {Priority} task that requires immediate action")
        elif Time_Bound == "no":
            print(f"{Task} is a {Priority} priority task.Consider completing it when you have free time." )
