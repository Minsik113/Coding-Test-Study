# 3-3 :문자열 압축

def solution(s):
    answer = len(s)


    for i in range(1, len(s)//2+1):
        count = 1 #변수로 길이 파악
        prev= s[0:i]
        compressed = 0 #실제문자열보다 길이만 담는 변수

        for j in range(i, len(s)+i, i):
            curr = s[i+j]
            if curr == prev:
                count +=1
            else:
                compressed += len(str(count)+prev) if count>1 else len(prev)
                prev = curr

        answer = min (answer, compressed)
    return answer
