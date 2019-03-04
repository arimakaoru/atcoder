# 解説見たけどわからぬWA

class UnionField:

    def __init__(self, bridge_num):
        self.parent = [-1] * bridge_num

    def root(self, island):
        if self.parent[island] < 0:
            return island
        self.parent[island] = self.root(self.parent[island])
        return self.parent[island]

    def size(self, island):
        return -self.parent[self.root(island)]

    def connect(self, island_a, island_b):
        island_a = self.root(island_a)
        island_b = self.root(island_b)
        if island_a == island_b:
            return False

        if self.size(island_a) < self.size(island_b):
            island_a, island_b = island_b, island_a

        self.parent[island_a] += self.parent[island_b]
        self.parent[island_b] = island_a

        return True


island_num, bridge_num = map(int, input().split())
island_a = [0] * bridge_num
island_b = [0] * bridge_num
for i in range(bridge_num):
    island_a[i], island_b[i] = map(int, input().split())
    island_a[i] -= 1
    island_b[i] -= 1

ans = [-1] * bridge_num
ans[bridge_num - 1] = int(island_num * (island_num - 1) / 2)

Uni = UnionField(island_num)

for i in range(bridge_num - 1, 0, -1):
    ans[i - 1] = ans[i]
    
    if Uni.root(island_a[i] != Uni.root(island_b[i])):
        ans[i - 1] -= Uni.size(island_a[i]) * Uni.size(island_b[i])
        Uni.connect(island_a[i], island_b[i])

for i in ans:
    print(int(i))
