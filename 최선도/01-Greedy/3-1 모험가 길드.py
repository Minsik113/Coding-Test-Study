from time import time

n = int(input()) # 총 인원
x = [int(x) for x in input()] # 공포도
x.sort() # 리스트 x 정렬 

start_time = time()  # 측정 시작

cnt = 0 # 개별 그룹 카운트용
result = 0 # 전체 그룹 수

for i in x:
    cnt += 1 # 개별 그룹에 일단 포함
    if i <= cnt: # 개별 그룹 수가 i보다 크거나 같으면 다음 그룹원 모집 아니면 그룹원 모집 마감
        result += 1
        cnt =0
        
print(result)
print(f'{(time() - start_time):.2f}')
