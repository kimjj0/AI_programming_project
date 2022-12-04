def func_A(a, b):
    if a > b:
        print(f'{b}은 (는) {a}보다 작다.')
    elif a < b:
        print(f'{a}은 (는) {b}보다 작다.')
    else:
        print(f'두 수는 {a}로 같다')

func_A(10, 17)