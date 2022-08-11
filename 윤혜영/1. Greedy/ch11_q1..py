# Q1. 모험가 길드
import time
start_time = time.time() # 측정 시작

# 1. 입력값
N = int(input('모험가는 몇 명입니까? ->'))
user_list = list(map(int, input('모험가의 정보를 입력하세요. ->').split()))

# 최대값을 넘지 않는 모험가 리스트
sorted_list = sorted(user_list, reverse=True)  # 내림차순으로 리스트 정렬

# 1) 리스트를 정렬한 후 최대값 개수만큼 리스트 자르는 함수
def max_cutter(list):
    if len(list) == 0:
        max_in_list = 0
        tmp = []
    else:
        max_in_list = max(sorted_list) # 리스트 내 최댓값
        tmp = sorted_list[:max_in_list]
    return tmp

# 2) 자른 리스트를 삭제하는 함수
def drop_list(tmp):
    if len(sorted_list) > len(tmp):
        for i in tmp:
            del sorted_list[tmp.index(i)]
    elif len(sorted_list) == len(tmp):
        del sorted_list[:]
    return(sorted_list)

# 1-2를 반복하는 함수
def group_count(list):
    count = 0
    while len(list) > 0:
        X = max_cutter(list)
        count += 1
        drop_list(X)
    print(count)

group_count(sorted_list)

end_time = time.time() # 측정 종료
print('time :', end_time - start_time)