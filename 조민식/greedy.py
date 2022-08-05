import random

name_list = ['김빈', '이해현', '성미래', '최선도', '조민식', '홍성훈','이진웅', '윤혜영', '정진', '박희정', '송유림', '장윤식']

k = int(input())

for i in range(k):
    random.shuffle(name_list)
    
    if i==k-1:
        print(f"최종 : {name_list}")
    else:
        print(f'{i} 번째: {name_list}')

