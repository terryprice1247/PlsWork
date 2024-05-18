import FreeSimpleGUI as sg
from converters import convert              # import the function to convert

feet_label = sg.Text("Enter Feet")
feet_input = sg.Input(key="feet")           # white line that gives us input

inches_label = sg.Text("Enter Inches")
inches_input = sg.Input(key="inches")

button = sg.Button("Convert")
output_label = sg.Text("", key="output")

window = sg.Window("Convertor",                         # putting all those elements on to the app
                   layout=[[feet_label, feet_input],
                           [inches_label, inches_input],
                           [button, output_label]])

while True:
    event, values = window.read()                           # showing the values onto the screen revealing the app
    feet = float(values["feet"])                           # turning the value of both feet and inches into floats
    inches = float(values["inches"])

    result = convert(feet, inches)                     # using now the function of feet and inches and variable result
    window["output"].update(value=f"{result} m", text_color="white")   # using the key output and printing the value

window.close()
