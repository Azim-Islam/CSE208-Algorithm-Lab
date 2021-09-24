from abc import abstractproperty
from random import choice, sample

#Generating random value-weight array
#2-tuple array where 0th index = value 1st index = weight
x = lambda : choice(range(10, 100))
array = [[x(),x()]  for i in range(5)]
print(array)

#Calculating the value-weight ration into the nested  
#3-tuple array where 0th index = value 1st index = weight 2nd index = value/weight ratio

for i in array:
    i.append(i[0]/i[1])


    
#Sorting the value-weight array by vale/weight ratio
array.sort(key=lambda x: x[2], reverse=True)
print(array)

#Finding the maximum value that can be fit inside 100 unit weight constraint.
value = 0
weight = 0
for i in array:
    if weight+i[1] < 101:
        value += i[0]
        weight += i[1]
    else:
        value += i[2]*(100-weight)
        weight += (100-weight)

print(f"Maximum value: {value}\nTotal weight: {weight}")