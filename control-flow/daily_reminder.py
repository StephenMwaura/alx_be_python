task = input("Enter your task: ")
priority = input("Priority (high/medium/low):").lower()
time_Bound = input("Is it time-bound (yes / no): ").lower()
reminder = print(f"Finish {task} is a {priority} priority task. ")
if time_Bound == "yes":
    print("requires attention.")
elif time_Bound == "no":
    print()


match priority:
    case "high":
        print ("Immediate attention to be taken.")
    case "medium" :
        print("Work on it as soon as possible.")
    case "low":
        print("Complete it during free time.")
    case _:
        print("Invalid priority")

reminder = print(f"Finish {task} is a {priority} priority task. ")
