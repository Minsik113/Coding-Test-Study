"""
프로그래머스 92점..
from collections import Counter

def solution(N, stages):
    dic = {}
    count = Counter(stages)
    challenger = len(stages)
    for x in range(1, len(stages)+1):
        if count.get(x) != None:
            value = count.get(x)
            fail = value / challenger
            challenger -= value
        else :
            fail = 0
        if (len(dic) < N):
            dic[x] = fail
        else:
            break
    sort_dic = sorted(dic.items(), key=lambda item : item[1], reverse=True)
    answer = [x[0] for x in sort_dic]
    return answer
"""


def solution(N, stages):
    failure_rate = {}
    stages_len = len(stages)

    for i in range(1, N + 1):
        if stages_len != 0:
            stage_count = stages.count(i)
            failure_rate[i] = stage_count / stages_len
            stages_len -= stage_count
        else:
            failure_rate[i] = 0

    answer = sorted(
        failure_rate.keys(), key=lambda key: failure_rate[key], reverse=True
    )

    return answer

