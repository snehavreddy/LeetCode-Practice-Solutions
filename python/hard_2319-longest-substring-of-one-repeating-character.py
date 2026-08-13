class SegmentTreeNode:
    def __init__(self, char: str):
        self.lc = char       # Leftmost character
        self.rc = char       # Rightmost character
        self.prefix = 1      # Length of longest repeating prefix
        self.suffix = 1      # Length of longest repeating suffix
        self.mx = 1          # Longest repeating substring in segment

class SegmentTree:
    def __init__(self, s: str):
        self.n = len(s)
        self.tree = [None] * (4 * self.n)
        self._build(s, 0, 0, self.n - 1)

    def _merge(self, left: SegmentTreeNode, right: SegmentTreeNode, left_len: int, right_len: int) -> SegmentTreeNode:
        res = SegmentTreeNode(left.lc)
        res.lc = left.lc
        res.rc = right.rc

        # Calculate Prefix
        if left.prefix == left_len and left.lc == right.lc:
            res.prefix = left.prefix + right.prefix
        else:
            res.prefix = left.prefix

        # Calculate Suffix
        if right.suffix == right_len and right.rc == left.rc:
            res.suffix = right.suffix + left.suffix
        else:
            res.suffix = right.suffix

        # Calculate Max
        cross = left.suffix + right.prefix if left.rc == right.lc else 0
        res.mx = max(left.mx, right.mx, cross)

        return res

    def _build(self, s: str, node: int, l: int, r: int):
        if l == r:
            self.tree[node] = SegmentTreeNode(s[l])
            return

        mid = (l + r) // 2
        left_node, right_node = 2 * node + 1, 2 * node + 2
        self._build(s, left_node, l, mid)
        self._build(s, right_node, mid + 1, r)

        left_len = mid - l + 1
        right_len = r - mid
        self.tree[node] = self._merge(self.tree[left_node], self.tree[right_node], left_len, right_len)

    def update(self, node: int, l: int, r: int, idx: int, char: str):
        if l == r:
            self.tree[node] = SegmentTreeNode(char)
            return

        mid = (l + r) // 2
        left_node, right_node = 2 * node + 1, 2 * node + 2
        if idx <= mid:
            self.update(left_node, l, mid, idx, char)
        else:
            self.update(right_node, mid + 1, r, idx, char)

        left_len = mid - l + 1
        right_len = r - mid
        self.tree[node] = self._merge(self.tree[left_node], self.tree[right_node], left_len, right_len)

    def query_max(self) -> int:
        return self.tree[0].mx


class Solution:
    def longestRepeating(self, s: str, queryCharacters: str, queryIndices: list[int]) -> list[int]:
        st = SegmentTree(s)
        ans = []
        n = len(s)

        for char, idx in zip(queryCharacters, queryIndices):
            st.update(0, 0, n - 1, idx, char)
            ans.append(st.query_max())

        return ans