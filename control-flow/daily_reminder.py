task = input("Enter your task: ")

time_bound = input("Is it time-bound? (yes / no): ").strip().lower()

priority = input("Priority (high/medium/low):").lower()

reminder = print(f"Finish {task} is a {priority} priority task. ")

if time_bound == "yes":
    reminder = "requires immediate attention today!"
else :
    reminder = "."


match priority:
    case "high":
        reminder = ("Immediate attention to be taken.")
    case "medium" :
        reminder = ("Work on it as soon as possible.")
    case "low":
        reminder = ("Complete it during free time.")
    case _:
        print("Invalid priority")

print(reminder)
