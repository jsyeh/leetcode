# 模擬題，照著做就好了
class Solution:
    def executeInstructions(self, n: int, startPos: List[int], s: str) -> List[int]:
        # 4個移動的方向, 對應移動 ii,jj 的方向
        move = {'L':(0,-1), 'R':(0,+1), 'U':(-1,0), 'D':(+1,0)}
        ans = []
        for i in range(len(s)): # 依字串長度，從i-th開始走
            ii, jj = startPos
            step = 0 # 從第0步開始走
            for c in s[i:]: # 照著字母開始位置來模擬
                ii += move[c][0]
                jj += move[c][1] # 照著方向走
                if ii<0 or jj<0 or ii>=n or jj>=n:
                    break # 離開這次的迴圈
                step += 1 # 順移多走1步
            ans.append(step) # 最後能走幾步
        return ans
