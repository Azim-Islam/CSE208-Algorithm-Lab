
# function to find maximum sum of subarray crossing the middle element
from array import array


def max_crossing_subarray(ar, low, mid, high):

    left_sum = -999999
    sum = 0

    for i in range(mid, low-1, -1):
        sum = sum+ar[i]
        if (sum>left_sum):
            left_sum = sum

    right_sum = -999999
    sum = 0

    for i in range(mid+1, high+1):
        sum = sum+ar[i]
        if (sum>right_sum):
            right_sum = sum

    return left_sum+right_sum

# calculating the maximum subarray sum
def max_sum_subarray(ar, low, high):
    if (high == low): # only one element in an array or base case
        print("Array =", [ar[high]])
        print("Max =", arr[high])
        return ar[high]

    # middle element of the array
    mid = (high+low)//2

    # maximum sum in the left subarray
    maximum_sum_left_subarray = max_sum_subarray(ar, low, mid)
    # maximum sum in the right subarray
    maximum_sum_right_subarray = max_sum_subarray(ar, mid+1, high)
    # maximum sum in the array containing the middle element
    maximum_sum_crossing_subarray = max_crossing_subarray(ar, low, mid, high)

    # returning the maximum among the above three numbers
    print("Array =", ar[low:high+1])
    print("Max =", max(maximum_sum_left_subarray, maximum_sum_right_subarray, maximum_sum_crossing_subarray))
    return max(maximum_sum_left_subarray, maximum_sum_right_subarray, maximum_sum_crossing_subarray)

    #if a value of the sub-array is 0 then we change it to -1
    #if the index of the value is odd then we will turn it into a negative number
def generate_array(array):
    for i in range(len(array)):
        if array[i] == 0:
            array[i] = -1
        if array[i]%2:
            array[i] = array[i]*-1
    return array

#We generate the subarray from my ID
arr = generate_array([1,9,2,0,1,0,2,6])
print("-"*50)
print("Generated Sub Array = ", arr)
print("-"*50)
print("Maximum Sub-Array = ", max_sum_subarray(arr, 0, len(arr)-1))