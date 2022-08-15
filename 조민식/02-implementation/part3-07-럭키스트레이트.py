'''
날짜: 2022.08.16
시간복잡도: 

문제:
풀이:
'''
import sys
s = sys.stdin.readline().rstrip()
len_s = len(s) # O(1)

sum_left = 0
sum_right = 0
for i in range(len_s//2):
    sum_left += int(s[i])
for i in range(len_s//2, len_s):
    sum_right += int(s[i])

if sum_left == sum_right:
    print("LUCKY")
else:
    print("READY")