def main():
    N = int(input())
    s = list(input())

    if(s.count('R') > N / 2):
        print('Yes')
    else:
        print('No')


if __name__ == '__main__':
    main()