from functools import lru_cache

@lru_cache
def fibonacci_number(n0, n1, i): #printing the nTh fibonacci number
    if i < 2:
        return 1
    return n0+fibonacci_number(n1, n0+n1, i-1)

@lru_cache
def full_series(nth): #printing the nTh fibonacci series
    if nth < 1:
        print(0, end=" ")
        return 
    full_series(nth - 1)
    print(fibonacci_number(0, 1, nth), end=" ")


full_series(int(input()))