# 本來不知道怎麼解，看了 Editorial 方法1寫Set就會了
class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        codes = set()
        for i in range(len(s)-k+1): # -k 配 +k 剛剛好，但要再+1因不碰邊界
            codes.add(s[i:i+k]) # 字串裡，所有「長為k」的字串加入set
        # print(codes)
        # print(len(codes))
        if len(codes)==2**k: return True # 全部排列組合有 2^k，全有就成功
        else: return False
# case: 186/201: "00110" k=2
