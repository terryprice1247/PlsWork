import functions  # This is the file where we put our functions in.
import FreeSimpleGUI as sg              # naming the app sg to make it easier to code

label = sg.Text("Type in a to-do")          # creates a label
input_box = sg.InputText(tooltip ="Enter todo", key="todo")     # what we will see if we hover mouse over textbox
add_button = sg.Button("Add")

window = sg.Window('My To-Do App',
                   layout=[[label, input_box, add_button]],     # this is a element
                   font=('Helvetica', 20))  # where we place the elements

while True:             # making a loop so the program won't close yet
    event, values = window.read()  # making a variable to read what we input
    print(event)
    print(values)
    match event:          # making an if / then style loop
        case "Add":
            todos = functions.get_todos()           # will call the get todos function from the other file
            new_todo = values['todo'] + "\n"               # gives us the value of the action added from the app
            todos.append(new_todo)
            functions.write_todos(todos)
        case sg.WIN_CLOSED:
            break

window.close()
