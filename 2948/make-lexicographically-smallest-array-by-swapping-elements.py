# LeetCode 2948. Make Lexicographically Smallest Array by Swapping Elements
# Solutions 裡 I AM WHO 的解釋示意圖非常好，讓我們容易了解題意及解法
# 任2個數「數值的距離<=limit」便可交換、超過範圍就不能互換位置，所以 nums 便可用 limit 來分群
class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
        N = len(nums)
        table = [[nums[i],i] for i in range(N)]  # 建出對照表，左邊是「值」，右邊是「原本對應的index」位置
        table.sort()  # 照左邊的「值」排序，右邊的 index 很重要，
        parts = [ [table[0]] ] # 要將 table[i] 分群，先把「最小的」放新的一群
        for i in range(1,N):  # 每項與前一項比較
            if table[i][0] - table[i-1][0] > limit:  # 如果兩項的距離太遠，要開新的一群
                parts.append([])  # 開「新的」空白群，後面再慢慢塞
            parts[-1].append(table[i])  # 把 table[i] 塞入「最後的那群」
        ans = [0]*N  # 最後要放答案囉！要照 index 的位置，放好
        for part in parts:  # 把每一群拿來看
            index = sorted([p[1] for p in part])  # 這一群裡，每個元素 p 的 index 拿出來，小到大排好
            for i in range(len(index)):
                ans[index[i]] = part[i][0]  # 把 part[i] 的值，放入「照index小到大排好」的那個位置
        return ans
