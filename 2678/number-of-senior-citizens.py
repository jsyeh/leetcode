# LeetCode 2678. Number of Senior Citizens
# details[i] 字串裡有 電話、性別、年齡、座位 資訊，問有幾位年齡>60
class Solution:
    def countSeniors(self, details: List[str]) -> int:
        ans = 0
        for s in details:
            # 年齡欄位，是第11及第12個字母：字母連起來，再轉整數即可
            if int(s[11]+s[12]) > 60: ans += 1
        return ans

