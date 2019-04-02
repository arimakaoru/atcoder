def main():
    N = int(input())
    d = [0] * N
    for i in range(N):
        d[i] = int(input())
    
    d.sort()
    print(len(set(d)))


if __name__ == '__main__':
    main()