# from functions import get_todos, write_todos
from modules import functions
import time

now = time.strftime("%b %d, %Y %H:%M:%S")
print("It is,", now)
while True:
    # default value in strip is space " "
    user_action = input("Type add, show, edit, complete or exit: ").strip()

    if user_action.startswith("add"):
        todo = user_action[4:]
        todos = functions.get_todos()
        todos.append(todo + '\n')
        functions.write_todos(todos)

    elif user_action.startswith("show"):  # use elif() so that if condition in true, rest of the program is not executed
        # without 'with' context manager
        # file = open('files/todos.txt', 'r')
        # todos = file.readlines()
        # file.close()

        todos = functions.get_todos()

        # new_todos = [item.strip('\n') for item in todos] # list comprehension

        # enumerate() takes list as argument and returns index & their values inside list
        for index, item in enumerate(todos):
            item = item.strip("\n")
            # f-string can be used to add an argument to string
            row = f"{index+1}-{item}"
            # print statement adds a \n after every print in loop
            print(row)
    elif user_action.startswith("edit"):
        try:
            number = int(user_action[5:]) - 1

            todos = functions.get_todos()
            print("Here is todos existing", todos)

            todos[number] = input("Enter new todo: ") + '\n'
            print("Here is how it will be", todos)

            functions.write_todos(todos)
        except ValueError:
            print("Your command is not valid.")
            # continue statements runs another cycle of while loop
            continue

    elif user_action.startswith("complete"):
        try:
            todos = functions.get_todos()
            # pop takes in index as argument and returns + remove. Default index is -1
            # remove() takes value as argument and removes the value. Argument is necessary
            number = int(user_action[9:])
            index = number - 1
            todo_to_remove = todos[index].strip('\n')
            todos.pop(index)

            functions.write_todos(todos)

            print(f"Todo {todo_to_remove} was removed from the list")
        except IndexError:
            print("There is no item with that number.")
            continue

    elif user_action.startswith("exit"):
        break

    else:
        print("Command is not valid.")

print('Bye!')
