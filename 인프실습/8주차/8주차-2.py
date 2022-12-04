def convert(a, b):
    strings = "0123456789ABCDEF" #15까지 저장해놓음
    if a < b:
        return strings[a]
    else:
        return convert(a // b, b) + strings[a % b] #재귀를 통해 변환한 수 구하기
decimal = int(input("10진수 입력: ")) #10진수 수 입력
num = int(input("변환 진수 입력:")) #변환하고 싶은 진수 입력
print(str(num)+"진수 변환: " + convert(decimal, num)) #convert함수를 통해 나온 값 출력