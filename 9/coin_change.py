#**************************************** Package Imports ****************************************#

from functools import lru_cache
from random import choice, randint, sample
import time
import sys
#**************************************** Package Imports ****************************************#

sys.setrecursionlimit(10**8) #Setting the recursion limit to avoid crashes

#**************************************** Input ****************************************#
amount, m = map(int, input().split()) #m = number of coin types
coins = list(map(int, input().split()))
#**************************************** Input ****************************************#


#**************************************** Randomly Generating Data ****************************************#
# amount = 250 #coin change to make
# m = 10 #number of coins
# coins = sample(range(1, 101), k=m)
#**************************************** Randomly Generating Data ****************************************#


coins.sort()
coins_desc = sorted(coins, reverse=True)

number_of_notes = 999999999999

#**************************************** Timer Decorator To Calculated Spent Time ****************************************#
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

#**************************************** Coin Change Dynamic Solution ****************************************#
@lru_cache(None)
def coin_change_dynamic(change, index, note_number, note_sack):
    global number_of_notes
    if change == 0:
        if note_number <= number_of_notes:
            number_of_notes = note_number        
            print(f"Number of Notes In Dynamic: {note_sack} || SUM = {sum(note_sack)}")
        note_number = 0
        return 1
    if change < 0 or index >= m or coins[index] > change:
        note_number = 0
        #note_sack = []
        return 0
    else:
        #We Try Excluding and Including Notes To Find The mininmal Number of Notes
        note_sack = list(note_sack) 
        note_sack.append(coins[index])
        note_sack_1 = note_sack[:]
        note_sack_1.pop()
        return coin_change_dynamic(change, index + 1, note_number, tuple(note_sack_1)) + coin_change_dynamic(change - coins[index], index, note_number+1, tuple(note_sack))
#**************************************** Coin Change Dynamic Solution ****************************************#
        
#**************************************** Coin Change Greedy Solution ****************************************#
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
#**************************************** Coin Change Greedy Solution ****************************************#

print(f"Amount To Create = {amount}")        
print(f"Notes Available = {coins}")

#**************************************** Benchmark Functions ****************************************#
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
    

run_dynamic()
run_greedy()
#**************************************** Benchmark Functions ****************************************#
