def main():
    N = int(input())
    a = list(map(int, input().split()))

    a.sort(reverse=True)

    sum_alice = sum(a[::2])
    sum_bob = sum(a[1::2])

    print(sum_alice - sum_bob)


if __name__ == '__main__':
    main()