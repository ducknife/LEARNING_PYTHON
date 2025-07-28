from datetime import datetime 
import json 

DUCKNIFE = "__main__"

DATASET = open('_DATASETS.json', 'r')
QUERYSET = open('_QUERYSETS.json', 'r')

def load_todos():
    return json.load(DATASET)

def load_query():
    return json.load(QUERYSET)

todos = load_todos()
queries = load_query()

def write_todos():
    f = open('_DATASETS.json', 'w')
    json.dump(todos, f, indent=4)

def write_query(query):
    f = open('_QUERYSETS.json', 'w')
    queries.append(query)
    json.dump(queries, f, indent=4)
    
def add_todo(task_name):
    f = open('_DATASETS.json', 'w')
    now = datetime.now().strftime("%Y-%m-%d")
    for task in todos:
        if task[0] == task_name:
            print("Task already exists.")
            return
    else:
        todos.append([task_name, now, False])
        write_todos()
    
def remove_todo(task_name):
    for task in todos:
        if task[0] == task_name:
            todos.remove(task)
            write_todos()
    else:
        print("Task not found in the list.")
        
def mark_done(task_name):
    for task in todos:
        f = open('_DATASETS.json', 'w')
        if task[0] == task_name: 
            task[2] = True  
            write_todos()   
            return
    else:
        print("Task not found in the list.")

def display_todos():
    for task in todos:
        status = "Done" if task[2] else "Not done"
        print(f'Task: {task[0]} Due:{task[1]}, Status: {status}')

def display_todos_in_range(start, end):
    if start < 0 or end > len(todos) or start > end:
        print('Invalid range.')
    else:
        print(f'Todos in range {start} to {end}: ')
        for i in range(start, end):
            print(todos[i])
        
def reverse_todos():
    todos.reverse()
    write_todos()
    display_todos()
        
def exit_program():
    print("Exiting the program. Goodbye!")
    exit()

def show_menu():
    print("Todo List Menu:")
    print("1. Add Todo")
    print("2. Remove Todo")
    print("3. Mark Todo as Done")
    print("4. Display Todos")
    print("5. Display Todos in a Range")
    print("6. Reverse Todos")
    print("7. Exit")
        
if __name__ == DUCKNIFE:
    query_nth = 0
    while True:
        show_menu()
        choice = int(input('Enter your choice (1-5): '))
        query_nth += 1
        time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        if choice == 1:
            task = input("Enter the task to add: ")
            add_todo(task)
            write_query(f'Query {query_nth}: ADD TASK {task} AT {time}')
        elif choice == 2:
            task = input("Enter the task to remove: ")
            remove_todo(task)
            write_query(f'Query {query_nth}: REMOVE TASK {task} AT {time}')
        elif choice == 3:
            task = input("Enter the task to mark as done: ")
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
        else:
            exit_program()
            write_query(f'Query {query_nth}: EXIT PROGRAM AT {time}')
        print()