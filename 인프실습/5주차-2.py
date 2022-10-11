tuple1 = tuple(range(0,20,3)) #0부터 20전까지 3씩 증가하는 튜플 생성
print(tuple1)
tuple1 = list(tuple1) #튜플을 리스트 형태로 변환
tuple1.remove(0) #0 제거
tuple1 = tuple(tuple1) #리스트에서 튜플로 변환
print(tuple1)
tuple1 = tuple1 + tuple(range(21,32,3)) #튜플에 21부터 31까지의 3의 배수 추가
print(tuple1)
print(tuple1[2:9]*2) #9부터 27까지 3의 배수를 두번씩 출력
