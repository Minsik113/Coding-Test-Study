'''
😍KMP알고리즘 ---- 출처: https://bowbowbow.tistory.com/6 [멍멍멍:티스토리]
X = 'anhjcwabnchjbslamcwancnsacbakbacbabcabavabacba'
'abc'라는 문자열이 X안에 있는지 파악하려면, 어떻게 해야할까??

1. 한칸씩 이동하면서 본다. -> O(NM)
찾고자하는 문자열 * 전체 문자열길이

2. KMP 알고리즘 -> O(N+M) !!!
어케함?
2-1. 접두사, 접미사 개념을 알아야함.
    2-1-1.banana의 접두사
        -> b, ba, ban, bana, banan, banana
    2-1-2.banana의 접미사
        -> a, na, ana, nana, anana, banana
2-2. pi배열 알아야함
    2-2-1.pi[i]는 주어진 문자열의 0~i 까지의 부분 문자열 중에서 
        prefix == suffix가 될 수 있는 부분 문자열 중에서 가장 긴 것의 길이
        (단, prefix가 0~i 까지의 부분 문자열과 같으면 안된다.)

-----
즉, 실패함수는 KMP알고리즘 실행중, 일치하지 않는 문자가 있을 때
어디서부터 검색을 해야할지(몇칸을 뛰어넘어야 하는지) 알려주는 지표같은 존재이다.

패턴의 처음부분부터 해당위치까지 즉 접두사와 접미사가 몇개나 일치하는지 기록하는
부분 일치 테이블(partial match table or fail function)을 만드는 것이라고 보면된다.
-----

'''
