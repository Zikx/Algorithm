'''
```python 
문제 1 
인코딩문제
	섬으로 향하라!

	'   + -- + - + -   '
	'   + --- + - +   '
	'   + -- + - + -   '
	'   + - + - + - +   '

해(**1**)와 달(**0**),
Code의 세상 안으로!(**En-Coding**)
```

+ 는 1 로 
- 는 0 으로 변환할 것
'''

import subprocess

text = ['   + -- + - + -   ',
        '   + --- + - +   ',
        '   + -- + - + -   ',
        '   + - + - + - +   ']
# rtnTxt = list()

# for txt in text:
	# rtnTxt.append(chr(int(txt.strip().replace(' ','').replace('+','1').replace('-','0'),2)))

# print(f''.join(rtnTxt))

# Using List Comprehension

rtnTxt = [chr(int(i.strip().replace(' ','').replace('+','1').replace('-','0'),2)) for i in text]
# print(''.join(rtnTxt))


# list comprehension
# [i for i in range(10) if i % 2 == 0 ] 
# print([f'{i} X {j} = {i*j}' for i in range(1,10) for j in range(1,10)])


# Built in Function
# .zfill()
# 특정 문자열 자리를 맞춰줌
# '111'.zfill(10)

s = [i.strip().replace(' ','').replace('+','1').replace('-','0') for i in text]

print(list(map(lambda x: chr(int(x, 2)), s)))