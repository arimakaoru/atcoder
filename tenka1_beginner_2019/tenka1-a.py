def main():
    A, B, C = map(int, input().split())

    if A <= C <= B or B <= C <= A:
        print('Yes')
    else:
        print('No')


if __name__ == '__main__':
    main()
