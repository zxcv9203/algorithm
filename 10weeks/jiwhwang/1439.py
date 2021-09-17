import sys

# 한줄에 띄어쓰기 없이 정수를 여러개 받을 때 2차원 배열로 저장
input_string = list(input())

# print(input_string)

short_v = ''
for i in range(len(input_string)):
    if i == 0:
        short_v += input_string[i]
    elif input_string[i-1] == input_string[i]:
        continue
    elif input_string[i-1] != input_string[i]:
        short_v += input_string[i]
# print('short_v = ', short_v)

toZero = 0
toOne = 0
if short_v[0] == '0': # 0을 1로 바꾸는 경우
    toOne = 1
else: # 1을 0으로 바꾸는 경우
    toZero = 1


for i in range(len(short_v)):
    if (short_v[i] == '0'):
        toOne += 1
    else: 
        toZero += 1

print(min(toZero, toOne))
