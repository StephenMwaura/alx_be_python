task = input("Enter your task: ")

priority = input("Priority (high/medium/low):").lower()

time_bound = input("Is it time-bound? (yes / no): ").strip().lower()



match priority:
    case "high":
        reminder = (f"{task}Immediate attention to be taken.")
    case "medium" :
        reminder = (f"{task}Work on it as soon as possible.")
    case "low":
        reminder = (f"{task}Complete it during free time.")
    case _:
        print(f"{task}Invalid priority")

if time_bound == "yes":
    reminder = "requires immediate attention today!"
else :
    reminder = "." 

print(f"{reminder}")