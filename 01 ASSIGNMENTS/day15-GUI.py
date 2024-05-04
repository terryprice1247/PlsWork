import functions  # This is the file where we put our functions in.
import FreeSimpleGUI as sg              # naming the app sg to make it easier to code

label = sg.Text("Type in a to-do")          # creates a label
input_box = sg.InputText(tooltip ="Enter todo")     # what we will see if we hover mouse over textbox
add_button = sg.Button("Add")

window = sg.Window('My To-Do App', layout=[[label, input_box, add_button]])     # where we place the elements
window.read()  # displays window on screen
window.close()
