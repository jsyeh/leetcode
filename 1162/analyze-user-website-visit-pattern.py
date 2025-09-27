# LeetCode 1152. Analyze User Website Visit Pattern
# username[i] 在 timestamp[i] 點擊網址 website[i] 
# 找出「3個網址」的參觀順序「出現最多人」的點擊順序。(可跳、不用連女火土田難點)
class Node:
    def __init__(self, name, timestamp, website):
        self.name = name
        self.timestamp = timestamp
        self.website = website


class Solution:
    def mostVisitedPattern(
        self, username: List[str], timestamp: List[int], website: List[str]
    ) -> List[str]:
        nodes = [
            Node(name, ts, site)
            for name, ts, site in zip(username, timestamp, website)
        ]
        nodes.sort(key=lambda x: x.timestamp)
        user_visits = defaultdict(list)
        for node in nodes:
            user_visits[node.name].append(node)

        route = defaultdict(int)
        for visits in user_visits.values():
            tmp = set()
            for i, j, k in combinations(range(len(visits)), 3):
                path = (visits[i].website, visits[j].website, visits[k].website)
                tmp.add(path)
            for path in tmp:
                route[path] += 1

        max_count = -1
        result = ()
        for path, count in route.items():
            if count > max_count or (count == max_count and path < result):
                max_count = count
                result = path
        return list(result)
        
