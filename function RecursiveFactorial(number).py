def RecursiveFactorial(number):
    if number <= 1:
        return 1
    return number * RecursiveFactorial(number-1)


value = 10
f = RecursiveFactorial(value)
print(f"The factorial of {value} calculated with the recursive factorial function is {f}")