def get_todos(filepath="files/todos.txt"):
    """Read a text file and return the list of
    to-do items.
    """
    # 'with' context manager, we do not need file.close()
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    # when no return statement, function returns None
    # readlines() gives you a list of string of lines whereas read() gives a single string of all data
    return todos_local


def write_todos(todos_arg, filepath="files/todos.txt"):
    """Write the to-do items list in the text file."""
    # 'w' for write (also overwrites existing file)
    with open(filepath, 'w') as file_local:
        file_local.writelines(todos_arg)


# We only want to execute below lines when we run this script, not when imported in main.py file
if __name__ == "__main__":  # this variable is secretly defined by python for every file
    print("Hello")
    print(get_todos())
