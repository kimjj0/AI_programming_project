def func_factorial(n):
    if n == 1:
        return 1
    return n * func_factorial(n - 1)

print(func_factorial(6))