# LeetCode 1598. Crawler Log Folder
# 要在電腦的目錄裡面走來走去。如果是 '../' 就是往上一層目錄走
# 如果是 './' 就留在原地。其他的，就越走越深。問最後的深度。
class Solution:
    def minOperations(self, logs: List[str]) -> int:
        depth = 0
        for log in logs:
            if log == '../':
                depth = max(0, depth-1)
            elif log!='./':
                depth += 1
        return depth
