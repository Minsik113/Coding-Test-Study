'''
날짜: 2022. 09. 19
시간복잡도:

문제: https://www.acmicpc.net/problem/18353
풀이:
01:05 ~ 

dp[i] = i까지의 최대값
dp[i] = max(dp[i], 앞에꺼 모두)

LIS(longest increasing subsequence)
:가장 긴 증가하는 부분 수열 = 가장 긴 감소하는 부분 수열
dp[i] = arr[i]를 마지막원소로 가지는 부분 수열의 최대 길이.
모든 0<=j<i에 대하여, dp[i] = max(dp[i], dp[j]+1) if arr[j]<arr[i]
앞에 있는 원소가 뒤에있는 원소보다 작을 떄만 가능. -> 증가하는 부분수열이니까


테스트 값
7
15 11 4 8 5 2 4
->2

3
1 5 7
->2
'''

# n = int(input())
# arr = list(map(int, input().split()))
# dp = [0] * n  # 전투력 저장
# dp[0] = arr[0]

# cnt = 0 # 사람수
# for i in range(1, n):
#     if arr[i-1] > arr[i]: # 현재가 이전보다 작으면 그대로 더함
#         dp[i] = dp[i-1] + arr[i]
#     elif arr[i-1] == arr[i]: # 전투력 같으면 빼야지
#         cnt += 1
#     else: # 현재가 이전보다 크면 뒤부터 봐야함
#         # print('발견',i)
#         save = arr[i]
#         for j in range(i-1,0,-1):
#             save = max(save, arr[j])
#             if arr[j] > arr[i]: # 이전꺼 > 현재 인 부분찾아서
#                 # print(i,j,'일때 고쳐')
#                 dp[i] = max(dp[i-1], dp[j]+arr[i]) # max(이전꺼, 걸리는곳)
#                 break
#         # 안바뀌었다면
#         if dp[i] == 0:
#             dp[i] = save
#         cnt+=1

# # print(dp)
# print(cnt)
