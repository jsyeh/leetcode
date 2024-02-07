# 字串裡，把ab去掉，得x分。把ba去掉，得y分。
# 最「最多」可得幾分。
# Discussion 裡，Switch2on 說，他覺得這題是 Hard
# 直覺：難道是「先把高分的」全部處理完後，再處理「另一組」？
# Hint 1 證實這個作法。
# Solutions 裡,lzl124631x 就照著這樣的方法來做。
class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        ab, ba = "ab", "ba"
        if x < y:
            ab, ba = ba, ab # 交換一下，讓高分在 ab 及 x
            x, y = y, x
        s = list(s) # 轉成 list 以便修改
        def remove(s, ab, x) -> int:
            ans = 0
            k = 0 # s[k] = s[i] 將字母「往左」移
            for i in range(len(s)):
                s[k] = s[i] # 字母左移（如果k比較小）
                if k>0 and ab[0]==s[k-1] and ab[1]==s[k]:
                    k -= 1 # 消掉 ab，左移1格
                    ans += x # 得分
                else: k += 1 # 沒辦法消，右移1格
            del s[k:] # 刪掉「移走」的部分
            return ans
        #print(s) # 逐筆測試 Debug
        #ans1 = remove(s, ab, x) # 逐筆測試 Debug
        #print(s) # 逐筆測試 Debug
        #ans2 = remove(s, ba, y) # 逐筆測試 Debug
        #print(s) # 逐筆測試 Debug
        #return ans1 + ans2 # 逐筆測試 Debug
        return remove(s, ab, x) + remove(s, ba, y)
