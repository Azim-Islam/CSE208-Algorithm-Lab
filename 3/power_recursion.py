def recursive_power(a, n):
    if n == 1:
        return a
    return a*recursive_power(a, n-1)


n = 6 #my id
a = int(input("Please input the base: ")) #input of base

print(recursive_power(a, n)) #printing our answer