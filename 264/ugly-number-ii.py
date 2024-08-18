# LeetCode 264. Ugly Number II
# 想找出「只有2,3,5」組合出來的數「的第n個」
# 用 Heap 抽出「一群數」裡最小數，再塞入3個數（乘2乘3乘5）
# 重覆的數不要再塞回去。重覆做n次，就能找到答案。
class Solution:
    def nthUglyNumber(self, n: int) -> int:
        heap = [1] # 從1開始，生出全部的數
        visited = set()  # 避免重覆：有出現過，就不重覆塞入
        for i in range(n):  # 要挑出第n個數
            ans = heappop(heap)  # 抽出1個數（目前最小的數）
            # print(ans)  # debug時，觀察用
            for m in [2,3,5]:  # 再塞入3個數
                if ans*m not in visited:  # 避免重覆塞入
                    heappush(heap, ans*m)
                    visited.add(ans*m)
        return ans
