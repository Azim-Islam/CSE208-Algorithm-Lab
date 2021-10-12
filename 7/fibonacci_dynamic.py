from collections import defaultdict
from functools import lru_cache
import time

import sys
sys.setrecursionlimit(10_000_000)

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



#Nth value gets saved inside a dictionary
get_n = {0:0, 1:1}
def fibonacci_dynamic(n):
    if n in get_n:
        return get_n[n]
    get_n[n] = fibonacci_dynamic(n - 1) + fibonacci_dynamic(n-2)
    
    return get_n[n]

#Using LRU (Least Recently Used) CACHE to save the Nth term.
@lru_cache
def fibonacci_dynamic2(n):
    if n < 2:
        return n
    else:
        return fibonacci_dynamic2(n-1) + fibonacci_dynamic2(n-2)

def fibonacci(n):
    if n < 2:
        return n
    else:
        return fibonacci_dynamic2(n-1) + fibonacci_dynamic2(n-2)
    
    
#Taking input
n = int(input("Nth term: "))

#Proxy functions to run the benchmark | non dynamic, dynamic, dynamic2
@timerfunc
def non_dynamic(n):
    for i in range(0, n):
        print(fibonacci(i), end=" ")
        #fibonacci(i)
    print("\n")
        
@timerfunc
def dynamic1(n):
    for i in range(0, n):
        print(fibonacci_dynamic(i), end=" ")
        #fibonacci_dynamic(i)
    print("\n")
    
@timerfunc
def dynamic2(n):
    for i in range(0, n):
        print(fibonacci_dynamic2(i), end=" ")
        #fibonacci_dynamic2(i)
    print("\n")
    
    
#Running the benchmark and printing the results
print(non_dynamic(n))
print(dynamic1(n))
print(dynamic2(n))