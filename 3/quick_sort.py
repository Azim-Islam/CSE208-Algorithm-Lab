
array = [3, 5, 2, 1, 4, 7, 6]


def quick_sort(array, lo, hi):
    if lo >= hi:
        return 
    part = partition(array, lo, hi)
    quick_sort(array, 0, part - 1)
    quick_sort(array, part + 1, hi)
    

def partition(array, low, high):

  # choose the rightmost element as pivot
  pivot = array[high]

  # pointer for greater element
  i = low - 1

  # traverse through all elements
  # compare each element with pivot
  for j in range(low, high):
    if array[j] <= pivot:
      # if element smaller than pivot is found
      # swap it with the greater element pointed by i
      i = i + 1

      # swapping element at i with element at j
      (array[i], array[j]) = (array[j], array[i])

  # swap the pivot element with the greater element specified by i
  (array[i + 1], array[high]) = (array[high], array[i + 1])

  # return the position from where partition is done
  return i + 1
    
def exec_():
    print(array)
    quick_sort(array, 0, len(array) - 1)
    print(array)
exec_()
    