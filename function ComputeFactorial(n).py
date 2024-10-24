def ComputeFactorial(n):
    result = 1
    for x in range(n+1):
        result = x * result
    print(result)

input_from_user = ComputeFactorial(int(input("What would you liken to input")))