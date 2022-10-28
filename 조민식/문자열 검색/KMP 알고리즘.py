'''
https://developmentdiary.tistory.com/455

문자열의 가르키는 위치 i 패턴의 위치를 가르키는 j를 이용한다.
i는 1씩 증가하며 j는 일치할경우 증가시키고, 일치하지않을경우 j=table[j-1]로 위치를 
바꾸어 다시 비교한다.
j가 패턴의 끝에서 즉 len(P)-1과 같을때 T[i]와 일치한다면 문자열에서 패턴을 찾은
경우이다.

'''
import sys
input = sys.stdin.readline
# 뒤에 개행문자 제거
T = input().replace('\n','') # 문자열 
P = input().replace('\n','') # 패턴

KMPTable = [0 for _ in range(len(P))]
def MakeTable(P, KMPTable): # i:문자열, j:패턴
    j = 0
    for i in range(1, len(P)):
        while j > 0 and P[i] != P[j]: # 같지 않으면
            j = KMPTable[j-1] # 이전의 맞은 부분까지 돌아가서 다시비교
        if P[i] == P[j]: # 같다면
            j += 1 # j증가시키고
            KMPTable[i] = j # 테이블 갱신

def KMP(T, P, KMPTable):
    MakeTable(P, KMPTable)
    j = 0
    count = 0
    result = []
    P_size = len(P)
    for i in range(len(T)):
        while j > 0 and T[i] != P[j]: # 같지 않을때
            j = KMPTable[j-1] # 이전의 맞은 부분까지 돌아가서 비교
        if T[i] == P[j]: # 같으면
            if j == P_size-1:
                count += 1 # 개수 추가
                result.append(i-P_size+2) # 위치 추가
                j = KMPTable[j] # 위치를 옮겨주고 다시 탐색
            else: # j늘려준다
                j += 1
    return count, result


print(KMP(T, P, KMPTable))