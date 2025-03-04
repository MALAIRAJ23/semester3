def mergesort(arr):
    if len(arr) < 2:
        return arr
    else:
        middle = len(arr) // 2
        left_half = mergesort(arr[:middle])
        right_half = mergesort(arr[middle:])
        return merge(left_half, right_half)
def merge(left_half, right_half):
    sortedarr = []
    i = j = 0

    while i < len(left_half) and j < len(right_half):
        if left_half[i] < right_half[j]:
            sortedarr.append(left_half[i])
            i += 1
        else:
            sortedarr.append(right_half[j])
            j += 1
    while i < len(left_half):   
        sortedarr.append(left_half[i])
        i += 1
    while j < len(right_half):
        sortedarr.append(right_half[j])
        j += 1
    return sortedarr
def menu():
    while True:
        print("\n--- Merge Sort Menu ---")
        print("1. Sort an Array")
        print("2. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            arr = list(map(int, input("Enter the elements of the array separated by space: ").split()))
            print("Original Array:", arr)
            sorted_array = mergesort(arr)
            print("Sorted Array:", sorted_array)
        elif choice == "2":
            print("Exiting..")
            break
        else:
            print("Invalid choice. Please try again.")


menu()