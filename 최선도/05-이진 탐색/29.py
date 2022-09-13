import sys

# 인덱스가 아닌 간격 기준으로 계산
N, C = map(int, sys.stdin.readline().split())
arr = [int(sys.stdin.readline()) for _ in range(N)]
arr.sort()  # 이진 분류는 sort가 된 상태로 실행 가능


def binary_search(start, end):
    answer = 0

    while start <= end:
        count = 1  # 처음 지점엔 무조건 공유기가 설치 되어있어야 한다.
        point = arr[0]  # 첫 지점
        mid = (start + end) // 2  # 중간 간격

        for x in range(1, len(arr)):
            if arr[x] >= point + mid:  # 첫지점 + 중간과 위치 비교
                point = arr[x]  # 공유기 추가 위치 지정
                count += 1

        if count >= C:
            start = mid + 1
            answer = mid
        else:
            end = mid - 1
    return answer


start = 1  # 최소 간격
end = arr[-1] - arr[0]  # 최대 간격
print(binary_search(start, end))

