# LeetCode 2191. Sort the Jumbled Numbers 數字弄混後，再排序
# nums[i] 排序的方法，是照 mapping 對照表弄混後，再排序
class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        def mapped(n):
            return int(''.join([str(mapping[int(c)]) for c in str(n)]))
        return sorted(nums, key=lambda x: mapped(x))  # 使用昨天的 key=lambda 來排序

        # 下面只是解釋用。第5行的函式 mapped() 的倒裝句，等價於以下程式
        def mapped2(n): # 用 mapped2() 來解釋第5行 mapped() 做的事
            ans = []  # 用來接收 mapping 的結果
            for c in str(n):  # 將 n 轉成字串後，針對每個字母c
                ans.append(mapping[int(c)])  # c先轉成整數,再查表mapping[] 再收答案
            return int( ''.join(ans) )  # 把答案變成字串後，再轉成int整數
    
