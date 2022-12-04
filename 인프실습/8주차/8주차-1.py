list = ['me', 45, 'c', 123987, 'awe', 22, [3,2,9]] #리스트 선언
list_iterator = list.__iter__() #list 이터레이터 생성
try:
    while True:
        print(list_iterator.__next__()) #내부 데이터를 모두 출력
except:
    print('모든 데이터를 꺼냈으므로 StopIteration 오류가 발생하였습니다.') #모두 다 꺼내면 에러문 출력
