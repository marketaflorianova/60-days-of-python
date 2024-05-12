def get_todos(filename="todos.txt"):
    """
    Read a text file and return a list of to-do items.
    """
    with open(filename, "r") as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_arg, filename="todos.txt"):
    with open(filename, "w") as file_local:
        file_local.writelines(todos_arg)


if __name__ == "__main__":
    print(get_todos())