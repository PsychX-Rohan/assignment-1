# insertion_sort.py

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

try:
    arr = list(map(int, input("Enter numbers separated by spaces or commas: ")
                   .replace(',', ' ')
                   .split()))
    print("Sorted array:", insertion_sort(arr))
except ValueError:
    print("Invalid input. Please enter only integers separated by spaces or commas.")
