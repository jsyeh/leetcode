# LeetCode 1678. Goal Parser Interpretation
# 遇到 () 就變成 'o'
class Solution:
    def interpret(self, command: str) -> str:
        command = command.replace('()', 'o')
        command = command.replace('(al)', 'al')
        return command
