# LeetCode 3443. Maximum Manhattan Distance After K Changes
# N S E W 對應「北、南、東、西」四個方向，可改變字串 s 裡字母 k 次，最遠可到多遠？
# 可在模擬過程看「最遠的距離」在哪。k次「改變的機會」可集中在東北、東南、西南、西北
# 也就是「把另一個方向」的k個，都「改投票」到這些方向
class Solution:
    def maxDistance(self, s: str, k: int) -> int:
        ans = 0
        cnt = Counter()  # 將在過程中，統計目前字母為止出現頻率
        for c in s:  # 照著字母，逐步移動
            cnt[c] += 1
            n, e, w, s = cnt['N'], cnt['E'], cnt['W'], cnt['S']
            ne, ws = n+e, w+s
            nw, es = n+w, e+s
            # ne東北方向，是最大嗎？
            change = min(ws, k)  # ws 有幾個「能換成」ne 方向？
            ans = max(ans, ne-ws+change*2)  # change 來回差2倍
            # ws西南方向，是最大嗎？
            change = min(ne, k)
            ans = max(ans, ws-ne+change*2)
            # nw西北方向，是最大嗎？
            change = min(es, k)
            ans = max(ans, nw-es+change*2)
            # es東南方向，是最大嗎？
            change = min(nw, k)
            ans = max(ans, es-nw+change*2)
        return ans
