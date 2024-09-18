# LeetCode 179. Largest Number
# 一堆數字，組出「最大」的數。我本來以為「先大到小sort」就好，
# 但有很多例外狀況，最後用「兩字串接起來」的前後關係，完成這題的sort()
class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        def sort_rule(x, y):  # 用來比大小的函式，回傳+1,-1,0
            if x+y > y+x: return 1
            if x+y < y+x: return -1
            return 0 # 這個 compare 函式，再交給 cmp_to_key() 變成 sort key

        s = [str(num) for num in nums] # 把一堆數字，變一堆字串
        s.sort(reverse=True, key=cmp_to_key(sort_rule))  # 由大到小排好
        if s[0][0]=='0': return '0'. # 字串「最大的」竟然是0的話，接起來就只能是'0'了
        return ''.join(s)  # 再接成「長字串」當答案
