"""
출력 초과
import sys

N = int(sys.stdin.readline())
result = 0
temp = 0
test = []

test = [int(sys.stdin.readline()) for _ in range(N)]

test.sort()


for idx, x in enumerate(test):
    temp += x
    if idx > 1:
        result += result + temp
        temp = 0
    else:
        result += temp
        temp = 0

print(result)
"""

# list sort 와 heap push의 속도 차이
# heappush() 함수는 O(log(n))의 시간 복잡도를 가집니다.

import sys
import heapq

N = int(sys.stdin.readline())  # 나중에 Range로 사용해야하므로 int
deck = []
result = 0

for _ in range(N):  # deck에 힙으로 카드 추가
    heapq.heappush(deck, int(sys.stdin.readline()))

if len(deck) == 1:  # 카드 뭉치가 1개일 때 조합할 필요가 없으므로 조합의 수 0으로 반환
    print(0)
else:
    while len(deck) > 1:  # 카드 뭉치가 2개 이상일 경우 진행되며 deck가 1개가 되면 종료
        temp = heapq.heappop(deck) + heapq.heappop(deck)  # 가장 작은 요소 2개를 순서대로 뽑아 더한다.
        result += temp  # 더한 조합의 수를 결과에 포함시킨다.
        heapq.heappush(deck, temp)  # 더한 값을 다시 heap에 넣어 다음 연산을 진행한다.
    print(result)

