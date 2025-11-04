# LeetCode 3318. Find X-Sum of All K-Long Subarrays I
# nums 陣列裡，依序找每個「長度i為k的subarray」統計裡面「各數出現次數」，
# 把每個 subarray「前x名的數」加權後加起來，放到 ans 陣列裡
class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        ans = []
        counter = Counter(nums[:k])  # 先把最前面、長度k的subarray數「次數」
        # 重新組合，把「次數」放左邊、優先排序，相同時再把「key」放右邊排序，從大到小排序
        top = sorted([(counter[c],c) for c in counter], reverse=True)
        # 要將「前x名的數」加權後加起來
        ans.append(0)  # 先在「最後項」放 0，再逐項加到「最後項」
        for freq,num in top[:x]:  # 找到 top 前x項，不夠的話也沒關係
            ans[-1] += freq*num

        for i in range(k, len(nums)):
            counter[nums[i]] += 1  # 右邊加入「新的項」
            counter[nums[i-k]] -= 1  # 左邊扣掉「舊的項」
            # 重新組合，把「次數」放左邊、優先排序，相同時再把「key」放右邊排序，從大到小排序
            top = sorted([(counter[c],c) for c in counter], reverse=True)
            # 要將「前x名的數」加權後加起來
            ans.append(0)  # 先在「最後項」放 0，再逐項加到「最後項」
            for freq,num in top[:x]:  # 找到 top 前x項，不夠的話也沒關係
                ans[-1] += freq*num
        return ans
