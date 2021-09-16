import sys
# sys.stdin = open("input.txt", 'r')
n = int(sys.stdin.readline()) 
array = []
# print(array)
# input
for i in range(n):
    array.append(list(map(int, sys.stdin.readline().split())))

# print(array)

answer = []

for i in range(n):
    max = 0
    for a in range(3):
        for b in range(a+1, 4):
            for c in range(b+1, 5):
                temp = array[i][a] + array[i][b] + array[i][c]
                if max <= temp%10:
                    max = temp%10
    answer.append(max)
# print (answer)

pp = 0
pi = 0
# 시작, 끝(포함x), +숫자
for i in range(n):
    if pp <= answer[i]:
        pi = i
        pp = answer[i]
print(pi+1)








'''
반복문으로 여러줄 입력 받는 상황에서는 반드시 sys.stdin.readline()을 사용

map은 리스트의 요소를 지정된 함수로 처리해주는 함수 (원본을 수정하지않고 새 리스트 생성)
    a = list(map(int, a)) -> float 리스트를 int 리스트로
    a = list(map(str, a)) -> int 리스트를 str 리스트로


1) 임의의 개수의 "정수"를 "한줄에" 입력받아 리스트에 저장
    data = list(map(int,sys.stdin.readline().split()
2) 임의의 개수의 "정수"를 "n줄 입력받아 2차원 리스트"에 저장
    data = []
    n= int(sys.stdin.readline())
    for i in range(n):
        data.append(list(map(int, sys.stdin.readline().spilt())))
3) 문자열 n줄을 입력받아 리스트에 저장할때
    n = int(sys.stdin.readline())
    data = [sys.stdin.readline().strip for i in range(n)]
     # strip()은 문자열 맨 앞과 맨 끝의 공백문자를 제거
'''
