import sys
sys = sys.stdin.readline
s = input()
st = 0
ed = 1
s_len = len(s)
while st < s_len :
    if s[st] == '<' :
        ed = st + 1
        while s[ed] != '>' :
            ed += 1
        print(s[st:ed+1], end="")
        st = ed
    else :
        ed = st + 1
        while ed < s_len and (s[ed] != '<' and s[ed] != ' ') :
            ed += 1
        if st == 0 :
            print(s[ed-1::-1], end="")
        else :
            print(s[ed-1:st:-1], end="")
        if ed < s_len and s[ed] == ' ' :
            print(s[ed], end="") 
        st = ed
    if st + 1 == s_len :
        st += 1
print()