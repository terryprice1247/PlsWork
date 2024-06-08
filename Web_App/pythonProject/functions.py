FILEPATH = "todos.txt"      # the functions page


def get_todos():  # making the filepath the document we are using
    with open('todos.txt', encoding='iso-8859-1') as file:
        todos = file.readlines()
    return todos  # defining how we will call the function


def write_todos(todos_arg, filepath=FILEPATH):  # making a function to write data making a new local variable
    """ Write the to-do items list in the text file."""
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)


if __name__ == "__main__":
    print("Hello")
    print(get_todos())
