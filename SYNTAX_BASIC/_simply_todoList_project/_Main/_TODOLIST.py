from datetime import datetime 
import json 
import os

#prepare data start
DATASET_PATH = os.path.join(os.path.dirname(__file__), '../_DATASETS.json') 
QUERYSET_PATH = os.path.join(os.path.dirname(__file__), '../_QUERYSETS.json')

DATASET = open(DATASET_PATH, 'r')
QUERYSET = open(QUERYSET_PATH, 'r')

DUCKNIFE = "__main__"

def load_todos():
    return json.load(DATASET)

def load_query():
    return json.load(QUERYSET)

todos = load_todos()
queries = load_query()
#prepare data end

#todos operations start
def write_todos():
    f = open(DATASET_PATH, 'w')
    json.dump(todos, f, indent=4, ensure_ascii=False, default=str)
    f.close()

def write_query(query):
    f = open(QUERYSET_PATH, 'w')
    queries.append(query)
    json.dump(queries, f, indent=4, ensure_ascii=False, default=str)
    f.close()
    
def standard_task_name(task):
    tmp = task.strip().split()
    res = ''
    for idx in range(len(tmp) - 1):
        res += tmp[idx].capitalize() + ' '
    res += tmp[-1]
    return res
    
def add_todo(task_name):
    f = open(DATASET_PATH, 'w')
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    for task in todos:
        if task[0] == task_name:
            print("Task already exists.")
            f.close()
            return
    else:
        todos.append([task_name, now, False])
        write_todos()
    
def remove_todo(task_name):
    for task in todos:
        if task[0] == task_name:
            todos.remove(task)
            write_todos()
            return
    else:
        print("Task not found in the list.")
        
def mark_done(task_name):
    for task in todos:
        f = open(DATASET_PATH, 'w')
        if task[0] == task_name: 
            task[2] = True  
            write_todos()   
            f.close()
            return
    else:
        print("Task not found in the list.")

def display_todos():
    print("Tasks in Todolist: \n")
    for task in todos:
        status = "Done" if task[2] else "Not done"
        print(f'\tTask: {task[0]}, Due:{task[1]}, Status: {status}')

def display_todos_in_range(start, end):
    if start < 0 or end > len(todos) or start > end:
        print('Invalid range.')
    else:
        print(f'Todos in range {start} to {end}: ')
        for i in range(start, end):
            print(todos[i])
            
def display_tasks_done():
    tasks_done = list(filter(lambda x : x[2] == True, todos))
    if len(tasks_done):
        print("Tasks has been done: \n")
        for task in tasks_done:
            print(f'\tTask: {task[0]}, Due:{task[1]}')
        return
    else:
        print("No task has been done yet.")
        
def display_tasks_not_done():
    tasks_not_done = list(filter(lambda x : x[2] == False, todos))
    if len(tasks_not_done):
        print("Tasks has not been done: \n")
        for task in tasks_not_done:
            print(f'\tTask: {task[0]}, Due:{task[1]}')
        return
    else:
        print("All tasks have been done yet.")
        
def reverse_todos():
    todos.reverse()
    write_todos()
    display_todos()
        
def exit_program():
    print("Exiting the program. Goodbye!")
    exit()
#todos operations end

#menu start
def show_menu():
    print("Todo List Menu:")
    print("1. Add Todo")
    print("2. Remove Todo")
    print("3. Mark Todo as Done")
    print("4. Display Todos")
    print("5. Display Todos in a Range")
    print("6. Reverse Todos")
    print("7. Display Tasks Done")
    print("8. Dispplay Tasks Not Done")
    print("9. Exit")
#menu end

#main start
if __name__ == DUCKNIFE:
    query_nth = 0
    timezone = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    write_query(f'PROGRAM STARTED AT {timezone}')
    while True:
        show_menu()
        choice = int(input('Enter your choice (1-9): '))
        query_nth += 1
        time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        if choice == 1:
            task = standard_task_name(input("Enter the task to add: "))
            add_todo(task)
            write_query(f'Query {query_nth}: ADD TASK {task} AT {time}')
        elif choice == 2:
            task = standard_task_name(input("Enter the task to remove: "))
            remove_todo(task)
            write_query(f'Query {query_nth}: REMOVE TASK {task} AT {time}')
        elif choice == 3:
            task = standard_task_name(input("Enter the task to mark as done: "))
            mark_done(task)
            write_query(f'Query {query_nth}: MARK DONE TASK {task} AT {time}')
        elif choice == 4:
            display_todos() 
            write_query(f'Query {query_nth}: DISPLAY TASKS AT {time}')
        elif choice == 5:
            start = int(input("Enter start index: "))
            end = int(input("Enter end index: "))
            display_todos_in_range(start, end)
            write_query(f'Query {query_nth}: DISPLAY TASKS FROM {start} TO {end} AT {time}')
        elif choice == 6:
            reverse_todos()
            write_query(f'Query {query_nth}: REVERSE TASKS AT {time}')
        elif choice == 7:
            display_tasks_done()
            write_query(f'Query {query_nth}: DISPLAY TASKS DONE AT {time}')
        elif choice == 8:
            display_tasks_not_done()
            write_query(f'Query {query_nth}: DISPLAY TASKS NOT DONE AT {time}')
        else:
            write_query(f'------------Time Exit: {time}------------ ')
            exit_program()
            write_query(f'Query {query_nth}: EXIT PROGRAM AT {time}')
        print()
        DATASET.close()
        QUERYSET.close()
#main end