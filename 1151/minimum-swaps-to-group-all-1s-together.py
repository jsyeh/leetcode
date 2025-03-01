# LeetCode 1151. Minimum Swaps to Group All 1's Together
# 要把 data 裡的 1 交換到「放到一起」，要「交換」幾次？
class Solution:
    def minSwaps(self, data: List[int]) -> int:
        counter = Counter(data)
        ones = counter[1]  # 總共有幾個 1，對應「最後有幾個1」需要湊在一起
        zeros = 0
        for i in range(ones):  # 先讀入前幾個數，看裡面有0「需要swap幾個外面的1進來」
            if data[i]==0: zeros += 1
        ans = zeros  # 一開始的答案「有幾個0」對應「需要swap幾次」
        for i in range(ones, len(data)):  # 利用「毛毛蟲」技巧，了解「裡面有幾個0」
            if data[i]==0: zeros += 1  # 右邊「吃到」zero
            if data[i-ones]==0: zeros -= 1  # 左邊「吐出」zero
            ans = min(ans, zeros)  # 「有幾個0」對應「需要swap幾次」，越少越好
        return ans
