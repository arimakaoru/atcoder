# AC

N, M, C = map(int, input().split())
B = list(map(int, input().split()))
A = []
for i in range(N):
    A.append(list(map(int, input().split())))

cnt = 0
for i in range(N):
    ans = 0
    for j in range(M):
        ans += A[i][j] * B[j]
    ans += C
    
    if ans > 0:
        cnt += 1

print(cnt)
