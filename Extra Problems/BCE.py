

#Employee data: [name, base_salary, [task1, task2, ...]]
employees = [
    ["XXX", 5000, [["Task 1", "complete", "2023-08-15"], ("Task 2", "incomplete", "2023-08-12")]],
    ["YYY", 6000, [("Task 1", "complete", "2023-08-10"), ("Task 2", "complete", "2023-08-14")]],
    ["ZZZ", 4500, [("Task 1", "incomplete", "2023-08-12"), ("Task 2", "incomplete", "2023-08-14")]],
]

# For looping through employees
for employee in employees:
    name, base_salary, tasks = employee
    total_salary = base_salary
    
    all_tasks_complete = True
    any_task_incomplete = False
    deadline = "2023-08-14"
    # For looping through tasks for the employee
    for task, status, submitted_date in tasks:
        if status == "incomplete":
            all_tasks_complete = False
            any_task_incomplete = True
        if status == "complete" and submitted_date > deadline:
            total_salary *= 0.5
    
    if all_tasks_complete:
        print("{}'s total salary: {}".format(name, total_salary))
    elif any_task_incomplete:
        total_salary *= 0.5
        print(name,"\b's total salary:",total_salary)
    else:
        print(f"{name}'s total salary: {total_salary * 0.1}")