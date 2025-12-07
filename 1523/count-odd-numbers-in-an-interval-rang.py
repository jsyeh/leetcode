# LeetCode 1523. Count Odd Numbers in an Interval Range
# 請問 low ... high 這個範圍裡，有幾個「奇數」？
# 這題不能用for迴圈慢慢算，因為數字會很大。直接數字相減就好了。
class Solution:
    def countOdds(self, low: int, high: int) -> int:
        # 奇-奇：1 3 5 7 9 = (9-1)//2 + 1
        # 偶-奇：0 1 3 5 7 = (7-0)//2 + 1
        # 奇-偶：1 3 5 6 = (6-1)//2 + 1
        # 偶-偶：0 1 3 5 6 = (6-0)//2 不用再加一
        if low%2==0 and high%2==0:
            return (high-low)//2
        else:
            return (high-low)//2 + 1
