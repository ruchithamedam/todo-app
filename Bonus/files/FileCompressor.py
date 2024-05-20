import FreeSimpleGUI as Sg
from zip_creator import make_archive

label1 = Sg.Text("Select Files to Compress")
input_box1 = Sg.Input()
button1 = Sg.FilesBrowse("Choose", key="file")

label2 = Sg.Text("Select Destination Folder")
input_box2 = Sg.Input()
button2 = Sg.FolderBrowse("Choose", key="folder")

button3 = Sg.Button("Compress")
output = Sg.Text(key="output", text_color="red")

window = Sg.Window("File Compressor",
                   layout=[[label1, input_box1, button1], [label2, input_box2, button2],
                           [button3, output]])

while True:
    event, values = window.read()
    print(event)
    print(values)
    filepaths = values["file"].split(";")
    folder = values["folder"]
    make_archive(filepaths, folder)
    window["output"].update(value="Compression Completed")


window.close()
