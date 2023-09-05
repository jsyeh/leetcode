class Solution:
    def calPoints(self, operations: List[str]) -> int:
        table = []
        for op in operations:
            if op=="+":
                table.append(table[-1]+table[-2])
            elif op=="D":
                table.append(table[-1]*2)
            elif op=="C":
                table.pop()
            else:
                table.append(int(op))
        return sum(table)        
