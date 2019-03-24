# TLE
N, Q = map(int, input().split())
S = input()
ans = []
for _ in range(Q):
    l, r = map(int, input().split())
    ans.append(S[l-1:r].count('AC'))

for i in ans:
    print(i)