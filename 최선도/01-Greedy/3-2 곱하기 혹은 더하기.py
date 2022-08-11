from time import time

S = input()
start_time = time()

answer = int(S[0])

for i in range(len(S)-1):
    if int(S[i]) in [0, 1]:
        answer += int(S[i+1])
    else :
        answer *= int(S[i+1])

print(answer)
print(f'{time() - start_time:.2f}')

# input : 02984 --> output : 576     time = 0
# input : 567 --> output : 210    time = 0