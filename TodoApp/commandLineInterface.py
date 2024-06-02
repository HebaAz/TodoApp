from App1.TodoApp.functions import get_todos, set_todos

import time

now = time.strftime(f"%b %d, %Y - %H:%M:%S")
print(now)

while True:
    #present user with the prompt msg and save their input in 'todo1'
    user_action = input("add, show (s), mark as complete (c), or edit (e)? (or x to exit) along with the relevant to-do: ")
    user_action = user_action.strip()

    if user_action.startswith("add") or user_action.startswith("new"):
        todo = user_action[4: ]

        #open file in read mode, then store the contents as a list
        todos = get_todos()
        todos.append(todo + '\n')

        set_todos(todos)

    elif user_action.startswith("show"):
        todos = get_todos()

        for i, item in enumerate(todos):
            item = item.strip("\n") #Overwrite oeration to remove \n
            output = f"{i + 1}-{item.title()}"
            print(output)

    elif user_action.startswith("edit"):
        try:
            print(todos)
            #get index number from user but since all input is a string, muct convert it to int
            number = int(input("Enter the number of the task you would like to edit: "))
            #to adjust for index starting at 0
            number = number - 1

            #get existing list of todos
            todos = get_todos()

            #get new input
            new_todo = input("Enter a new task: ")
            todos[number] = new_todo + '\n'
            print(todos)

            set_todos(todos)

        except ValueError:
            print("Enter the index!")
            continue

    elif user_action.startswith("complete"):
        try:
            number = int(user_action[9: ])
            
            todos = get_todos()
            
            todo_to_remove = todos[number - 1].strip('\n')
            todos.pop(number - 1)

            set_todos(todos)

            message = f"The task {todo_to_remove} was removed from the list"
            print(message)

        except IndexError:
            print("There is no item with that index!")
            continue

    elif user_action.startswith("exit"):
        break

    else:
        print('Command is not valid!')

print("Bye!")