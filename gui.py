from modules import functions
import PySimpleGUI as sg

label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="Enter todo")
add_button = sg.Button("Add")

# layout expects a list of list and each of the list consists of PySimpleGUI object Instances
# window = sg.Window("My To-Do App", layout=[[label, input_box]])  # same line
window = sg.Window("My To-Do App", layout=[[label], [input_box, add_button]])  # each line is a list (2 line interface)

window.read()  # Displays window on the screen
window.close()
