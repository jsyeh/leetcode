//我這題的解法 超時。看了別人的 Solutions 發現需要我不熟悉的新技巧&數學觀念
//https://leetcode.com/problems/minimum-jumps-to-reach-home/solutions/978357/c-bidirectional-bfs-solution-with-proof-for-search-upper-bound/?envType=study-plan&envId=graph-i&plan=graph
//https://leetcode.com/problems/minimum-jumps-to-reach-home/solutions/935384/c-bfs/?envType=study-plan&envId=graph-i&plan=graph
//所以之後再解它

class Solution {
public:
    int minimumJumps(vector<int>& forbidden, int a, int b, int x) {
        unordered_set<int> set(forbidden.begin(), forbidden.end());
        vector<vector<int>> visited(2, vector<int>(30000));
        queue<pair<int,bool>>prevJump; //true: backward, false: forward
        prevJump.push({0, false});
        visited[0][0] = 1;
        visited[1][0] = 1;
        int ans = 0;
        while(prevJump.size()>0){
            int N = prevJump.size();
            while(N>0){
                N--;
                int pos = prevJump.front().first;
                bool dir = prevJump.front().second;
                prevJump.pop();
                if(pos == x) {
                    return ans;
                }
                int forward = pos + a;
                int backward = pos - b;
                if(forward<30000 && visited[0][forward]==0 && !set.count(forward)) {
                    prevJump.push({forward, false});
                    visited[0][forward] = 1;
                }
                if(backward>=0 && visited[1][backward]==0 && !set.count(backward) && dir==false) {
                    prevJump.push({backward, true});
                    visited[1][backward] = 1;
                }
            }
            ans++;
        }
        return -1;
    }
};
/*
class Solution {
public:
    queue<int> Q;
    queue<int> dist;
    queue<int> back;
    int minimumJumps(vector<int>& forbidden, int a, int b, int x) {
        int visited[500000]={};//因為可能會到4000後，往回跳2000而到達x(2000)
        sort(forbidden.begin(), forbidden.end());
        Q.push(0);
        dist.push(0);
        back.push(0);//0:不是back, 1:是back

        while(Q.size()>0){
            int now = Q.front();
            Q.pop();
            int d = dist.front();
            dist.pop();
            int bb = back.front();
            back.pop();

            if(now==x) return d;

            if(!binary_search(forbidden.begin(), forbidden.end(), now+a)){
                if(now+a<500000 && visited[now+a]==0){
                    Q.push(now+a);
                    dist.push(d+1);
                    back.push(0);//不是back
                }
            }
            if(bb==0 && !binary_search(forbidden.begin(), forbidden.end(), now-b)){
                if(now-b>=0 && visited[now-b]==0){
                    Q.push(now-b);
                    dist.push(d+1);
                    back.push(1);
                }
            }
        }

        return -1; //永遠到不了
    }
};*/
