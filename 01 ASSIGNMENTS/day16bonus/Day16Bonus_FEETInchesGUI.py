import FreeSimpleGUI as sg
from converters import convert              # import the function to convert

sg.theme("Black")

feet_label = sg.Text("Enter Feet")
feet_input = sg.Input(key="feet")           # white line that gives us input

inches_label = sg.Text("Enter Inches")
inches_input = sg.Input(key="inches")

button = sg.Button("Convert")
button_2 = sg.Button("Exit")
output_label = sg.Text("", key="output")

window = sg.Window("Convertor",                         # putting all those elements on to the app
                   layout=[[feet_label, feet_input],
                           [inches_label, inches_input],
                           [button, button_2, output_label]])

while True:
    event, values = window.read()                           # showing the values onto the screen revealing the app
    match event:
        case "Exit":                                # when exit button is pushed, finishing program
            break
        case sg.WIN_CLOSED:
            break
    try:
        feet = float(values["feet"])                           # turning the value of both feet and inches into floats
        inches = float(values["inches"])

        result = convert(feet, inches)                # using now the function of feet and inches and variable result
        window["output"].update(value=f"{result} m", text_color="white")   # using the key output and printing the value
    except ValueError:                              # if no one places a value in the boxes, we will get this.
        sg.popup("Please provide two numbers.", font=("Helvetica", 15))


window.close()
