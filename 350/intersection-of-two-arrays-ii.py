# LeetCode 350. Intersection of Two Arrays II
# 兩個array裡，有哪些相同的部分？ 其實使用 Counter()就可解
# 也可以使用 sort()後，再逐一比對。
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        counter1 = Counter(nums1)  # 用counter統計各數字出現次數
        counter2 = Counter(nums2)
        ans = []
        for c in counter1:  # 以 counter1 為主
            if c in counter2:  # 如果剛好也出現在 counter2
                ans += [c]*min(counter1[c],counter2[c]) # 照「較少」數量，重覆加入list裡
        return ans
