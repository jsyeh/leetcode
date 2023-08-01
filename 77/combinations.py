class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def helper(start: int, n: int, k: int) -> List[List[int]]:
            ans = []
            if k==0: # 取0個，那答案是空集合
                return ans
            if k==1: # 取1個，那答案是每個都取1個
                for i in range(start, start+n):
                    ans.append( [i] )
                return ans

            # 剩下，請簡單的 helper(開始, 個數, k-1)幫忙，函式呼叫函式
            for i in range(1, n-k+2): # 開始+i, 個數-i
                # 子問題：從 start+i 開始 的答案 (跳開 i 個哦)
                listAll = helper(start+i, n-i, k-1) # start+i...個數
                for temp in listAll:
                    temp.insert(0, start+i-1) # 最前面補上 start+i-1
                    ans.append(temp)
            return ans

        return helper(1, n, k)


