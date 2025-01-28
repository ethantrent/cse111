# Create a program that allows the user to manage a list of tasks.
# menu 1=add/2=remove/3=edit/4=change order/5=show tasks list/6=quit
# each task is numbered starting from 1.
 
# Instructions:
# 1. Create a list named 'tasks' with some initial tasks.
# 2. Ask the user what action they want to perform: add a task, remove a task, edit, change task order, show list, or quit.
# 3. If 'add', prompt for the task description and add it to the end of the list.
# 4. If 'remove', prompt for the task number and remove the corresponding task.
# 5. If 'edit', prompt for the task number and the new task content.
# 6. If 'change order', prompt for the current task number and the new position number, then move the task.
# 7. if 'show tasks list', display the list with each task numbered.
# 8. Repeat the process until the user decides to quit the program.
# 9. When the user quits, thanks the user for using your program.


# 1. Create a list named 'tasks' with some initial tasks.
tasks = ['run','eat','read']
# 2. Ask the user what action they want to perform: add a task, remove a task, edit, change task order, show list, or quit.
action = ''

print ('Welcome to the Task Manager Program!')
while action != 6:
    action = int(input('\nWhat action do you want to perform? \n1 = Add\n2 = Remove\n3 = Edit\n4 = Change order\n5 = Show tasks list\n6 = Quit \nPlease enter a number: '))
    # 3. If 'add', prompt for the task description and add it to the end of the list.
    if action == 1:
        task = input('\nEnter the task description: ')
        tasks.append(task)
        print (f"'{task}' has been added to the list ")
    # 4. If 'remove', prompt for the task number and remove the corresponding task.
    elif action == 2:
        task_number = int(input('\nEnter the task number: '))
        tasks.pop(task_number - 1)
        print (f'Task number {task_number} has been removed from the list ')
    # 5. If 'edit', prompt for the task number and the new task content.
    elif action == 3:
        task_number = int(input('\nEnter the task number: '))
        task = input('\nEnter the new task description: ')
        tasks[task_number - 1] = task
        print (f'Task number {task_number} has been updated ')
    # 6. If 'change order', prompt for the current task number and the new position number, then move the task.
    elif action == 4:
        task_number = int(input('\nEnter the task number: '))
        new_position = int(input('\nEnter the new position: '))
        task = tasks.pop(task_number - 1)
        tasks.insert(new_position - 1, task)
        print (f'Task number {task_number} has been moved to position {new_position} ')
    # 7. if 'show tasks list', display the list with each task numbered.
    elif action == 5:
        print('Tasks:')
        for i in range(len(tasks)):
            print(f'{i + 1}. {tasks[i]}')
    # 8. Repeat the process until the user decides to quit the program.
    elif action == 6:
        print('Thank you for using the Task Manager Program!')
        break

    else:
        print('Invalid option. Please try again.')