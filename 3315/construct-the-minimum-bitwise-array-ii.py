# LeetCode 3315. Construct the Minimum Bitwise Array II
# nums 裡有許多質數，找出 ans 陣列，使得 ans[i] OR (ans[i]+1) == nums[i]
# 這次數字很大，所以不能用「暴力法」去試答案，必須觀察出數學的規則。
# 3: 11 =  01 |  10  把右邊一堆1的11，最左邊的1變成0
# 5:101 = 100 | 101  把右邊一堆1的 1，變成0
# 7:111 = 011 | 100  把右邊一堆1的111，最左邊的1變成0
class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        def helper(n):  # 會把 n 二進位右邊一堆1「最左邊的1變成0」
            now = bin(n)  # 先把 n 以二進位字串 ex. 3 變 '0b11'
            i = len(now)-1  # 從最右邊，慢慢往左比
            while now[i]=='1':  i -= 1  # 只要是 '1' 就繼續往左
            #print(now, i, now[:i+1], now[i+2:])  # 印出 Debug，找到最左邊1的左邊
            return int(now[:i+1]+'0'+now[i+2:], 2)  # 把最左邊1變成'0'，再變整數
        ans = []
        for num in nums:
            if num==2:  # 唯一無法解的質數 2
                ans.append(-1)  # 要填入 -1
            else:  # 其他質數，都可找到答案
                ans.append( helper(num) )  # 用 helper() 找到答案
        return ans
