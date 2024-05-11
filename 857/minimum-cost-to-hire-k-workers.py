# LeetCode 857. Minimum Cost to Hire K Workers，是 Hard 題
# 每位員工有「期望薪資」。在聘人時，要符合規則：「quality若是n倍」，「給出的薪資也要n倍」。
# 也就是要照 quality 的比例，來給薪資。照這樣規則，「慣老板」最少要付多少錢，才能請k個人。
# 所以「先照quality」了解最後薪資的倍數，再看「挑哪些人」符合期薪薪資以上的規則。
# 最後我是使用 lee215 的解法，也就是每個人有對應的ratio值，最划算的在前面挑。
# 利用 ratio * qsum 能快速算出「目前累積k位low quality的員工的薪水」
class Solution:
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], k: int) -> float:
        N = len(quality)
        # 等下要用來排序的關鍵，是便宜比例值 ratio = wage[i]/quality[i]，
        # 因希望同樣quality時，薪水要少。再用 quality[i] 來回推出薪水
        table = [(wage[i] / quality[i], quality[i]) for i in range(N)]
        table.sort()  # 從小到大排好
        ans = inf
        qsum = 0  # 目前收的最便宜的員工，累積的quality值，用來算出薪水(挑最low quality的k人)
        heap = []  # 會吐出最便宜比例值 ratio 的員工資訊
        for ratio, q in table:  # 依「便宜比例值」ratio 逐一取出
            heappush(heap, -q)  # 稍後將以 quality 高的人「優先丟掉」，故塞入 -q 在heap取出小值時能用
            qsum += q  # 如果用了現在這個人，他的 quality q 要加入 qsum （目前累積low quality的qsum）
            if len(heap) > k: qsum += heappop(heap)  # 取出 -q 不要用高品質的人，「優先丟掉」
            if len(heap) == k: ans = min(ans, qsum * ratio)  # 照現在的 ratio 給薪水，給最low quality的k人
        return ans
