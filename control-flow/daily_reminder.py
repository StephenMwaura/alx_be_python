Task = input("Input a task description: ")
Time_Bound = input("Is the time-bound (yes or no): ")
Priority = input("Is the task priority (high,medium,low):")

match Priority:
    case "high" | "medium" | "low":
        print("Reminder")
        if Time_Bound == "yes":
            print(f"{task} is a {priority} task that requires immediate action")
        elif Time_Bound == "no":
            print(f"{task} is a {priority} priority task.Consider completing it when you have free time." )
