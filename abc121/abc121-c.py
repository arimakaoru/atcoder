# TLE

N, M = map(int, input().split())
A = [0] * N
B = [0] * N
for i in range(N):
    A[i], B[i] = map(int, input().split())

cnt = 0
ans = 0
while cnt < M:
    min_cost = min(A)
    min_index = A.index(min_cost)
    amount = B[min_index]
    if cnt + amount < M:
        ans += min_cost * amount
        cnt += amount
    elif cnt + amount == M:
        ans += min_cost * amount
        break
    else:
        ans += min_cost * (M - cnt)
        break
    A = [A[i] for i in range(len(A)) if i != min_index]
    B = [B[i] for i in range(len(B)) if i != min_index]
    
print(ans)