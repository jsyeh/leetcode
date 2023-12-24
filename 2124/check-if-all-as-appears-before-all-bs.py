# 檢查字串裡 'a' 都在 'b' 的前面
# 所以「最右邊的'a'」在左，「最左邊的'b'」在右
class Solution:
    def checkString(self, s: str) -> bool:
        posA, posB = -1, -1
        for i,c in enumerate(s):
            if c=='a': posA = i # 持續更新a座標，便會到最右邊
            if c=='b' and posB==-1: posB = i # 第1個b的座標
        # 糟，上面作法有個漏洞，是 -1 時，另外處理
        # case 211/216: "a"
        if posA==-1 or posB==-1: return True 
        # 只要有任一個沒出現，一定成立

        if posA < posB: return True
        else: return False
