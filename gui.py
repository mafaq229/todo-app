from modules import functions
import PySimpleGUI as sg
import time

sg.theme("Black")

clock = sg.Text(key='clock')
label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="Enter todo", key="todo")
add_button = sg.Button("Add", size= 10)
list_box = sg.Listbox(values=functions.get_todos(), key='todos',  # use different keys
                      enable_events=True, size=(45, 10))  # (45,10) is width and height of listbox in terms of character
edit_button = sg.Button("Edit")
complete_button = sg.Button("Complete")
exit_button = sg.Button("Exit")
# layout expects a list of list and each of the list consists of PySimpleGUI object instances (widget)
# think of each row as a separate list the overall list
# window = sg.Window("My To-Do App", layout=[[label, input_box]])  # same line
window = sg.Window("My To-Do App",
                   layout=[[clock],
                           [label],
                           [input_box, add_button],
                           [list_box, edit_button, complete_button],
                           [exit_button]],
                   font=('Helvetica', 20))

while True:
    event, values = window.read(timeout=500)  # Displays window on the screen | timeout so loop runs every 10ms
    if event == sg.WINDOW_CLOSED:
        break
    window['clock'].update(value=time.strftime("%b %d, %Y %H:%M:%S"))  # timeout=10 helps display time at app start
    print(1, event)
    print(2, values)
    match event:
        case "Add":
            todos = functions.get_todos()
            new_todo = values['todo'] + "\n"
            todos.append(new_todo)
            functions.write_todos(todos)
            window['todos'].update(values=todos)
        case "Edit":
            try:
                todo_to_edit = values['todos'][0]
                new_todo = values['todo']

                todos = functions.get_todos()
                index = todos.index(todo_to_edit)
                todos[index] = new_todo + '\n'
                functions.write_todos(todos)
                window['todos'].update(values=todos)
            except IndexError:
                sg.popup("Please select an item first.", font=('Helvetica', 20))
        case "Complete":
            try:
                todo_to_complete = values['todos'][0]
                todos = functions.get_todos()
                todos.remove(todo_to_complete)
                functions.write_todos(todos)
                window['todos'].update(values=todos)
                window['todo'].update(value="")  # to remove completed task from input box
            except IndexError:
                sg.popup("Please select an item first.", font=('Helvetica', 20))
        case "Exit":
            break
        case 'todos':
            window['todo'].update(value=values['todos'][0])
        case sg.WINDOW_CLOSED:
            # 'break' stops the loop where as 'exit()' stops the program
            break


window.close()
