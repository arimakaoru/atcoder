def main():
    N, K = map(int, input().split())
    S = input()

    if S[K-1] == 'A':
        char = 'a'
    elif S[K-1] == 'B':
        char = 'b'
    elif S[K-1] == 'C':
        char = 'c'

    print(S[:K-1] + char + S[K:N])


if __name__ == '__main__':
    main()