Sentence = input('문자열 입력 : ')
Sentence = Sentence.strip() #양 옆 공백 지움
print(Sentence)
Sentence = Sentence[:12] + Sentence[15:17] + Sentence[19] + Sentence[21] #문자열 슬라이싱
print(Sentence)
print('변경된 문자열의 길이:',len(Sentence)) #len함수로 문자열 길이 출력

print(Sentence.lower()) #소문자 출력
print(Sentence.upper()) #대문자 출력
print(Sentence.replace("Hody", "김지호"))

"""
2번째 방법
S = list(Sentence) #Sentence를 S라는 리스트로 변형
del(S[8:]) #Mr. Hody 삭제
S.append('MR. 김지호') #자신 이름 추가
print("".join(S)) #리스트 요소들 이음
"""

"""
3번째 방법
for i in S:
     print(i, end='')
"""
