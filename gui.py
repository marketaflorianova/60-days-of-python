import functions as fn
import FreeSimpleGUI as sg

label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="Enter todo", key="todo")
add_button = sg.Button("Add")
list_box = sg.Listbox(values=fn.get_todos(),
                      key="todos",
                      enable_events=True,
                      size=[45, 10])
edit_button = sg.Button("Edit")

window = sg.Window("My to-do app",
                   layout=[[label], [input_box, add_button], [list_box, edit_button]],
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
            window['todos'].update(values=todos)
        case "Edit":
            todo_to_edit = values['todos'][0]
            new_todo = values['todo'] + '\n'

            todos = fn.get_todos()
            index = todos.index(todo_to_edit)
            todos[index] = new_todo  # old todo (with a given index) is gonna be replaced with a new one
            fn.write_todos(todos)
            window['todos'].update(values=todos)
        case 'todos':
            window['todo'].update(value=values['todos'][0])
        case sg.WIN_CLOSED:
            break

window.close()
