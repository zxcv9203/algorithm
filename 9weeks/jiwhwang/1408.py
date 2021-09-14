
one = (input())
two = (input())


O = one.split(":")
T = two.split(":")

if T[0] < O[0]:
    hour = int(T[0]) + 24 -int(O[0])
    min = int(T[1])-int(O[1])
    sec = int(T[2])-int(O[2])
    if sec < 0:
        min-=1
        sec+=60
    if min < 0:
        hour -= 1
        min += 60
    if hour < 0:
        hour = 0
else:
    hour = int(T[0])-int(O[0])
    min = int(T[1])-int(O[1])
    sec = int(T[2])-int(O[2])
    if sec < 0:
        min-=1
        sec+=60
    if min < 0:
        hour -= 1
        min += 60
    if hour < 0:
        hour = 0
print(str(hour).zfill(2),':',str(min).zfill(2),":",str(sec).zfill(2), sep='')
