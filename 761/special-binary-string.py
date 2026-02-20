# LeetCode 761. Special Binary String
# 特殊字串：0和1一樣多、左邊每種prefix都是1比較多
# ex. 11011000 每次將相鄰2個「特殊字串」交換，找能做出的最大字串
#      ^^!!!! 把「10」和「1100」交換後，能做到最大
class Solution:
    def makeLargestSpecial(self, s: str) -> str:
        # Hint 介紹「往上、往下」的高低線，像山的線「回到起點高度」對應特殊字串
        def helper(s):  # 吃到一段「特殊字串」1開頭、0結尾
            ans = []  # 再裁切成許多「小段」的「特殊字串」
            start, H = 0, 0  # 這段字串的開始高度，之後會往上、往下
            for i in range(len(s)):  # 逐一處理字母
                if s[i]=='1': H += 1  # 往上
                if s[i]=='0': H -= 1  # 往下
                if H==0:  # 「回到起點高度」切出一段「特殊字串」再「函式呼叫函式」
                    ans.append( '1' + helper(s[start+1:i]) + '0')
                    start = i + 1   # helper() 裡「升1格」測試，字串越來越短
            # 若可「相鄰交換」就能完成泡泡排序，完成排序任務
            ans.sort(reverse=True)  # 從大到小排好
            return ''.join(ans)  # 再接回原本長度的字串
        return helper(s)  # 函式呼叫函式
