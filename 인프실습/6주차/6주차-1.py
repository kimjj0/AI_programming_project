N = int(input('끝 숫자 입력: '))
sum = 0
for i in range(1, N+1): #1부터 N까지 반복
    if i % 2 == 1: #홀수 조건
        sum += i
        if i < N-1:
            print(i, end=" + ") #'+'로 이어서 print
        else:
            print(i, end=" = ") #sum 출력할  때 '='로 이어 출력
print(sum)





