# [함수1] 군형잡힌 괄호 문자열 인덱스
def balanced_index(p):
    count = 0 # 왼쪽 괄호 개수
    for i in range(len(p)):
        if p[i] == '(':
            count += 1
        else:
            count -= 1
        if count == 0:
            return i
#[함수2] 올바른 괄호 문자열인가
def check(p):
    count = 0 # 왼쪽 괄호 개수
    for i in p:
        if i == '(':
            count += 1
        else:
            if count == 0:
                return False 
            count -= 1
    return True

def solution(p):
    answer = ''
    if p == '':
        return answer

    index = balanced_index(p)
    u = p[:index+1]
    v = p[index+1:]
    if check(u):
        answer = u + solution(v)
    else:
        answer = '('
        answer += solution(v)
        answer += ')'
        u = list(u[1:-1])
        for i in range(len(u)):
            if u[i] == '(':
                u[i] = ')'
            else:
                u[i] = '('
        answer += ''.join(u)

    return answer