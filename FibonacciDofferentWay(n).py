def FibonacciDofferentWay(n):
    x= 1
    y= 1
    if n <= 1:
        return 1
    for z in range(2, n+1):
        temp = x
        x= x + y 
        y = temp
    return x

print(FibonacciDofferentWay(8))