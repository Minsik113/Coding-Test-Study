'''
날짜:2022. 08. 29
시간복잡도:

문제:
풀이:
01:40 ~
'''
import sys
input = sys.stdin.readline

n, min_range, max_range = list(map(int, input().split()))
# 1. 맵 입력
arr = [list(map(int, input().split())) for _ in range(n)]
dx = [0,1] # 동남
dy = [1,0]
answer = 0

while True:
    cnt = 0 # 인구 차이가 범위안에 존재하는 인접도시의 개수
    x, y = 0, 0 # 현재 위치
    city = set()
    # 도시체크
    for i in range(n):
        for j in range(n):

            for k in range(2):
                nx = i + dx[k]
                ny = j + dy[k]
                if nx >= n or ny >= n:
                    continue
                else:
                    diff = abs(arr[nx][ny] - arr[i][j])
                    # print(min_range,arr[i][j],arr[nx][ny],diff,max_range)
                    if min_range <= diff and diff <= max_range:
                        # print('이동함',i,j,nx,ny)
                        cnt += 1 # 관계증가
                        city.add((arr[i][j],i,j))
                        city.add((arr[nx][ny],nx,ny))

    # 종료조건
    if cnt == 0:
        break
    else:
        proper_pop = 0
        city = list(city)
        for i in city:
            proper_pop += i[0]
        temp = proper_pop // (cnt+1)
        for i in city:
            arr[i[1]][i[2]] = temp
        answer += 1
        # print('>>')
        # print(arr)
        # print('>>')
print(answer)
    