mylist = [37, 4, 16, 13, 29]
print(mylist)
del mylist[2] #3번째 원소 삭제
print(mylist)
mylist.append(47) #정수 47 추가
mylist.sort() #리스트 정렬
print(mylist)
mylist.reverse() #리스트 반전
print(mylist)
print('mylist의 평균값:', sum(mylist)/len(mylist)) #리스트 원소의 합을 리스트 길이로 나누어 평균 계산
print('mylist의 최솟값:', min(mylist)) #리스트 최솟값 출력
print('mylist의 최댓값:', max(mylist)) #리스트 최댓값 출력
