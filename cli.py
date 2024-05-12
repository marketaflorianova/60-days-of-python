from functions import get_todos, write_todos
import time

now = time.strftime("%d %b %Y, %H:%m")
print(f"Now is {now}.")

while True:
    user_action = input("Type add, show, edit, complete, or exit: ")
    user_action = user_action.strip()

    if user_action.startswith("add"):
        todo = user_action[4:]

        todos = get_todos()  # function call

        todos.append(todo + "\n")

        write_todos(todos)

    elif user_action.startswith("show"):
        todos = get_todos()

        # new_todos = [item.strip('\n') for item in todos] - for items in a list

        for index, todo in enumerate(todos):
            todo = todo.strip('\n')
            todo = todo.title()
            row = f"{index + 1}-{todo}"
            print(row)
    elif user_action.startswith("edit"):
        try:
            number = int(user_action[5:])
            number = number - 1

            todos = get_todos()

            new_todo = input("Enter new todo: ")
            todos[number] = new_todo + "\n"

            write_todos(todos)
        except ValueError:
            print("Command not valid")
            # continue

    elif user_action.startswith("complete"):
        try:
            number = int(user_action[9:])

            todos = get_todos()

            number = number-1
            todo_to_remove = todos[number].strip('\n')
            todos.pop(number)

            write_todos(todos)

            message = f"Todo {todo_to_remove} was removed from the list."
            print(message)
        except ValueError:
            print("Command not valid")
            # continue

    elif user_action.startswith("exit"):
        break
    else:
        print("Command is not valid!")

    print("end of loop")

print("Bye!")
