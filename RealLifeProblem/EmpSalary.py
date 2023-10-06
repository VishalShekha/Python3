'''
Problem Statement: Calculating Employee Salary Based on Task Completion.

You are given a list of employees, along with their base salaries,
and a list of tasks assigned to each employee. Each task has
a completion status ("complete" or "incomplete") and a deadline date.
Based on the completion status and timeliness of the tasks,
you need to calculate and print the total salary for each employee.

Implement the following rules for salary calculation:
1. If all tasks are completed on time, the employee receives 100% of their base salary.
2. If all tasks are completed, but not all were completed on time, the employee receives 50% of their base salary.
3. If there are incomplete tasks, regardless of their completion status, the employee receives 10% of their base salary.

Algorithm:
1. Initialise a list of employees with their names, base salaries, and lists of tasks.
2. For each employee, iterate through their tasks and check the completion status and deadline.
3. Calculate the total salary based on the defined rules.
4. Print the employee's name and total salary.
'''
#Python Program:



employees = [
    ["XXX", 5000, [("Task 1", "complete", "2023-08-15"), ("Task 2", "incomplete", "2023-08-12")]],
    ["YYY", 6000, [("Task 1", "complete", "2023-08-10"), ("Task 2", "complete", "2023-08-14")]],
    ["ZZZ", 4500, [("Task 1", "incomplete", "2023-08-12"), ("Task 2", "incomplete", "2023-08-14")]],
]
#loop employee
for employee in employees:
    name , base_salary , task = employee
    all_task_complete = True
    any_task_incomplete = False
    total_salary = base_salary
    deadline = '2023-08-14'
    
    #loop tasks
    for task , status , submitted_date in task:
        if status == "incomplete":
            all_task_complete = False
            any_task_incomplete = True
        if status == "complete" and submitted_date > deadline :
            total_salary *= 0.5
    
    if all_task_complete:
        total_salary = str(total_salary)
        print(name+"'s salary is "+total_salary)
    elif any_task_incomplete:
        total_salary*=0.5
        total_salary = str(total_salary)
        print(name+"'s salary is "+total_salary)
    else:
        total_salary*=0.1
        total_salary = str(total_salary)
        print(name+"'s salary is "+total_salary)