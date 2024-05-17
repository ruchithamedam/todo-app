# from functions import get_todos, write_todos
import functions
import time

now = time.strftime("%b %d,%Y %H:%M:%S")
print("It is", now)


while True:
    user_action = input("Enter add, show ,edit,complete or exit:")
    user_action = user_action.strip()

    if user_action.startswith("add"):
        todo = user_action[4:]+'\n'

        todos = functions.get_todos()

        todos.append(todo)

        functions.write_todos(todos)

    elif user_action.startswith("show"):

        todos = functions.get_todos()

        for index, items in enumerate(todos):
            items = items.strip('\n')
            row = f"{index+1}-{items}"
            print(row)

    elif user_action.startswith("edit"):
        try:
            number = int(user_action[5:])
            print(number)

            number = number - 1

            todos = functions.get_todos("todos.txt")

            new_todo = input("Enter new todo:")
            todos[number] = new_todo+'\n'

            functions.write_todos(todos)
        except ValueError:
            print("Your command is invalid")
            continue

    elif user_action.startswith("complete"):
        try:
            number = int(user_action[9:])
            print(number)

            todos = functions.get_todos()

            index = number-1
            todo_to_remove = todos[index].strip('\n')
            todos.pop(index)

            functions.write_todos(todos)

            message = f"Todo {todo_to_remove} was removed from the list."
            print(message)
        except IndexError:
            print("There is no item with that number")
            continue

    elif user_action.startswith("exit"):
        break
    else:
        print("invalid command")
print("Bye!")
