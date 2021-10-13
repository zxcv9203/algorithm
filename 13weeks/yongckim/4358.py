import sys
input = sys.stdin.readline
tree = {}
cnt = 0
while True:
    tmp = input().rstrip()
    if not tmp:
        break
    if tmp in tree.keys():
    	tree[tmp] += 1
    else:
        tree[tmp] = 1
    cnt += 1
ans = sorted(tree.items())
for key, value in ans:
    print(key, "{:.4f}".format(value/cnt * 100))
