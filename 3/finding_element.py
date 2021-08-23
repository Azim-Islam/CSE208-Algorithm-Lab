import random



array = random.sample(range(1, 20), 11) # Random list within 0 to 20 OF 11 elements
#array = [19, 21, 31, 12, 13, 6, 26, 15, 17, 21, 31]
print(array)

def search_element(element, i):
    
    if array[i] == element:
        print(f"Element Found! Index = {i}")
        return True
    
    if i < 0:
        return False #If i is less than 0 then the we have searched the whole array but could not find the element.
    return search_element(element, i-1)

    
    

element = 6 #my id
found = search_element(element, len(array) - 1) # Searching Element In the array, and Storing True False if it is found.

if not found: #if element not found inside the array then print
    print("Element Not Found")
    