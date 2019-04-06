def main():
    time = [0] * 5
    re = []
    for i in range(5):
        time[i] = int(input())
        if time[i] % 10 != 0:
            re.append(time[i] % 10)

    ans = sum(time)
    if len(re) > 1:
        re.sort()
        for r in re[1:]:
            ans += 10 - r % 10

    print(ans)


if __name__ == '__main__':
    main()