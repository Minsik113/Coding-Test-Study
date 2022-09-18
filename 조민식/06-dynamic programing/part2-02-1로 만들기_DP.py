'''
날짜: 2022. 09. 18
시간복잡도:

문제:
풀이:

Ai = min(A(i-1)), A(i/2), A(i/3), A(i/5)) + 1


테스트값
1234567
= 17
-> 0.75000 sec

'''
x = int(input())
d = [0] * 1234568 # 숫자가 3만까지니까
import time
start = time.time()

for i in range(2, x+1):
    # 현재 수에서 1빼는 경우
    d[i] = d[i-1] + 1

    # 나눌수있는지봄.
    if i % 2 == 0:
        d[i] = min(d[i], d[i//2] + 1)
    if i % 3 == 0:
        d[i] = min(d[i], d[i//3] + 1)
    if i % 5 == 0:
        d[i] = min(d[i], d[i//5] + 1)

print(d[x])

end = time.time()
print(f"{end - start:.5f} sec")
