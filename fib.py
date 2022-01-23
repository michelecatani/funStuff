
## get input and convert to int

val = int(input("Enter your value: "))

## create a memo list

memo = []

## fill memo with -1 up to the 100th index

for i in range(100):
    memo.append(-1)

## define a function that will get you your fib number

def fib(n: int):
    if n < 2:
        return n
    
    if memo[n] != -1:
        return memo[n]
    
    memo[n] = fib(n-1) + fib(n-2)
    return memo[n]

print(fib(val))



