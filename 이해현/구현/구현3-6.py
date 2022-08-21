def possible(ans):
    for i in ans:
        x,y,type = i
        if type == 0:
            # 바닥 위
            if y==0 :
                continue
            # 보의 한 쪽 끝 위
            if [x-1,y,1] in ans or [x,y,1] in ans :
                continue
            # 다른 기둥 위
            if [x,y-1,0] in ans :
                continue
        else :
            # 한쪽 끝이 기둥 위
            if [x,y-1,0] in ans or [x+1,y-1,0] in ans :
                continue
            # 양쪽 끝이 다른 보와 연결
            if [x-1,y,1] in ans and [x+1,y,1] in ans :
                continue
        return False

    return True
def solution(n, build_frame):
    answer = []
    for i in build_frame:
        if i[3] == 0 :
            answer.remove([i[0],i[1],i[2]])
            # 삭제
            if not possible(answer) :
                answer.append([i[0],i[1],i[2]])

        else :
            answer.append([i[0],i[1],i[2]])
            # 설치
            if not possible(answer):
                answer.remove([i[0],i[1],i[2]])

    answer.sort()
    return answer