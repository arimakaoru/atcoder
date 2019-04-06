import math

def main():
    N = int(input())
    time = [0] * 5
    for i in range(5):
        time[i] = int(input())

    min_time = min(time)
    ans = 5 + math.ceil((N - min_time) / min_time)

    print(ans)


if __name__ == '__main__':
    main()