import random
#merging 3 of the sub-array
def merge(arr, low, mid1, mid2, high):

    left_array = arr[low - 1 : mid1]
    mid_array = arr[mid1: mid2 + 1]
    right_array = arr[mid2 + 1 : high]

    left_array.append(float('inf')) #Inserting these because the array may not be properly divisible by 3
    mid_array.append(float('inf'))
    right_array.append(float('inf'))
    
    index_left = 0 #Setting all indexs to start from 0
    index_mid = 0
    index_right = 0
    
    print(left_array, mid_array, right_array)
    #merging 3 of the sub arrays.
    for i in range(low-1, high):
        #find the minimum values then assining them at array
        minimum = min([left_array[index_left], mid_array[index_mid], right_array[index_right]])
        if minimum == left_array[index_left]:
            arr[i] = left_array[index_left]
            index_left += 1
        elif minimum == mid_array[index_mid]:
            arr[i] = mid_array[index_mid]
            index_mid += 1
        else:
            arr[i] = right_array[index_right]
            index_right += 1
    
#dividing the array into 3 sub arrays. base case if atleast one of the sub-array has atleast one element.   
def merge_sort(arr, low, high):
    
    if len(arr[low -1: high]) < 2:
        return arr
    else: 
        mid1 = low + ((high - low) // 3)
        mid2 = low + 2 * ((high-low) // 3)

        merge_sort(arr, low, mid1)
        merge_sort(arr, mid1+1, mid2 + 1)
        merge_sort(arr, mid2+2, high)
        merge(arr, low, mid1, mid2, high)
        return arr
    
    

arr = random.sample(range(1, 20), 15)
#arr = [1,9,2,0,1,0,2,6]
print("-"*50)
print("Current array ", arr)
print("-"*50)
low = 1 #low starting from 1
high = len(arr) #length of array
print(merge_sort(arr, low, high))
print("-"*50)
print("Sorted array ", arr)
