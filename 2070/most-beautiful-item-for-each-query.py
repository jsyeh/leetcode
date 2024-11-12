# LeetCode 2070. Most Beautiful Item for Each Query
# 每個 items 裡有 price 和 beauty 的值
# 每次 query 時，要找到 price < queries[i] 的最 beauty 的值
class Solution:
    def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:
        items.sort()  # 先照 price 從小到大排好
        beauty = items[0][1] # 接著修改 price 對應 beauty值，改記「它以下最beauty值」漸增
        for item in items:
            if item[1]<beauty:  # 值更小，改成最beauty值
                item[1] = beauty
            else: # 值更大，改 beauty 值
                beauty = item[1]
        ans = []
        for query in queries:  # 針對每個query值，使用 binary search 找到「插在右邊的位置」
            i = bisect_right(items, query, key=lambda x:x[0])  # 比對法：用 items[i][0] price 比
            if i==0: ans.append(0)  # 若要插入的位置在0，表示左邊沒任何東西，沒有適合的 item 能用
            else: ans.append(items[i-1][1])  # 要插在 i，表示 i-1 是「等於」或「更小」的值，符合題意
        return ans
