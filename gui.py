import functions
import FreeSimpleGUI as Sg

label = Sg.Text("Type in a To-Do")
input_box = Sg.InputText(tooltip="Enter todo", key='todo')
add_button = Sg.Button("add")

window = Sg.Window('My TO-DO App', layout=[[label], [input_box, add_button]])


while True:
    event, values = window.Read()
    print(event)
    print(values)
    match event:
        case "add":
            todos = functions.get_todos()
            new_todo =values['todo']
            todos.append(new_todo)
            functions.write_todos(todos)
        case Sg.WIN_CLOSED:
            break

window.Close()


