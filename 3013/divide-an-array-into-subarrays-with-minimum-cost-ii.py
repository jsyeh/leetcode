# LeetCode 3013. Divide an Array Into Subarrays With Minimum Cost II
# 將 nums 切成 k 份，第0份包含 nums[0]，剩下 k-1份的頭的 index 距離 <= dist
# 可用長度(dist+1)的毛毛蟲（頭尾差dist)，找體內「重點」最小的(k-1)個數「加總最小」，往右滑行、更新答案
class Solution:
    def minimumCost(self, nums: List[int], k: int, dist: int) -> int:
        # 下面是模仿 Ian 在 Solutions 裡的 Key Insight
        total = nums.pop(0)  # 先把 nums[0] 放入 total cost 裡，之後專注在剩下的陣列
        # SortedList 能有效率將數字小到大排好，雖非 Python 內建，但剛好 LeetCode 可用
        body = SortedList(nums[:dist])  # 剩下陣列的前dist項（毛毛蟲的身體），會吃1格、吐1格
        total += sum(body[:k-2])  # total 含 nums[0] 及毛毛蟲體內「較小的k-2個數」，將再補1個數
        ans = inf  # 先設成 inf 無限大，再依序去找最小值
        for left, right in zip(nums, nums[dist:]):  # 慢慢往右滑動，會吃1格right、吐1格left
            body.add(right)  # 毛毛蟲右邊的頭，多吃1格right，長度變(dist+1)剛好 index <= dist
            if right <= body[k-2]:  # 新加入的數，若剛好比第(k-1)的數小，是「重點」最小的(k-1)個數
                total += right  # 那 right 可「放入 total」
            else:  # 剛吃入的數，不列入「重點」最小的(k-1)個數
                total += body[k-2]  # 改將原本毛毛蟲體內 body[k-2] 也就是第(k-1)小的數「放入total」

            ans = min(ans, total)  # 更新答案，total是nums[0] + 毛毛蟲體內最小的(k-1)個數 

            if left <= body[k-2]:  # 將吐掉的數，是體內「重點」最小的(k-1)個數的其中一員
                total -= left  # left 將永遠離開 total，扣掉它
            else:  # 將吐掉的數，不列入「重點」最小的(k-1)個數
                total -= body[k-2]  # 「再次」將「邊緣」的那個第(k-1)小的數「暫時移出」
            body.remove(left)  # 毛毛蟲左邊尾巴吐掉1個數，長度變(dist)
        return ans
