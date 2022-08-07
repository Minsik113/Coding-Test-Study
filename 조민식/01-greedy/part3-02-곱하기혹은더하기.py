'''
날짜:2022.08.08
시간복잡도: O(N)

문제: 들어오는 string에 'X' 혹은 '+'를 넣어 가장 큰 수 만들자.
    연산은 왼쪽부터 실행
풀이: 피연산자가 1이하인지 확인해서 1이하면 더한다. 그외는 곱함
'''

s = input()
ans = int(s[0])

for i in s[1:]:
    k = int(i)
    if k <= 1 or ans <= 1:
        ans += k
    else:
        ans *= k
print(ans)