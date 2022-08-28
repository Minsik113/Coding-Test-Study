'''
날짜: 2022. 08. 29
시간복잡도:

문제:
풀이: 말 그대로 구현하면됨.
00:33 ~ 01:17 -> 44분
'''
from collections import deque
# [함수1] 들어온 문자열을 나눠라 -> 올바른 괄호 문자열, 나머지
def split_uv(p):
    q = deque(p)
    lcount = 0
    rcount = 0
    cnt = 0 
    while p:
        # 종료조건: 개수 동일
        if lcount==rcount and lcount >= 1:
            break
        t = q.popleft()
        if t == '(':
            lcount += 1
        else:
            rcount += 1
        cnt += 1
    return p[:cnt],p[cnt:]
# [함수2] 들어온 문자열이 '올바른 괄호 문자열'인가?
def check(q):
    arr = []
    for i in range(len(q)):
        if len(arr) > 0 and arr[-1]=='(' and q[i] == ')': # arr가 존재하고 arr맨위가 ''인데 들어온게')'라면 성공
            arr.pop()
        else: # 실패하면 추가
            arr.append(q[i])
    if len(arr) == 0: # 올바른 괄호 문자열
        return True
    return False

def solution(p):
    answer = ''
    # 1
    if len(p) == 0:
        return ""
    # 2. u:균형잡힌문자열,v:올바른문자열
    u, v = split_uv(p)
    print(u,v)
    # 3. u가 올바른문자열이면 -> v에 대해 1,2,3 재실행
    if check(u):
        u += solution(v) # 3.1 맞다면 v에 대해 1,2,3실행
        return u
    # 4.
    else:
        q = '(' # 4-1
        q += solution(v)
        q += ')'
        print(f'real u: {u}')
        u = u[1:-1] #4-3.
        print(f'after u: {u}')
        save = ''
        for i in u: # 4-4
            if i=='(':
                save+=')'
            else:
                save+='('
        print('>>>',answer)
        return q+save
