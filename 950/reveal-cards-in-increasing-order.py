# 最多有1000張牌, 一開始全都蓋住。有個翻牌的規則如下
# 1. 把最上面的牌翻開, 拿走
# 2. 再把第2張牌, 移到最後面
# 再繼續以上兩個步驟一直做, 直到牌全部翻走。希望翻出來的牌, 要從小到大跳出來。
# 問: 牌一開始要怎麼放, 才能完成上面的任務, 且翻出的牌是從小到大出來。
# 有點麻煩, 要倒過來想才行。但就倒過來模擬即可
class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        ans = deque() # 模擬牌堆
        deck.sort(reverse=True) # 倒著將牌放回去
        for card in deck: # 倒著將牌放回去
            if len(ans)>0: # 最後的, 放在最前面
                ans.appendleft(ans.pop())
            ans.appendleft(card) # 最後抽出來的版, 在最前面
        return list(ans)
