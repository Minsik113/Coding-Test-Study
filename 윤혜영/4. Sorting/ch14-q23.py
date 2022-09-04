# p.359 국영수

n = int(input()) #학생수

score_data = []
for _ in range(n):
    score = input().split() # 이름 국어 영어 수학
    score_data.append((score[0], int(score[1]), int(score[2]), int(score[3])))

score_data.sort(key=lambda k: (-k[1], k[2], -k[3], k[0]))

for score in score_data:
    print(score[0])

# 점수를 비교하는 함수 생성 - if 써서 해보려고 했는데, name은 어떻게 해야할 지 모르겠음.
# 이 때는 위의 score_data.append를 튜플이 아닌 리스트로 설정해줘야 함

# def compare_score(list):
#     result = sorted(list, key=lambda k:k[1], reverse=True) # 국어 점수 기준으로 내림차순 정렬
#     for i in range(len(result)):
#         if i == 0:
#             continue
#         else:
#             if result[i][1] == result[i-1][1]:
#                 if result[i][2] < result[i-1][2]:
#                     result[i], result[i-1] = result[i-1], result[i]
#                     if result[i][2] == result[i-1][2]:
#                         if result[i][3] < result[i-1][3]:
#                             result[i], result[i-1] = result[i-1], result[i]
#
#     return result
#
# for i in range(len(score_data)):
#     print(compare_score(score_data)[i][0])
#
# 12
# Junkyu 50 60 100
# Sangkeun 80 60 50
# Sunyoung 80 70 100
# Soong 50 60 90
# Haebin 50 60 100
# Kangsoo 60 80 100
# Donghyuk 80 60 100
# Sei 70 70 70
# Wonseob 70 70 90
# Sanghyun 70 70 80
# nsj 80 80 80
# Taewhan 50 60 90