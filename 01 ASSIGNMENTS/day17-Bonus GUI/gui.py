import functions  # This is the file where we put our functions in.
import FreeSimpleGUI as sg  # naming the app sg to make it easier to code
import time
import os   # making it so if a file doesn't exist

if not os.path.exists("todos.txt"):         # if the file is not in location
    with open("todos.txt", "w") as file:           # opens new file named todos.txt
        pass                                # statement that doesn't do anything but has to be there

sg.theme("Black")  # makes the background black

clock = sg.Text('', key='clock')
label = sg.Text("Type in a to-do")  # creates a label
input_box = sg.InputText(tooltip="Enter todo", key="todo")  # what we will see if we hover mouse over textbox
add_button = sg.Button("Add", mouseover_colors="LightBlue2",
                       tooltip="Add Todo", key="Add")
list_box = sg.Listbox(values=functions.get_todos(), key='todos',  # getting the list from todos.txt
                      enable_events=True, size=[45, 10])  # enabling true or false
edit_button = sg.Button("Edit")
delete_button = sg.Button("Delete")
exit_button = sg.Button("Exit")

window = sg.Window('My To-Do App',
                   layout=[[clock],
                           [label],
                           [input_box, add_button],
                           [list_box, edit_button, delete_button],
                           [exit_button]],  # this is where we place our elements
                   font=('Helvetica', 20))

while True:  # making a loop so the program won't close until we wish it to
    event, values = window.read(timeout=200)  # making a variable to read what we input
    window['clock'].update(value=time.strftime("%b %d,%Y %H:%M:%S"))  # the clock functions code
    match event:  # making an if / then style loop
        case "Add":
            todos = functions.get_todos()  # will call the get todos function from the other file
            new_todo = values['todo'] + "\n"  # gives us the value of the action added from the app
            todos.append(new_todo)  # places the new todo into the list
            functions.write_todos(todos)  # writes it into todos.txt
            window['todos'].update(values=todos)  # adding the new todo on the list box app in realtime

        case "Edit":
            try:  # setting a variable to try this first
                todo_to_edit = values['todos'][0]  # selects a todo to edit from our list
                new_todo = values['todo']

                todos = functions.get_todos()
                index = todos.index(todo_to_edit)
                todos[index] = new_todo  # updates the todos list with new one
                functions.write_todos(todos)  # writes that new one to the todos.txt file
                window['todos'].update(values=todos)  # going into the window clicking the todos and updating
            except IndexError:  # if we get an index error ( they don't choose anything)
                sg.popup("Please select item first.", font=("Helvetica", 20))

        case "Delete":
            try:
                todo_to_delete = values['todos'][0]  # gets the value of the todo from list
                todos = functions.get_todos()  # calling get todo function with the values
                todos.remove(todo_to_delete)  # removes the todo we selected in app
                functions.write_todos(todos)  # calling the write todo function to update the file
                window['todos'].update(values=todos)  # updates the app so that it is gone
                window['todo'].update(value='')  # calling the input box by it key name and empty it
            except IndexError:
                sg.popup("Please select item first.", font=("Helvetica", 20))

        case "Exit":
            break

        case 'todos':
            window['todo'].update(value=values['todos'][0])  # when we click the item it changes on the textbox
        case sg.WIN_CLOSED:
            break

window.close()
