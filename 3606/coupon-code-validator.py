# LeetCode 3606. Coupon Code Validator
# code[i] 優惠碼 對應 businessLine[i] 產品線 及 isActive[i] 是否還有效
# 去除不對
class Solution:
    def validateCoupons(self, code: List[str], businessLine: List[str], isActive: List[bool]) -> List[str]:
        def checkCharGood(code):  # 確認「每個字母」都正確
            for c in code:  # 逐一檢查字母
                if not (c.isalnum() or c=='_'):  # 不是合法字母
                    return False  # 就失敗
            return True  # 檢查成功
        table = {"electronics":0, "grocery":1, "pharmacy":2, "restaurant":3}
        ans = []  # 放：正確的code[i]、對應的businessLine[i]
        for i in range(len(code)):  # 逐一檢查，把「無效、錯誤」的優惠碼「避開」
            if not isActive[i]: continue  # 避開「用過的」
            if code[i]=="": continue  # 避開「空字串」
            if not checkCharGood(code[i]): continue  # 避開「非」字母、數字底線
            if businessLine[i] not in table: continue  # 避開「錯誤」的產品線
            # Case 766/779 竟有重覆code[i],故 code[i] 要與 businessLine[i] 一起記錄
            ans.append( (code[i],businessLine[i]) )  # 記下答案（對應的優惠碼、產品線）
        ans.sort(key=lambda x:(table[x[1]],x[0]) )  # 先照「產品線」排，再照字母排
        return [x[0] for x in ans]  # 只要回傳「正確順序」的 code[i]
