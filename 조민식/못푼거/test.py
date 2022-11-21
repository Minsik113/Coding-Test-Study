# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
first, last = map(int,input().split())
d = int(input())

flag = False
while d > 0:
    if flag==False: # 시작
        if first % 2 == 1: # 홀수
            temp = first // 2 + 1
        else:
            temp = first // 2
        first -= temp
        last += temp
        flag = True
    else:
        if first % 2 == 1: # 홀수
            temp = last // 2 + 1
        else:
            temp = last // 2
        first += temp
        last -= temp
        flag = False
    
    d -= 1
    print(flag,d)


print(first, last)

