'''
날짜: 2022. 09. 06
시간복잡도: O(NlogN)

문제: https://school.programmers.co.kr/learn/courses/30/lessons/42889
풀이:
01:24 ~ 01:54  ㅡㅡ

실패율 = 스테이지에 도달했지만 아직 클리어하지 못한 사람 수 / 스테이지에 도달한 플레이어 수
N = 20만 -> O(NlogN)

테스트값
5, [2, 1, 2, 6, 2, 4, 3, 3]
'''
def solution(N, stages):
    answer = [] # 스테이지번호, 실패율(못깬사람/도달한사람) -> 나중에 실패율로 내림차순
    cnt = [0] * (N+2) # 각 스테이지에 위치한 사람 수. idx 0은 제외하고, N+1은 다 깬사람
    
    for i in stages:
        cnt[i] += 1
    
    total = len(stages) # 사람 수
    
    for i in range(1, N+2): # 1~ N+1
        answer.append([i, cnt[i]/total]) # 1번 스테이지 실패율
        total -= cnt[i] # 인원 수 감소
        if total <= 0:
            total = 1 # 나누기할때 0을 나누면 안되니까 이 이후로는 쭉 0나옴
    # print(answer)		[[1, 0.125], [2, 0.42857142857142855], [3, 0.5], [4, 0.5], [5, 0.0], [6, 1.0]]

    # 1~ N까지 실패율 비교
    arr = answer[:-1]
    arr.sort(key=lambda x:-x[1]) # O(NlogN)
    # print('->',arr)    -> [[3, 0.5], [4, 0.5], [2, 0.42857142857142855], [1, 0.125], [5, 0.0]]
    res = []
    for i in arr:
        res.append(i[0])
    return res