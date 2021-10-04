# 2785 chain

import sys
input = sys.stdin.readline

n = int(input())
chain = list(map(int, input().split()))

chain.sort()

res = 0
while(1):
	if len(chain) == 1:
		break
	chain[len(chain)-2] = chain[len(chain)-1] + chain[len(chain)-2]
	del chain[len(chain)-1]
	chain[0]-=1
	res+=1
	n-=1
	if chain[0] == 0:
		del chain[0]
	
print(res)

	# 1. 1개면 break
	# 2. 맨 뒤에있는거랑 그 뒤의 앞에 있는거를 더해서 그 앞에 있는거에 저장
	# 3. 맨 뒤 삭제
	# 4. cnt++
	# 5. v[0]--
	# 6. if (v[0] == 0)
	# 7. 한칸씩 앞으로 값 복사
	# 8. 맨 뒤 삭제
