# TLE > AC
# 累積和を使う
# 出力は随時でもOK

N, Q = map(int, input().split())
S = input()

t = [0] * N
t[0] = 0
for i in range(1,N):
    if S[i-1] == 'A' and S[i] == 'C':
        t[i] = t[i-1] + 1
    else:
        t[i] = t[i-1]

for _ in range(Q):
    l, r = map(int, input().split())
    print(t[r-1] - t[l-1])

