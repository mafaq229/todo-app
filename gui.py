from modules import functions
import PySimpleGUI as sg

label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="Enter todo", key="todo")
add_button = sg.Button("Add")
list_box = sg.Listbox(values=functions.get_todos(), key='todos',  # use different keys
                      enable_events=True, size=(45, 10))
edit_button = sg.Button("Edit")

# layout expects a list of list and each of the list consists of PySimpleGUI object instances (widget)
# think of each row as a separate list the overall list
# window = sg.Window("My To-Do App", layout=[[label, input_box]])  # same line
window = sg.Window("My To-Do App",
                   layout=[[label], [input_box, add_button],
                           [list_box, edit_button]],
                   font=('Helvetica', 20))

while True:
    event, values = window.read()  # Displays window on the screen
    print(1, event)
    print(2, values)
    match event:
        case "Add":
            todos = functions.get_todos()
            new_todo = values['todo'] + "\n"
            todos.append(new_todo)
            functions.write_todos(todos)
        case "Edit":
            todo_to_edit = values['todos'][0]
            new_todo = values['todo']

            todos = functions.get_todos()
            index = todos.index(todo_to_edit)
            todos[index] = new_todo + '\n'
            functions.write_todos(todos)
            window['todos'].update(values=todos)
        case 'todos':
            window['todo'].update(value=values['todos'][0])
        case sg.WINDOW_CLOSED:
            break


window.close()
