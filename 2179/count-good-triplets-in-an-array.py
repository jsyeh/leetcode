# LeetCode 2179. Count Good Triplets in an Array
# nums1 nums2 裡都有 1...n-1 這些數，只是重新排列過
# 挑 x, y, z 三數，希望剛好兩陣列「對應的 index」都漸增，有幾種挑法？
# 因數字很多 10^5，不能用太多迴圈。Hint 先挑好 y 可用 binary search 找左邊x幾種、右邊z幾種
class Solution:
    def goodTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        index2 = {num: i for i, num in enumerate(nums2)}  # nums2 的 index 對照表
        ans1, ans2 = [], []  # 分別放「左邊有幾種可能」、「右邊有幾種可能」等待「逐一相乘」
        front = []# 依序放 nums2 對應的 index（且隨時保持排序，方便二分搜尋）
        for num in nums1:  # nums1 左到右，依序處理
            i2 = index2[num]  # nums1 的這個數，對應 nums2[i2]
            idx = bisect_left(front, i2)  # 二分搜尋，找到 i2 要放在 front 的哪裡
            front.insert(idx, i2)  # (1) 將 i2 插入 front[idx]，讓 front 保持「排序
            ans1.append(idx)  # (2) idx 位置決定「左邊有幾種可能」，因左邊 index 都「更小」

        back = []  # 倒著放 nums2 對應的 index（且隨時保持排序，方便二分搜尋）
        for num in nums1[::-1]:  # nums1「右到左」依序處理
            i2 = index2[num]  # nums1 的這個數，對應 nums2[i2]
            idx = bisect_left(back, i2)  # 二分搜尋
            back.insert(idx, i2)  # (1) 將 i2 插入 back[idx]，讓 back 保持「排序」
            ans2.append(len(back) - 1 - idx)  # idx 位置決定「右邊」有幾種可能
        ans2 = ans2[::-1]  # 因迴圈倒著處理，所以要到反過來
        # print('ans1', ans1)  # 印出來觀察「不同位置的y」對應的x有幾種
        # print('ans2', ans2)  # 印出來觀察「不同位置的y」對應的z有幾種
        return sum(a*b for a, b in zip(ans1, ans2))  # 針對中間y的座標，將 ans1[i] * ans2[i]
