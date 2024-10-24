def FibonacciNumberPos(n):
    if n <= 1:
        return 1
    return FibonacciNumberPos(n-1) + FibonacciNumberPos(n-2)

user_input = 4
chnage_to = user_input - 1
print(FibonacciNumberPos(chnage_to))