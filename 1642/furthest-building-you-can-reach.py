# 在爬時，可使用「幾塊」 bricks 或「1個」 ladder
# 問最多可爬到第幾個 building
# 因 bricks 最多有 10^9 個，有點難判斷
# Editorial 裡推薦用 priority queue 或 binary search 法
# 我可理解 binary search 的原因及作法的技巧，不過我想試試 priority queue：
# 先把前k個「高度差」找出來---可用k個梯子解決，或用一堆磚塊解決。
# 接下來繼續往右逐一征服，再從 priority queue 裡，挑小的「高度差」填磚解決。
# 註： Discussions 裡 mstuebs 有分享測資，很好用 XD
class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        heap = [] # proirity queue，會把最小的「高度差取出來
        for i,h in enumerate(heights): # 逐個加入
            if i==0: continue # 避開一開始，因要算 heights[i]-heights[i-1]
            diff = heights[i] - heights[i-1]
            if diff>0: # 需要爬昇的 diff 才需加入 heap 中
                heappush(heap, diff)
            if len(heap)<=ladders: # 還在梯子能處理的範圍
                continue # 就不做下面的處理
            now = heappop(heap) # 取出最小的，想用磚來疊
            if now<=bricks: # 磚還夠用
                bricks -= now
            else: # 磚不夠用，在第i樓失敗
                return i-1 # 因 0-index，在第i-1樓可成功
        return len(heights)-1 # 因 0-index 全部樓都克服囉！
