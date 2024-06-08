FILEPATH = "WebApp-Todo/todos.txt"


def get_todos(filepath=FILEPATH):  # making the filepath the document we are using
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local  # defining how we will call the function


def write_todos(todos_arg, filepath=FILEPATH):  # making a function to write data making a new local variable
    """ Write the to-do items list in the text file."""
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)


if __name__ == "__main__":
    print("Hello")
    print(get_todos())
