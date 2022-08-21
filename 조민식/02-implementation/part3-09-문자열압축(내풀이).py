'''
날짜: 2022. 08. 20
시간복잡도: 500*1000

문제:
풀이:
22:51~24:05 -> 1시간15분
조건1. 무조건 맨앞부터 자른다. # 1개씩자르던 2개씩자르던 k개씩자르던 맨앞부터자름.
조건2. 자를때 나눈애들이 정확히 나누어 떨어지지않아도 됨. 뒤는 이어붙임.;;
'''
def solution(s):
    answer = 1e9
    if len(s)==1:
        return 1
    len_half = len(s) // 2 
    len_s = len(s)

    total = []
    divide_num = 0 # 나누는 수 -> 1~len(s)//2까지
    while True:
        ans = []
        divide_num += 1
        # 1. 종료조건
        if divide_num > len_half: # s길이의 반까지 나눌 수 있으니까 넘으면 종료
            # print("종료")
            break
        # 2. 나누어 떨어지지 않으면 -> 뒷부분은 그냥 이어붙여야한다
        least_plus = False
        if len_s % divide_num != 0:
            # print(f'나누어 안떨어짐 {len_s} % {divide_num}')
            least_plus = True
        # 2-1. divide_num의 간격만큼 s를 나눈다.
        cnt = 0
        for i in range(len_s // divide_num + 1): # s길이의 절반까지 나눌 수 있다.
            while cnt + divide_num <= len_s:
                ans.append(s[cnt:cnt+divide_num]) # 0:2 2:4 4:6 6:8
                cnt += divide_num
        # 2-2. 나누어떨어지지 않은 경우 뒷부분 그냥 이어붙임
        if least_plus:
            ans.append(s[cnt:])

        # print('>>>>',ans)

        total.append(ans)
        # 4. 같은 알파벳은 숫자로 더해줌
        result = ''
        cnt = 1 # 중복된애 개수
        flag = False # [예외처리] 
        prev = 0 # 2개씩 구분할거니까 앞을 지칭할 변수
        for i in range(1, len(ans)):
            # 5-1. 2개가 같다 -> cnt 증가
            if ans[prev] == ans[i]: # ans[-1]이 ans[-2]와 동일하게 끝났다 -> 따로 추가해줘야함 -> false
                cnt += 1
                flag = False
            # 5-2. 2개가 다르다 -> cnt+앞알파벳 출력
            else:
                if cnt == 1:
                    result += ans[prev]
                else:
                    result += str(cnt)+ans[prev]
                cnt = 1
                flag = True # 동일하게 끝나지 않았다 -> true
                prev = i

        if not flag:
            if cnt == 1:
                result += ans[prev]
            else:
                result += str(cnt)+ans[prev]
        else:
            result += ans[i]
        answer = min(answer, len(result))
    #     print(f'정답 {result}')
    # print(total)
        
    return answer