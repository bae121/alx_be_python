#User's task details
task = input("Enter your task: ")
priority = input("Enter the task priority (high/medium/low): ").lower()
time_bound = input("Is the task time-bound? (yes/no): ").lower()

# Task with match-case
match priority:
    case "high":
        if time_bound == "yes":
            print(f"Reminder: '{task}' is a HIGH priority task. This requires immediate attention today!")
        else:
            print(f"Reminder: '{task}' is a HIGH priority task.")

    case "medium":
        if time_bound == "yes":
            print(f"Reminder: '{task}' is a MEDIUM priority task. This requires immediate attention today!")
        else:
            print(f"Reminder: '{task}' is a MEDIUM priority task.")

    case "low":
        if time_bound == "yes":
            print(f"Reminder: '{task}' is a LOW priority task. This requires immediate attention today!")
        else:
            print(f"Reminder: '{task}' is a LOW priority task.")

    case _:
        print(f"Reminder: '{task}' has an UNKNOWN priority.")
