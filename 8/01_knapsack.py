from random import choice

cached_table = dict()
#Generating random value-weight array
#2-tuple array where 0th index = value 1st index = weight
x = lambda : choice(range(10, 20)) #Values including 10 to 19
array = [[x(),x()]  for i in range(5)] #5 items

n = len(array)
capacity = 50 #Sack Capacity in Kilograms


def knapsack(capacity, index):
    #Checking the cached_dictionary for values
    if (capacity, index) in cached_table:
        return cached_table[(capacity, index)]
    
    #if index is out of bound then K = 0
    if(index >= n): 
        k = 0;
        
    else:
        #if capacity exceedes weight then EXCLUDE the item
        if(capacity < array[index][1]):
            k = knapsack(capacity, index+1)
        else:
        #If it does not; Then try EXCLUDING and also INCLUDING, whichever path gives the best solution
            k = max(knapsack(capacity, index+1), array[index][0] + knapsack(capacity - array[index][1], index + 1))

    #Saving the data inside our dictionary to memorize each sub-problem`s answer
    cached_table[(capacity, index)] = k
    return k

answer = knapsack(capacity, 0) #Starting from 0th Index


print(f"Value-Weight array [Value, Weight]: {array}")
print(f"Knapsack Capacity: {capacity} Kilo-Grams")
print(f"MAX VALUE: {answer} Taka")