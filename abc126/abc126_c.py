# WA

def main():
    N, K = map(int, input().split())

    sum = 1
    cnt = 0
    while sum < K:
        sum *= 2
        cnt += 1
    
    ans = 0
    for i in range(N):
        if cnt > 0:
            ans += (1 / N) * (0.5 ** cnt)
            cnt -= 1
        else:
            ans += (1 / N)

    print(ans)


if __name__ == '__main__':
    main()