#**************************************** Package Imports ****************************************#

from functools import lru_cache
from random import choice, randint, sample
import time
import sys
#**************************************** Package Imports ****************************************#

sys.setrecursionlimit(10**8) #Setting the recursion limit to avoid crashes
number_of_notes = 999999999999 #Setting this to a big value so that we may compare it with lower values
amount = 0 #Initializing Variables
m = 0
coins = []

#**************************************** Timer Decorator To Calculated Spent Time ****************************************#
"""
    This Section Calculates the Run Time of Each Functions Dynamic and Greedy
"""
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
#**************************************** Timer Decorator To Calculated Spent Time ****************************************#


#**************************************** Coin Change Dynamic Solution START ****************************************#
"""
    Coin Change Dynamic Top Down Approach which shows The Most Optimal Ways To Create The Amount 
"""
@lru_cache(None)
def coin_change_dynamic(change, index, note_number, note_sack):
    global number_of_notes
    if change == 0: # When the change becomes 0, then we have found an solution which may or may not be optimal.
        if note_number <= number_of_notes:
            number_of_notes = note_number        
            print(f"Number of Notes In Dynamic: {note_sack} || SUM = {sum(note_sack)}")
        note_number = 0
        return 1
    if change < 0 or index >= m or coins[index] > change:
        note_number = 0
        return 0
    else:
        #We Try Excluding and Including Notes To Find The minimal Number of Notes and also the notes that are included.
        note_sack = list(note_sack) 
        note_sack.append(coins[index])
        note_sack_1 = note_sack[:]
        note_sack_1.pop()
        return coin_change_dynamic(change, index + 1, note_number, tuple(note_sack_1)) + coin_change_dynamic(change - coins[index], index, note_number+1, tuple(note_sack))
#**************************************** Coin Change Dynamic Solution END ****************************************#
    
    
#**************************************** Coin Change Greedy Solution START ****************************************#
"""
    Coin Change Dynamic Top Down Approach Which Shows The Greedy Way To Create The Amount 
"""
def coin_change_greedy(coins, amount):
    cpy_amount = amount
    number_of_notes = 0
    for note_value in coins:
        if amount//note_value >= 1: #5/2 = 2.5 and 5//2 = 2
            number_of_notes += amount//note_value
            print(f"Number of {note_value} taka notes required In Greedy: {amount//note_value}")
            amount -= amount//note_value * note_value
    print(f"Greedy Sum = {cpy_amount-amount}")
    return number_of_notes
#**************************************** Coin Change Greedy Solution END****************************************#



#**************************************** Benchmark Functions START ****************************************#
@timerfunc
def run_dynamic():
    global number_of_notes
    coin_change_dynamic(amount, 0, 0, tuple())
    print("-"*50)
    print(f"Minimum number of notes in Dynamic = {number_of_notes}")
    
@timerfunc
def run_greedy():
    print("-"*50)
    answer = coin_change_greedy(coins_desc, amount)
    print(f"Minimum number of notes in Greedy = {answer}")


def auto_input():
    #**************************************** Randomly Generating Data ****************************************#
    global amount, coins, m
    amount = int(input("Enter The Change To make\n$:")) #coin change to make
    m = int(input("Enter The Number of Available Notes (Randomly Generated From 1 to 101)\n$:")) #number of coins
    coins = sample(range(1, 101), k=m)
    

def manual_input():
    #**************************************** Input ****************************************#
    global amount, coins, m
    amount = int(input("Enter The Change To make\n$:")) #coin change to make
    m = int(input("Enter The Number of Available Notes\n$:")) #number of coins
    coins = list(map(int, input("Enter The Available Notes\n$:").split())) #the coins
    


mode = input("Input [1] For Auto-Generated Data Based Benchmark\nInput [2] For Manual Input Data Based Benchmark\n$:").strip()

{"1":auto_input, "2":manual_input}[mode]()
#**************************************** Benchmark Functions END ****************************************#
    
    
#**************************************** MAIN DRIVER CODE START ****************************************#


print("-"*50)
print(f"Amount To Create = {amount}")        
print(f"Notes Available = {coins}")
print("-"*50)

coins.sort()
coins_desc = sorted(coins, reverse=True)
print("-"*50)
run_dynamic() #Running the Dynamic Solution
print("-"*50)
run_greedy() #Running The Greedy Solution
#**************************************** MAIN DRIVER CODE END ****************************************#
