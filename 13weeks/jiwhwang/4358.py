import sys
input = sys.stdin.readline


total = 0

america = {}

while (1):
    b = input().strip()
    if not b:
        break
    if b in america:
        america[b] += 1
    else:
        america[b] = 1
    total+=1

america_list = list(america.keys()) # dict_keys 객체를 리스트로 변환하려면 다음과 같이 하면 된다.
america_list.sort()
for k in america_list:
    print('{} {:.4f}'.format(k, (america[k]/total)*100))




# # input().rstrip() # 오른쪽 공백 삭제
