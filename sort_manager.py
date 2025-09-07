def selection(arr,order):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i+1,n):
            if(order == "ascending" and arr[j]<arr[min_index] or (order == "descending" and arr[j]>arr[min_index])):
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]


    return arr

def merge(arr,order):
    if(len(arr)>1):
        mid = len(arr)//2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge(left_half,order)
        merge(right_half,order)

        i = j = k = 0


        while i<len(left_half) and j<len(right_half):
            if(order =="ascending" and left_half[i] < right_half[j] or (order == "descending" and left_half[i]>right_half[j])):
                arr[k] = left_half[i]
                i+=1
            
            else:
                arr[k] = right_half[j]
                j+=1
            k+=1

        while i<len(left_half):
            arr[k] = left_half[i]
            i+=1
            k+=1

        while j<len(right_half):
            arr[k] = right_half[j]
            j+=1
            k+=1


    return arr


def insertion(arr,order):

    n = len(arr)
    for i in range(1,n):
        key = arr[i]
        j = i-1
        while ((order=="ascending" and j>=0 and arr[j]>key) or (order == "descending" and j>=0 and arr[j]<key)):
            arr[j+1] = arr[j]
            j-=1

        arr[j+1] = key


    return arr

def bubble(arr,order):
    n = len(arr)
    swapped = False
    for i in range(n):
        for j in range(0,n-i-1):

            if order == "ascending" and  arr[j]>arr[j+1] or order == "descending" and arr[j]<arr[j+1]:
                arr[j], arr[j+1] = arr[j+1] , arr[j]
                swapped = True 

        if(swapped == False):
            break

    return arr


print("Welcome to Sort Mangement ")
print("You can sort your list by ascending or descending order")

while(True):
    order = ''
    choice = 0
    print("Choose how to sort your list from below???")
    print("1. Insertion sort\n2. Bubble Sort\n3. Merge Sort\n4. Selection sort\n5. Exit the program")
    choice = int(input("Enter the choice no: "))
    if(choice<5):
        order = input("Enter how to arrange ascending or descending: ").lower()  

    arr = [1,46,2,0,9,50]
    match choice:

        case 1:
            print("Before Sorting ",arr)
            result = insertion(arr,order)
            print("After Sorting ",result)
            print("\n\n\n")

        case 2:
            print("Before Sorting ",arr)            
            result = bubble(arr,order)
            print("After Sorting ",result)
            print("\n\n\n")            

        case 3:
            print("Before Sorting ",arr)            
            result = merge(arr,order)
            print("After Sorting ",result)
            print("\n\n\n")           

        case 4:
            print("Before Sorting ",arr)            
            result = selection(arr,order)
            print("After Sorting ",result)
            print("\n\n\n")            

        case 5:
            print("Exiting................")
            break

        case _:
            print("Please Enter the valid option!!!!!")
            print("\n\n\n")


print("Thanks for using this......")            

        