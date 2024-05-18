import functions
import FreeSimpleGUI as Sg

label = Sg.Text("Type in a To-Do")
input_box = Sg.InputText(tooltip="Enter todo")
add_button = Sg.Button("add")

window = Sg.Window('My TO-DO App', layout=[[label], [input_box, add_button]])
window.Read()
window.Close()
