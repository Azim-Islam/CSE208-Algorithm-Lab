def binSearch(array, element):
    """
        Iterative implementation of Binary Search.
    """
    i = 0
    j = len(array)
    
    mid = (i+j)//2 
    while i < j:
        print(f"Mid index {mid} i = {i} j = {j}")
        if array[mid] == element:
            print(f"{element} was found on {mid}th index")
            break
        
        if array[mid] < element:
            i = mid + 1
        
        elif array[mid] > element:
            j = mid - 1
        
        mid = (i+j)//2
        
        
def binSearchRec(array, i, j, mid, element):
    """
        Recursive implementation of Binary Search.
    """
    if array[mid] < element:
        return binSearchRec(array, mid, j, (i+j)//2, element)

    elif array[mid] > element:
        return binSearchRec(array, i, mid, (i+j)//2, element)

    elif array[mid] == element:
        print(f"{element} was found on {mid}th index")

    if not i<j:
        print(f"{element} was not found on.")
        
        
    
array = [11, 13, 15, 17, 21, 23, 24, 26, 28, 33, 36, 39, 41, 43, 46, 51, 55, 57, 67, 70]

element = 26

binSearch(array, element)

binSearchRec(array, 0, len(array)-1, 0, element)