'''
날짜: 2022.09.03
시간복잡도: O(nlogn)

문제:
풀이:
'''
import sys
input = sys.stdin.readline

n = int(input())
arr = [int(input()) for _ in range(n)]
sorted_arr = sorted(arr,reverse=True)
ans = ""
for i in sorted_arr:
    ans += str(i) + " "

print(ans.rstrip())