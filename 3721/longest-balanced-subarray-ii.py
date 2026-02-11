# LeetCode 3721. Longest Balanced Subarray II
# 找到最長的陣列，裡面「奇數有幾種==偶數有幾種」
# 感覺很難，需要我還不會的技巧，加上體力不支，只好直接貼上 C_PRATEEK 的答案
class SegmentTree:
    def __init__(self, n: int):
        self.n = n
        self.min_tree = [0] * (4 * n)
        self.max_tree = [0] * (4 * n)
        self.lazy = [0] * (4 * n)

    def push(self, node: int, start: int, end: int):
        if self.lazy[node] != 0:
            self.min_tree[node] += self.lazy[node]
            self.max_tree[node] += self.lazy[node]
            if start != end:
                self.lazy[2 * node] += self.lazy[node]
                self.lazy[2 * node + 1] += self.lazy[node]
            self.lazy[node] = 0

    def update_range(self, node: int, start: int, end: int, l: int, r: int, val: int):
        self.push(node, start, end)
        if start > end or start > r or end < l:
            return 

        if l <= start and end <= r:
            self.lazy[node] += val
            self.push(node, start, end)
            return

        mid = (start + end) // 2
        self.update_range(2 * node, start, mid, l, r, val)
        self.update_range(2 * node + 1, mid + 1, end, l, r, val)
        self.min_tree[node] = min(self.min_tree[2 * node], self.min_tree[2 * node + 1])
        self.max_tree[node] = max(self.max_tree[2 * node], self.max_tree[2 * node + 1])

    def find_leftmost_zero(self, node: int, start: int, end: int):
        self.push(node, start, end)
        if self.min_tree[node] > 0 or self.max_tree[node] < 0:
            return -1

        if start == end:
            return start if self.min_tree[node] == 0 else -1
        mid = (start + end) // 2
        left = self.find_leftmost_zero(2 * node, start, mid)
        if left != -1:
            return left
        return self.find_leftmost_zero(2 * node + 1, mid + 1, end)

class Solution:
    def longestBalanced(self, nums: List[int]) -> int:
        n = len(nums)
        prev = defaultdict(lambda: -1)

        st = SegmentTree(n)
        res = 0

        for r in range(n):
            v = nums[r]
            val = 1 if v % 2 == 0 else -1
            
            if prev[v] != -1:
                st.update_range(1, 0, n - 1, 0, prev[v], -val)

            st.update_range(1, 0, n- 1, 0, r, val)

            prev[v] = r
            l = st.find_leftmost_zero(1, 0, n - 1)

            if l != -1 and l <= r:
                res = max(res, r - l + 1)
        return res      
