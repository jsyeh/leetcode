class Solution:
    def digitSum(self, s: str, k: int) -> str:
        # 照著題目的演算法
        while len(s)>k: # 只要還能以 k 的長度來切 s，就繼續做
            s2 = "" # 用來存這輪答案的字串，將會變成新的s
            for i in range(0,len(s), k): # 以 k 為長度來切字串
                now = 0
                for j in range(k): # 每段裡的逐個字母
                    if i+j<len(s): # 只要沒超過原本s字串的長度，就做加法
                        now += int(s[i+j])
                s2 += str(now) # 算出這段的結果後，轉成字串存起來
            s = s2 # 將結果變成新的s
        return s
