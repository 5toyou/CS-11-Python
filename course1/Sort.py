arr = [5,-3,6,1,42,13,0]

#Bubble sort
def Bubble_sort():
    lengh = len(arr)
    for i in range(lengh - 1):
        for value in range(lengh - i - 1):
            if arr[value] > arr[value+1]:
                arr[value], arr[value + 1] = arr[value + 1], arr[value]

#Selection sort
def Selection_sort():
    lengh = len(arr)
    for i in range(lengh - 1):
        min_index = i
        for value in range(i + 1, lengh):
            if arr[value] < arr[min_index]:
                min_index = value
        arr[i], arr[min_index] = arr[min_index], arr[i]

#Insertion sort
def Insertion_sort():
    lengh = len(arr)
    for i in range(1,lengh):
        ins_index = i
        current_value = arr.pop(i)
        for value in range(i - 1, -1, -1):
            if arr[value] > current_value:
                ins_index = value
        arr.insert(ins_index, current_value)

#Quick sort
def Quick_sort(array, low = 0, high = None):
  if high is None:
    high = len(array) - 1

  if low < high:
    pivot_index = partition(array, low, high)
    Quick_sort(array, low, pivot_index - 1)
    Quick_sort(array, pivot_index + 1, high)

def partition(array, low, high):
  pivot = array[high]
  i = low - 1

  for value in range(low, high):
     if array[value] <= pivot:
       i += 1
       array[i], array[value] = array[value], array[i]

  array[i + 1], array[high] = array[high], array[i + 1]
  return i + 1


def Menu():
    print("\n1 = Bubble sort")
    print("2 = Selection sort")
    print("3 = Insertion sort")
    print("4 = Quick sort")

Menu()
print(arr)
choice = int(input("Enter how to sort: "))
match choice:
    case 1:
        Bubble_sort()
        print(arr)
    case 2:
        Selection_sort()
        print(arr)
    case 3:
        Insertion_sort()
        print(arr)
    case 4:
        Quick_sort(arr)
        print(arr)