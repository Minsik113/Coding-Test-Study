'''
그냥푼거랑 걸리는시간은 비슷한듯
'''
def solution(N, stages):
    result = dict()
    
    number_list = [0] * (N+2)
    for i in stages:
        number_list[i] += 1
    
    len_people = len(stages)
    for stage in range(1, N+1): # 1~마지막 스테이지
        if len_people != 0:
            result[stage] = number_list[stage] / len_people
            len_people -= number_list[stage] # 사람수빼고
        else:
            result[stage] = 0
    # 실패율 순서(result[x]). 값이 큰 애들부터
    return sorted(result, key=lambda x:result[x],reverse=True)