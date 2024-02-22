# 這題是 a 相信 b, 所以a不是法官
# 把全部的a,b都加入 people 的 set()
# 再把 a 都從 people.remove(a)
# ...其實不用這麼麻煩, n 就直接知道 1..n個人
# 最後看看 people剩誰。但是如果沒有找到法官, 那return -1
# 不過題目真的意思,是「每個人都要相信」法官
# 所以法官要得到 N-1票
class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        if trust == [] and n == 1:
            return 1 # special case
        people = set()
        # 先把全部的a,b都加入 people 的 set()
        trustCount = Counter()
        for a,b in trust:
            people.add(a)
            people.add(b)
            trustCount[b] += 1
        N = len(people)
        for a,b in trust:
            # 再把 a 都從 people.remove(a)
            if a in people: people.remove(a)
        for a in people:
            if trustCount[a] == N-1: return a
        #for judge in people:
        #    return judge
        # 最後看看 people剩誰。但是如果沒有找到裁判, 那return -1
        return -1
        
# case 3/92:　[[1,2],[2,3]] 但是 1不相信3, 所以沒有裁判
# case 4/92: [[1,3],[1,4],[2,3],[2,4],[4,3]]
# case 91/92: n=1, []
