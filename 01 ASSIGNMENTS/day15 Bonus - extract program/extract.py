import FreeSimpleGUI as sg
from zip_extractor import extract_archive

sg.theme("Black")

label1 = sg.Text("Select Archive")
input1 = sg.Input()  # KEY IS A LABEL FOR THE WIDGETS THAT WE USE
choose_button1 = sg.FileBrowse("Choose", key="archive")

label2 = sg.Text("Select dest fold")
input2 = sg.Input()
choose_button2 = sg.FolderBrowse("Choose", key="folder")  # chooses the folder the file will go into.

extract_button = sg.Button("Extract")
output_label = sg.Text(key="output", text_color="green")

window = sg.Window("File Extractor",
                   layout=[[label1, input1, choose_button1],
                           [label2, input2, choose_button2],
                           [extract_button, output_label]])

while True:
    event, values = window.read()
    print(event, values)
    archivepatch = values["archive"]
    dest_dir = values["folder"]
    extract_archive(archivepatch, dest_dir)
    window["output"].update(value="Extraction Completed")

window.close()
