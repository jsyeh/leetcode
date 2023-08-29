class Solution:

    def __init__(self, w: List[int]):
        self.sum = 0
        for ww in w:
            self.sum += ww # 算出加總的結果

        self.w = [0]*(len(w)+1) # 這個 self.w 是 running sum, 也就是另類的 PDF
        for i in range(len(w)+1):
            if i==0: self.w[i] = 0 # 
            else: self.w[i] = self.w[i-1] + w[i-1]
        

    def pickIndex(self) -> int:
        # 先 random 找個值，再用 binary search 看它在哪裡
        now = randrange(self.sum) # 由加總的結果，決定 randrange()的範圍
        left, right = 0, len(self.w) # 再用 binary search 看
        print("===sum, now:", self.sum, now)
        while left < right:
            mid = (left+right)//2
            print(left, right, mid, self.w[mid])
            if self.w[mid] <= now: # 
                left = mid + 1
            else:
                right = mid
        print("ans:", left)
        return left-1
# case 5/57: ["Solution","pickIndex","pickIndex","pickIndex","pickIndex","pickIndex","pickIndex","pickIndex","pickIndex"]
# [[[4,2]],[],[],[],[],[],[],[],[]]

# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()
