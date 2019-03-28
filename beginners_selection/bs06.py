def get_sum_of_digits(num):
    sum_of_digits = 0

    while(num > 0):
        sum_of_digits += num % 10
        num = num // 10
    
    return sum_of_digits


def main():
    N, A, B = map(int, input().split())
    ans = 0

    for i in range(1, N+1):
        if A <= get_sum_of_digits(i) <= B:
            ans += i

    print(ans)


if __name__ == '__main__':
    main()