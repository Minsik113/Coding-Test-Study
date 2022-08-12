# 3. 문자열 뒤집기

s = input()
zero, one = 0,0

if(s[0]=='0'):
    zero+=1
else:
    one +=1

for i in range(1,len(s)):
    if (s[i] != s[i-1]):
        if(s[i]==0):
            zero+=1
        else:
            one+=1

print(min(zero, one))
