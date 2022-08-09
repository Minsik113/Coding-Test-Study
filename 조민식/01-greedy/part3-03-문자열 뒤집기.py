'''
날짜: 2022. 08. 09
시간복잡도: O(N)

문제: 
풀이: 이전 숫자랑 비교해서 같으면 넘어가고 다르면 숫자 증가?
'''
chars = input()
dict_num = dict()

dict_num[0] = 0
dict_num[1] = 0

# 예외1 - 입력받는거니까 입력안하는 경우는 없을듯
# 예외2 - 숫자1개만 들어오는경우도 생각 -> 그냥 진행해도될듯
prev = int(chars[0])
dict_num[prev] = 1

for i in range(1, len(chars)):
    now = int(chars[i])
    if prev != now: # 다르면 prev대체하고 지금 값증가
        prev = now
        dict_num[now] += 1
    else: # 같으면 그대로 진행
        pass

print(min(dict_num[0], dict_num[1]))