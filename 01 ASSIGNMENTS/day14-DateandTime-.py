import functions   # This is the file where we put our functions in.
import time

now = time.strftime("%b %d, %Y %H:%M:%S")
print("It is", now)

while True:
    user_action = input("Type add, show, edit, delete or exit: ")
    user_action = user_action.strip()  # strip makes it so you cant mess up with spaces in input

    if user_action.startswith("add"):  # making sure that it only goes if it starts with add
        todo = user_action[4:]  # list slicing removing characters so add isn't on there

        todos = functions.get_todos()    # <-- We write the file name in front of the function

        todos.append(todo + '\n')  # puts the input into a list

        functions.write_todos(todos)

    elif user_action.startswith('show'):

        todos = functions.get_todos()

        for index, item in enumerate(todos):  # enumerate adds numbers next to items with index
            item = item.strip('\n')  # strips the extra line from the list
            row = f"{index + 1}-{item}"  # f string to place a space in between the index and item
            print(row)
    elif user_action.startswith('edit'):
        try:  # tells the system to run the code if starts with edit
            number = int(user_action[5:])  # telling the system to go to the number in the 5th character
            number = number - 1

            todos = functions.get_todos()

            new_todo = input("Enter a todo: ")
            todos[number] = new_todo + '\n'

            functions.write_todos(todos)
        except ValueError:  # if a value error is created, it runs the below code
            print("Your command is not valid.")
            continue  # send the code back to the start

    elif user_action.startswith('delete'):
        try:
            number = int(user_action[7:])
            todos = functions.get_todos()
            index = number - 1
            to_do_remove = todos[index].strip('\n')
            todos.pop(index)  # the pop method goes into the list we are telling item to be removed

            functions.write_todos(todos)

            message = f"Todo {to_do_remove} was removed from the list."
            print(message)
        except IndexError:
            print("There is no item with that number.")
            continue

    elif user_action.startswith('exit'):
        break
    else:
        print("Command is not valid")
print("Bye!")
