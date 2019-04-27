def make_divisors(n):
    divisors = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n//i)

    return divisors


def main():
    N = int(input())
    A = list(map(int, input().split()))
    all_divisors = []

    for a in A:
        all_divisors.extend(make_divisors(a))
    
    all_divisors.sort(reverse=True)

    for d in all_divisors:
        if all_divisors.count(d) >= N - 1:
            print(d)
            return

    print(1)


if __name__ == '__main__':
    main()