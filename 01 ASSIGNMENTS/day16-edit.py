import functions  # This is the file where we put our functions in.
import FreeSimpleGUI as sg              # naming the app sg to make it easier to code

label = sg.Text("Type in a to-do")          # creates a label
input_box = sg.InputText(tooltip ="Enter todo", key="todo")     # what we will see if we hover mouse over textbox
add_button = sg.Button("Add")
list_box = sg.Listbox(values=functions.get_todos(), key ='todos',   # getting the list from todos.txt
                      enable_events=True, size=[45, 10])            # enabling true or false
edit_button = sg.Button("Edit")

window = sg.Window('My To-Do App',
                   layout=[[label], [input_box, add_button], [list_box, edit_button]],    # this is a element
                   font=('Helvetica', 20))  # where we place the elements

while True:             # making a loop so the program won't close yet
    event, values = window.read()  # making a variable to read what we input
    print(1, event)
    print(2, values)
    match event:          # making an if / then style loop
        case "Add":
            todos = functions.get_todos()           # will call the get todos function from the other file
            new_todo = values['todo'] + "\n"               # gives us the value of the action added from the app
            todos.append(new_todo)
            functions.write_todos(todos)
            window['todos'].update(values=todos)        # adding the new todo on the list box app in realtime

        case "Edit":
            todo_to_edit = values['todos'][0]             # selects a todo to edit from our list
            new_todo = values['todo']

            todos = functions.get_todos()
            index = todos.index(todo_to_edit)
            todos[index] = new_todo                 # updates the todos list with new one
            functions.write_todos(todos)            # writes that new one to the todos.txt file
            window['todos'].update(values=todos)        # going into the window clicking the todos and updating

        case 'todos':
            window['todo'].update(value=values['todos'][0])  # when we click the item it changes on the textbox
        case sg.WIN_CLOSED:
            break

window.close()