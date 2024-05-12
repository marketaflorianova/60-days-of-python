import functions as fn
import FreeSimpleGUI as sg

label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="Enter todo", key="todo")

add_button = sg.Button("Add")

window = sg.Window("My to-do app",
                   layout=[[label], [input_box, add_button]],
                   font=('Helvetica', 20))

while True:  # prevents the program from being closed when the "Add" button is pressed
    event, values = window.read()
    print(event)  # label of the button that was pressed
    print(values)  # values filled by the user
    match event:
        case "Add":
            todos = fn.get_todos()
            new_todo = values['todo'] + "\n"  # value of the todo key
            todos.append(new_todo)
            fn.write_todos(todos)
        case sg.WIN_CLOSED:
            break

window.close()
