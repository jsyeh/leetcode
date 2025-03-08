# LeetCode 2379. Minimum Recolors to Get K Consecutive Black Blocks
# 想要有連續 k 個黑色W，問「需要改幾個」，用毛毛蟲就可以解了
class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        counter = Counter(blocks[:k])  # 先統計「前k格」
        ans = counter['W']  # 有「幾個白色」需要被改變
        # 接下來使用「毛毛蟲」的走法
        for i in range(len(blocks)-k):
            counter[blocks[k+i]] += 1  # 右邊吃進1個字母
            counter[blocks[i]] -= 1  # 左邊吐出1個字母
            ans = min(ans, counter['W'])  # 更新「最小」值
        return ans
