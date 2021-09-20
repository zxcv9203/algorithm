# 1946 신입 사원
import sys

tc = int(input())

for i in range(0, tc):
    cnt = 1 # 서류 1등 합격시 무조건 합격
    people = []

    num = int(input())
    for j in range(num):
        f, s = map(int, sys.stdin.readline().split())
        people.append([f, s])
    
    people.sort() # f(서류) 기준 오름차순

    # for i in range(num):
    #     print(people[i][0], people[i][1])

    min = people[0][1] 
    for k in range(1, num):
        if min > people[k][1]:
            cnt += 1
            min = people[k][1]
    print(cnt)



'''
1.  다른 모든 지원자와 비교했을 때 
    서류심사 성적과 면접시험 성적 중 적어도 하나가 다른 지원자보다는 떨어지지 않는 자만 선발

2. A가 서류도 B보다 안 좋고 면접도 안 좋으면 절대 선발되지 x
3. 선발할 수 있는 신입사원의 최대 인원 수

tc수
지원자 수
서류심사 성적, 면접 성적
'''
