#Wiaux Bastien

def memoization():
    memo = {0: 0, 1: 1}

    def fib(n):
        if n not in memo:
            new_value = fib(n-1) + fib(n-2)
            memo[n] = new_value
        return memo[n]
    return fib

fib = memoization()
