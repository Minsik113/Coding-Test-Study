'''
날짜: 2022. 08. 21
시간복잡도:

문제:
풀이:
1. 점들간의 거리차이 구한다. diff
2. 근접한 점들 중 거리가 제일 긴 점 A, B를 구한다
3. 한쪽 방향으로 제일 긴 dist를 붙이면서 다음점을 계산한다.
4. 정답

'''
def solution(n, weak, dist):
    answer = -1
    diff = []
    prev = 0
    for i in range(1,len(weak)):
        # (AB거리, A, B) = weak[i]-weak[prev],weak[i],weak[prev]
        diff.append((weak[i] - weak[prev], weak[i],weak[prev])) 
        prev += 1
    
        
            
        
    
    return answer