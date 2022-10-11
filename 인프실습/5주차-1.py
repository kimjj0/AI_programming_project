set1 = {30, 20, 10, 40, 60, 20, 50, 10}
set2 = {50, 20, 10, 70, 10 ,40, 50}
set3= {10, 20, 30}

print(f'set1: {set1}, set2: {set2}')
print(f'set1과 set2의 교집합: {set1.intersection(set2)}') #set1과 set2의 교집합
print(f'set1과 set2의 합집합: {set1.union(set2)}') #set1과 set2의 합집합
print(f'set1과 set2의 차집합1: {set1.difference(set2)}') #A-B
print(f'set1과 set2의 차집합2: {set2.difference(set1)}') #B-A
print(f'set3가 set1의 부분집합인가요?: {set1.issuperset(set3)}')
print(f'set3가 set2의 부분집합인가요?: {set2.issuperset(set3)}')
set2.update([30, 60]) #set2 집합에 30, 60 추가
print(set2)
set1.remove(50) #set1 집합에서 50 제거
set1.remove(60) #set1 집합에서 60 제거
print(set1)