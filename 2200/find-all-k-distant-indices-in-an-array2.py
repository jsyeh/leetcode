# LeetCode 2200. Find All K-Distant Indices in an Array
# 找到 nums[i] == key 的位置，將 i 左右距離 k 之間的 index 都收集好，照小到大排好
class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        N = len(nums)
        table = [0] * (N+1)  # 增減對照表
        for i in range(N):
            if nums[i]==key:  # 找到 key，就增減 「開始...結束」
                table[max(0, i-k)] += 1  # 開始位置「增」
                table[min(N, i+k+1)] -= 1  # 結束位置右方「減」
        ans = []
        prefix = 0  # 會累積 prefix 的增減量
        for i in range(N):
            prefix += table[i]
            if prefix>0: ans.append(i)  # 增減量是正的：在範圍內
        return ans
