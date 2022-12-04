for i in range(1, 51):
    is_Prime = True
    if i == 1:
        is_Prime = False
    for j in range(2, i):
        if i % j == 0:
            is_Prime = False
            break
    if is_Prime == True:
        print(i,end=" ")