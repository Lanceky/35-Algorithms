class FenwickTree:
    def __init__(self, size):
        self.n = size
        self.tree = [0] * (self.n + 1)  # 1-based indexing

    def update(self, i, delta):
        while i <= self.n:
            self.tree[i] += delta
            i += (i & -i)  # Move to next covering index

    def query(self, i):
        res = 0
        while i > 0:
            res += self.tree[i]
            i -= (i & -i)  # Move to parent index
        return res

    def range_query(self, l, r):
        return self.query(r) - self.query(l - 1)