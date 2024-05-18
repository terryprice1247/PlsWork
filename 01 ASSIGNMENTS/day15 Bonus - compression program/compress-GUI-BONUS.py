import FreeSimpleGUI as sg
from zip_creator import make_archive

label1 = sg.Text("Select files to compress")
input1 = sg.Input()                                    # KEY IS A LABEL FOR THE WIDGETS THAT WE USE
choose_button1 = sg.FilesBrowse("Choose", key="files")  # Files browse is used to open key rename the same var

label2 = sg.Text("Select destination folder")
input2 = sg.Input()
choose_button2 = sg.FolderBrowse("Choose", key="folder")  # chooses the folder the file will then go into.

compress_button = sg.Button("Compress")
output_label = sg.Text(key="output", text_color="green")

window = sg.Window("File Compressor",
                   layout=[[label1, input1, choose_button1],
                           [label2, input2, choose_button2],
                           [compress_button, output_label]])
while True:
    event, values = window.read()            # reading the event and the value of the event
    print(event, values)                     # showing us the selection and action
    filepaths = values["files"].split(";")    # spilt the filepath name from the directory
    folder = values["folder"]
    make_archive(filepaths, folder)
    window["output"].update(value="Compression completed")

window.close()