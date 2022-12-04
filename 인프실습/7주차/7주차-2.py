i = 1
chance = 3 #숫자 입력 횟수
while True:
    print("=============================")
    try: #실행 코드
        print(f'{i}번째 실행 결과입니다.')
        num = int(input('숫자 입력: '))
        chance -= 1 # 숫자면 기회 1 감소
        print(f'{num}이(가) 입력되었습니다.   남은 숫자 입력 횟수: {chance}')
        i += 1 # 실행 횟수 증가
    except: # 예외 발생 시 실행되는 코드
        print(f'숫자가 아닙니다.   남은 숫자 입력 횟수: {chance}')
        i += 1 # 실행 횟수 증가
    if chance == 0: # 숫자 입력 횟수가 0이 되면 반복문 나감
        break
print("=============================")

