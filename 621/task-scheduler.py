# 有 A-Z 不同的工作，重覆的工作，不能連續做，需要n個cool-down時間
# 做工作，需要時間。等待CD，也需要時間。
# 所以，最難搞定的，是「出現最多」的字母，因為一定要為它預留CD時間
# 只要解決「最難搞定」的字母X，「其他工作」，就插在X的中間即可
# 運氣好的是，如果有「其他工作」能插在X的中間的話，佔了時間，CD值變小
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counter = collections.Counter(tasks) # 統計每個字母出現次數
        H = sorted(counter.values(), reverse=True)
        # 現在H出現次數「從大到小排好」
        task_time = len(tasks)
        sep = H[0]-1 # 以「最多」的H[0]為主，會有 H[0]-1 個間隔
        idle_time = (sep)*n # 最糟的話，CD要等這麼久
        for i in range(1,len(H)): # 看時間能否重疊/放入間隔/省下CD時間
            idle_time -= min(sep, H[i]) # 有幾個可塞入「間隔」，就能省下CD時間
        return task_time + max(0,idle_time) # 間隔CD時間不會是「負」的
