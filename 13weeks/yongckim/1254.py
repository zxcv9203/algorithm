s = input()
s_len = len(s)
for i in range(s_len):
    if s[i:] == s[i:][::-1]:
        print(s_len + i)
        break