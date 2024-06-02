def get_todos(filepath=f'C:/Users/Heba/Sulce_Python/App1/TodoApp/todos.txt'):
    """ Read the text file and return list of contents
    """
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local

def set_todos(contents_local, filepath=f'C:/Users/Heba/Sulce_Python/App1/TodoApp/todos.txt'):
    """overwrites existing file to write the whole list in it now
    store list items in text file
    opens text file in write mode and creates file objet representing the opened file
    """

    with open(filepath, 'w') as file_local:
        file_local.writelines(contents_local) #write new list to file           
    
    #Doesn't return anything since this file is a procedure that just modifies the file
