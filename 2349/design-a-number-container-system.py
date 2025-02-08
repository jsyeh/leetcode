# LeetCode 2349. Design a Number Container System
# 設計「資料結構」：change(i,number) 要將nums[i]的值改掉
# find(number) 要找出「目前此 number」的最小 index。（若無，就-1）
class NumberContainers:
    def __init__(self):
        # 因 index 的範圍有 10^9 太大，所以用 Hash Map 省空間
        self.nums = {}  # 正著放：index -> number, nums[i] = number 
        # 呼叫 10^5 次，需快速得到「最小」的index，最適合用 heap，heap[number] 裡有一堆 index
        self.heaps = defaultdict(list)  # 倒著放：每個 number 對應一個 index heap

    def change(self, index: int, number: int) -> None:
        if index in self.nums and self.nums[index]==number:
            return  # 這麼巧，原本的值就是它，就直接結束
        self.nums[index] = number  # 正著放：index -> number
        heappush(self.heaps[number], index)  # 倒著放：number -> index
    
    def find(self, number: int) -> int:
        heap = self.heaps[number]  # 這個 number 對應的 heap
        while heap:  # heap 裡還有 index（我們需要「有效、正確」的index）
            index = heap[0]  # 目前最小的 index
            if self.nums[index] == number:  # 很好，剛好值正確
                return index  # 這就是答案
            heappop(heap) # 不然的話，就代表index無效，要吐掉
        return -1
