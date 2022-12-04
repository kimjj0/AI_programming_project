import re

regex = re.compile('\d\d\d-\d\d\d\d-\d\d\d\d') #정규표현식 사용
f_in = open("contact.txt", "r")
datas = f_in.readlines() #한 줄씩 읽어옴
for i in range(len(datas)):
    data = datas[i]

    try:
        find = regex.search(data).group(0) #일치하는거 찾음
        start = regex.search(data).start(0) #찾은 것의 시작 인덱스
        end = regex.search(data).end(0) #찾은 것의 마지막 인덱스
        print("해당 문서에서 존재하는 전화번호는 '%s' 입니다." % (find))
        print("%d번 line에서 (%d, %d)에 위치하는 전화번호 입니다." % (i+1, start, end))

    except: #에러나면 그냥 무시
        pass

f_in.close()


