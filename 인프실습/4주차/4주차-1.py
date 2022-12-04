
mystring = """
Tomorrow - Dongju Yun
People kept talking about tomorrow;
So I asked them what it is.
They told me that tomorrow will be 
When night is gone and dawn comes.
Anxiously waiting for a new day,
I slept through the night and
woke up to learn
that tomorrow was no more --
It was another today.
Friends,
There is no such a thing
As tomorrow
"""

mystring = mystring.splitlines()
print(mystring)
print("\n")
mystring = mystring[3] + mystring[10]
print(mystring, end='')
count_t = mystring.count('t') # 문자 t의 개수
index_what = mystring.find('what') # 'what'의 시작 인덱스 위치
index_son = mystring.find('son') # 'son'의 시작 인덱스 위치 없으면 -1 반환
print(f'문장에서 t의 개수 : {count_t}\nmystring 리스트 "what" 시작 Index 위치: {index_what}, son 시작 index 위치: {index_son}')

