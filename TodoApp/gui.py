import functions
import FreeSimpleGUI as sg
import time

sg.theme("Green")

clock = sg.Text('', key = 'clock')
label = sg.Text("Type in a task: ")
input_box = sg.InputText(tooltip="Enter Todo", key='new_todo', size=46) #tooltip will show up when you mouseover

list_todos = sg.Listbox(values=functions.get_todos(), key='todos', enable_events=True, size=[45, 5])

#Buttons
add_button = sg.Button("Add", size = 10)
edit_button = sg.Button("Edit", size = 10)
complete_button = sg.Button("Complete", size = 10)
exit_button = sg.Button("Exit")

mainWindow = sg.Window('My todo app', layout = [[clock],
                                                [label], 
                                                [input_box, add_button],
                                                [list_todos, complete_button],
                                                [edit_button, exit_button]], 
                                                font = ('Helevetica', 20))

while True:
    event, values = mainWindow.read(timeout = 1000) #displays the window
    mainWindow["clock"].update(value=time.strftime("%b %d, %Y %H:%M:%S"))
    match event:
        case "Add":
            todos = functions.get_todos()
            new_todo = values['new_todo']
            todos.append(new_todo + '\n')
            functions.set_todos(todos)

            #update list box in real time
            mainWindow['todos'].update(values = todos)

        case "Edit":
            try:
                todo_to_edit = values['todos'][0]
                new_todo = values['new_todo'] #New todo is what they entered in the input box

                todos = functions.get_todos()
                index = todos.index(todo_to_edit)
                todos[index] = new_todo 

                mainWindow['todos'].update(values=todos) #Replace current list with new list

            except IndexError:
                sg.popup("Please Select A Todo First!", font = ('Helevetica', 20))

        case "Complete":
            try:
                todo_to_complete = values['todos'][0]
                todos = functions.get_todos()
                todos.remove(todo_to_complete)
                functions.set_todos(todos)

                mainWindow['todos'].update(values=todos)
                mainWindow['new_todo'].update(value = '')

            except IndexError:
                sg.popup("Please Select A Todo First!", font = ('Helevetica', 20))

        #show selection in input box
        case 'todos':
            mainWindow['new_todo'].update(value=values['todos'][0])

        case sg.WIN_CLOSED | "Exit":
            break

mainWindow.close()
