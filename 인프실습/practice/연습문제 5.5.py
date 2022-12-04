def func_Fibonacci(num):
    a = 0
    b = 1
    for i in range(num):
        a, b = b, a + b
    print(a)

func_Fibonacci(10)