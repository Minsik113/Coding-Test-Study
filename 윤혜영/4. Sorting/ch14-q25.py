# p.361 실패율

def solution(N, stages):
    count = [0] * (max(stages) + 1) # 필요한 값에 대한 인덱스 생성

    for i in range(len(stages)):
        count[stages[i]] += 1  # 각 인덱스 값에 대한 숫자 확인

    # 도달한 인원 수 확인
    success = []
    for i in range(len(count)):
        if i == 0:
            tmp = len(stages) - count[i]
        else:
            tmp -= count[i - 1]
        success.append(tmp)

    # 다음 단계로 넘어가지 못한 인원 수를 도달 인원 수로 나눠서 실패율 계산
    fail_rate = []
    for i in range(len(success)):
        tmp = count[i] / success[i]
        fail_rate.append((i, tmp))

    # 0과 6(N+1)은 삭제하고 fail_rate 값을 기준으로 내림차순 정렬
    fail_rate = sorted(fail_rate[1:N+1], key=lambda k: k[1], reverse=True)

    # 정답 리스트 생성 및 반환
    answer = []
    for i in fail_rate:
        answer.append(i[0])
    return answer

print(solution(5, [2, 1, 2, 6, 2, 4, 3, 3]))
print(solution(4, [4, 4, 4, 4, 4]))