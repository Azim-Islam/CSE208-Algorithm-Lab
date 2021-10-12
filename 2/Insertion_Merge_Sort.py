import random
import time

def timerfunc(func):
    """
    A timer decorator
    """
    def function_timer(*args, **kwargs):
        """
        A nested function for timing other functions
        """
        start = time.time()
        value = func(*args, **kwargs)
        end = time.time()
        runtime = end - start
        print("-"*50)
        msg = "{func} took {time} seconds to complete"
        print(msg.format(func=func.__name__,
                         time=runtime))
        return value
    return function_timer

class Student:
    def __init__(self, id, name, credit, cgpa):
        self.id = id
        self.name = name
        self.credit = credit
        self.cgpa = cgpa

    def __ge__(self, other):
        return (self.credit, self.cgpa) > (other.credit, other.cgpa)

    def __lt__(self, other):
        return (self.credit, self.cgpa) < (other.credit, other.cgpa)

    def __str__(self):
        return f"{self.id} {self.name} {self.credit} {self.cgpa}"
        
def generateRandomStudent(n):
    array = []
    names = ["Abid", "Harun", "Yahia", "Hafiz", "Adnan", "Jabid", "Hannan", "Jakaria", "Ahmed", "Abid", "Raihan"]
    for i in range(n):
        name = random.choice(names)+" "+random.choice(names)
        id_ = random.randint(10000, 999999999999)
        cgpa_ = random.randint(1,4) + random.randint(1, 9)/10
        credits_ = random.randint(0, 162)
        array.append(Student(int(id_), name, int(credits_), float(cgpa_)))
    return array

def insertSort(array, reverse = False):
    """
        Input array, reverse to sort by descending order.
    """
    for i in range(len(array)-1):
        key = array[i+1]
        j = i
        while array[j] > key and j > -1:
            array[j+1] = array[j]
            j -= 1
        array[j+1] = key
    if reverse:
        array.reverse()

def mergeSort(array, reverse = False):
    if len(array) > 1:
        pivot  = len(array)//2
        L = array[:pivot] #Excluding pivot
        R = array[pivot:]
        
        mergeSort(L, reverse)
        mergeSort(R, reverse)
        
        i,j,k = 0,0,0 # i for L || j for R || k for actual sub array (R+L)
        
        while i < len(L) and j < len(R):
            if (L[i] < R[j])^reverse:
                array[k] = L[i]
                i += 1
            else:
                array[k] = R[j]
                j += 1

            k += 1
        
        #Copying the remainig items left-over.
        while i < len(L):
            array[k] = L[i]
            i += 1
            k += 1
        
        while j < len(R):
            array[k] = R[j]
            j += 1
            k += 1
            
@timerfunc
def merge_sort_benchmark(array, print_=False):
    mergeSort(array, reverse=True)
    if print_:
        print("-"*50)
        print(" "*25+"OUTPUT"+" "*25)
        print("-"*50)
        print(*array, sep="\n")
@timerfunc
def insert_sort_benchmark(array, print_=False):
    insertSort(array, reverse=True)
    if print_:
        print("-"*50)
        print(" "*25+"OUTPUT"+" "*25)
        print("-"*50)
        print(*array, sep="\n")
@timerfunc
def buit_in_sort(array, print_=False):
    sorted(array)
    

def benchmark(tmp=[], tmp1=False):
    array = generateRandomStudent(100_000)    
    array_copy_1 = array[:]
    array_copy_2 = array[:]
    array_copy_3 = array[:]
    merge_sort_benchmark(array_copy_1, print_= False)
    insert_sort_benchmark(array_copy_2, print_= False)
    buit_in_sort(array_copy_3, print_ = False)

@timerfunc    
def exec_():
    print("Enter [1] To Perform Insertion Sort\nEnter [2] To Perform Merge Sort\nEnter [3] To Perform Benchmark (100 000 inputs)")
    n = input().strip("\r")
    
    array = []
    if n < "3":
        for i in range(int(input())):
            id_, name1_, name2_, credits_, cgpa_ = input().split()
            array.append(Student(int(id_), name1_+" "+name2_, int(credits_), float(cgpa_)))
        print("-"*50)
        print(" "*25+"INPUT"+" "*25)
        print("-"*50)
        print(*array, sep="\n")
        
    {'1': insert_sort_benchmark, 
    '2': merge_sort_benchmark, 
    '3': benchmark}[n](array, True)

if __name__ == "__main__":
    
    exec_()
    
    print("-"*50)
    #print(*array, sep="\n")
    
    