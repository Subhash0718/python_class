l = []
print("This is a to-do-list")



while(True):
    print("Choose one task from the below:")
    print("1. Add a task\n2. Show all the tasks\n3. Remove the task\n4. Remove all the task\n5. Exit the program")
    choice = int(input("Enter the choice no: "))
    match choice:
        case 1:
            print("You can maximum add 5 tasks at single time ")
            n = int(input("Enter how many tasks to be added?: "))
            if(n>=1 or n<=5):
                for i in range(0,n):
                    task = input("Enter the task to do: ")
                    l.append(task)
            else:
                print("Enter the task less than 5 ")


            print()
            print()


        case 2:
            if(len(l)>0):
                print("These are the tasks you stored")
                for i in l:
                    print("* ",i)

            else:
                print("There are no tasks in the your list\nPlease add atleast one task and see your to-do list")
            print()
            print()



        case 3:
            if(len(l)>0):
                print("You can delete only one task at a time from the to-do list")
                print("Enter your task spelling correctly")
                remove_task = input("Enter the task name to be removed: ")
                try:
                    l.remove(remove_task)
                    print("The task has been successfully removed")
                except ValueError:
                    print("The task you have entered is not found.....!")

            else:
                print("You have no task to be removed")
                print("please add some task to remove")
            print()
            print()

        case 4:
            if(len(l)>0):
                length = len(l)
                l.clear()
                print(f"You have deleted all your {length} tasks")

            else:
                print("There is no task to delete\nPlease add task to delete")


            print()
            print()

            
        case 5:
            print("Exiting......")
            break



        case _:
            print("Please enter the valid choice no !!!!!!!!!! ")
            print()
            print()


print("Thanks for using the to-do-list")
