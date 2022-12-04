f_in = input('파일 이름 : ') #f_in에 파일 이름 입력받음

try: #try-except문을 통한 에러문 종류별 출력
    file = open(f_in, 'r')
    datas = file.readlines() #datas에 한줄씩 저장
    print(datas[0] + datas[1], end='') #제목과 한줄 띄어쓰기 출력
    order = 1
    for line in datas[2:]:
        if line == 14: #모든 줄을 출력할 경우 반복문 종료
            break
        else:
            print(f' {order}: {line.strip()}') #한줄씩 순서 붙여서 출력
            order += 1

    f_in.close()

except IOError: #IOError인 경우를 따로 처리
    print(f'There is no file: {f_in}')

except: #입출력 에러를 제외한 나머지 에러 처리
    print('예상치 못한 에러입니다.')


