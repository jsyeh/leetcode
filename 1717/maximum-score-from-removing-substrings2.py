# LeetCode 1717. Maximum Score From Removing Substrings
# 字串裡，有一堆a和一堆b混在一起(也有其他字母)。如果消掉'ab'可得x分；消掉'ba'可得y分
# 最多可得到幾分？這裡有個作法，是「先處理分數高」的部分，邊巡邊刪、邊更新分數
# 處理完後，再處理另一個分數的部分，就完成了。
class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        def remove(s, ab, x): # 在字串s裡，找 ab 對應的字串，每找到1組，就+x分
            ans = 0
            k = 0 # k 與 i 搭配。k對應目前有效的前k個字母
            for i in range(len(s)): # 逐字處理
                s[k] = s[i] # 把 s[i] 搬到 s[k] 處理
                if k>0 and ab[0]==s[k-1] and ab[1]==s[k]: # 相鄰2字母，符合ab
                    ans += x  # 兌換，增加x分
                    k -= 1 # 消掉ab,k往左扣1格，將再放「下一輪」的資料
                else: k += 1 # 沒有消掉，k往右1格。k對應現在殘留的字串長度
            del s[k:] # 整個迴圈走完後，要把 s 字串裡，後面移走的部分「裁掉」
            return ans
        s = list(s) # 因為字串無法靈活修改，所以轉換成list
        if x>y: # 先處理比較高分的 'ab'
            return remove(s, 'ab', x) + remove(s, 'ba', y)
        else: # 先處理比較高分的 'ba'
            return remove(s, 'ba', y) + remove(s, 'ab', x)
