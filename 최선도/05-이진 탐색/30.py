# 1차 풀이 정확성 25 / 효율성 30 탈락
# def solution(words, queries):
#     answer = []
#     for query in queries:
#         cnt = 0
#         qm = query.count("?")
#         num = query.index("?"*qm)
#         left = num
#         right = (num + qm) - 1
#         for word in words:
#             if len(query) < len(word) or len(query) != len(word):
#                 continue
#             else:
#                 if query[0] == "?":
#                     if (word[right+1:] == query[right+1:]):
#                         cnt += 1     
#                 elif query[-1] == "?":
#                     if word[:left] == query[:left]:
#                         cnt += 1
#                 elif (query[0] == "?") and (query[-1] == "?"):
#                     if len(word) == len(query):
#                         cnt += 1
#         answer.append(cnt)
#     return answer

# bit.ly/3ePzedN 문제 풀이
# bit.ly/3BlXDiz trie 구조

import sys
from pprint import pprint
sys.setrecursionlimit(100001) # 재귀 제한 기본 1000번 -> 100001번

def solution(words, queries):
    answer = []
    rev_words, counted = [], []   # 조건 b, c를 위한 두 변수
    for w in words:
        rev_words.append(w[::-1])
        counted.append(len(w))

    trie = make_trie({}, words)   # 조건 a 의 trie
    rev_trie = make_trie({}, rev_words)   # 조건 b 의 rev_trie 

    for query in queries:  # 3가지 조건으로 나누어서,
        if query[0] == '?' and query[-1] == '?': # 양 끝이 모두 ? 일 때
            answer.append(counted.count(len(query))) # 쿼리의 길이가 같은 단어를 한번에 추가
        elif query[0] == '?': # 시작이 ?로 시작하면 
            answer.append(search_trie(rev_trie, query[::-1], len(query)))
        elif query[-1] == '?': # 끝이 ?로 시작하면 
            answer.append(search_trie(trie, query, len(query)))

    return answer


def make_trie(trie, words):
    for word in words:
        node = trie
        length = len(word)
        for w in word:
            if w in node:
                node = node[w]
                node['!'].append(length)
            else:
                node[w] = {}
                node = node[w]
                node['!'] = [length]
    pprint(trie)
    return trie


def search_trie(trie, query, length):
    count = 0
    if query[0] == '?':
        return trie['!'].count(length)
    elif query[0] in trie:
        count += search_trie(trie[query[0]], query[1:], length)
    return count


words = ["frodo", "front", "frost", "frozen", "frame", "kakao"]
queries = ["fro??", "????o", "fr???", "fro???", "pro?"]

print(solution(words, queries))