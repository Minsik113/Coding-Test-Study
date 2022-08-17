'''
날짜: 2022. 08. 17
시간복잡도: 완전탐색, O(N^4)시간안에됨.

문제:
풀이:
2N+M-2 x 2N+M-2 크기로 연장
0~N-1, N+M+1~2N+M-2 까지는 0 으로채운다
가운데부분본다
안되면 돌리기 -> 총4번
'''
# [함수 1] 반시계로 회전
def turn_left(key):
    l = len(key[0])
    array = [[0 for _ in range(l)] for _ in range(l)]
    for i in range(l):
        for j in range(l):
            array[l-j-1][i] = key[i][j]
    return array

def solution(key, lock):
    len_key = len(key[0])
    len_lock = len(lock[0])
    # 1.맵 생성
    arr = [[0 for j in range(2*len_key+len_lock-2)] for _ in range(2*len_key+len_lock-2)] # 원본
    # 2.맵에 자물쇠입력
    for i in range(len_lock):
        for j in range(len_lock):
            arr[i+len_key-1][j+len_key-1] = lock[i][j]
    # 3.열쇠끼워넣기
    len_arr = len(arr[0])
    count = 0 # 자물쇠 회전 4번
    answer = False
    while True:
        # 3-1.종료조건
        if count == 4 or answer:
            break
            
        for x in range(len_arr-len_key+1): # 0~전체에서열쇠길이만큼뺀곳
            for y in range(len_arr-len_key+1):
                # 3-2.열쇠 끼워넣기
                for i in range(len_key):
                    for j in range(len_key):
                        arr[x+i][y+j] += key[i][j]
                # 3-3.자물쇠 확인해보기
                # print(arr)
                cnt_one = 0
                for i in range(len_key-1, len_key+len_lock-1): # 2~4
                    for j in range(len_key-1, len_key+len_lock-1):
                        if arr[i][j] == 1:
                            cnt_one += 1
                            # print(f'{i},{j}, {arr[i][j]}')
                # print(key)
                # 3-4.모두 1이면 종료        
                if cnt_one == len_lock*len_lock: # 모두 1이면 종료
                    answer = True
                    # print(count,cnt_one,'일때 정답나옴')
                    # print(arr)
                # 3-4-1. 모두 1이 아니라면 원상복구
                else:                    
                    for i in range(len_key):
                        for j in range(len_key):
                            arr[x+i][y+j] -= key[i][j]
        # 3-5. 답이안나왔으면 회전
        if not answer:
            key = turn_left(key)
            count += 1
        
    return answer