class DSU:
    def __init__(self, size):
        self.parent = list(range(size))
        self.rank = [0] * size

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])  # Path compression
        return self.parent[x]

    def union(self, x, y):
        x_root = self.find(x)
        y_root = self.find(y)
        if x_root == y_root:
            return

        # Union by rank
        if self.rank[x_root] < self.rank[y_root]:
            self.parent[x_root] = y_root
        else:
            self.parent[y_root] = x_root
            if self.rank[x_root] == self.rank[y_root]:
                self.rank[x_root] += 1


def findCircleNum(matrix):
    n = len(matrix)
    dsu = DSU(n)

    for i in range(n):
        for j in range(i + 1, n):
            if matrix[i][j] == 1:
                dsu.union(i, j)

    # Count unique roots
    return len({dsu.find(i) for i in range(n)})


# Test
matrix = [
    [1, 1, 0],
    [1, 1, 0],
    [0, 0, 1]
]
print(findCircleNum(matrix))  # Output: 2