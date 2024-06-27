task = input("Input a task description: ")
priority = input("Is the task priority (high,medium,low):")
time_bound = input("Is the time-bound (yes or no): ")
match priority:
    case "high" | "medium" | "low":
        print("Reminder")
        if time_bound == "yes":
            print(f"{task} is a {priority} task that requires immediate action")
        elif time_bound == "no":
            print(f"{task} is a {priority} priority task.Consider completing it when you have free time." )