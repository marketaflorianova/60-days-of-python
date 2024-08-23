import functions as fn
import FreeSimpleGUI as sg
import time

sg.theme("DarkPurple3")

clock = sg.Text("", key="clock")
label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="Enter todo", key="todo")
add_button = sg.Button("Add")
list_box = sg.Listbox(values=fn.get_todos(),
                      key="todos",
                      enable_events=True,
                      size=[45, 10])
edit_button = sg.Button("Edit")
complete_button = sg.Button("Complete")
exit_button = sg.Button("Exit")

layout = [[clock],
          [label],
          [input_box, add_button],
          [list_box, edit_button, complete_button],
          [exit_button]
          ]

window = sg.Window("My to-do app",
                   layout=layout,
                   font=('Helvetica', 20))

while True:  # prevents the program from being closed when the "Add" button is pressed
    event, values = window.read(timeout=200)
    window["clock"].update(value=time.strftime("%d %b %Y, %H:%m"))
    match event:
        case "Add":
            todos = fn.get_todos()
            new_todo = values['todo'] + "\n"  # value of the todo key
            todos.append(new_todo)
            fn.write_todos(todos)
            window['todos'].update(values=todos)
        case "Edit":
            try:
                todo_to_edit = values['todos'][0]
                new_todo = values['todo'] + '\n'
                todos = fn.get_todos()
                index = todos.index(todo_to_edit)
                todos[index] = new_todo  # old todo (with a given index) is gonna be replaced with a new one
                fn.write_todos(todos)
                window['todos'].update(values=todos)
            except IndexError:
                sg.popup("Please select an item first", font=("Helvetica", 20))
        case 'todos':
            window['todo'].update(value=values['todos'][0])
        case 'Complete':
            try:
                todo_to_complete = values['todos'][0]
                todos = fn.get_todos()
                todos.remove(todo_to_complete)
                fn.write_todos(todos)
                window['todos'].update(values=todos)
                window['todo'].update('')
            except IndexError:
                sg.popup("Please select an item first", font=("Helvetica", 20))
        case 'Exit':
            break
        case 'todos':
            window['todo'].update(value=values['todos'][0])
        case sg.WIN_CLOSED:
            break # exit() stops the program completely, whereas break just jumps out of the loop

window.close()
