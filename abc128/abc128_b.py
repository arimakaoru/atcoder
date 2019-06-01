from operator import itemgetter


def sort_shop(N, shop):
    for i in range(N-1):
        for j in range(N):
            if shop[i][1] > shop[j][1]:
                shop[i], shop[j] = shop[j], shop[i]
            elif shop[i][1] == shop[j][1] and shop[i][2] < shop[j][2]:
                shop[i], shop[j] = shop[j], shop[i]

    return shop


def main():
    N = int(input())
    shop = [[0,0,0] for i in range(N)]

    i = 1
    for s in shop:
        s[0] = i
        s[1], s[2] = input().split()
        int(s[2])
        i += 1

    shop = sort_shop(N, shop)

    for s in shop:
        print(s[0])


if __name__ == '__main__':
    main()