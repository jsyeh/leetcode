class Solution {
public:
    int openN = 1;
    int visited[1000] = {1,0};//只有第1間有開，其他間房間等待打日弓一廿
    bool canVisitAllRooms(vector<vector<int>>& rooms) {
        helper(rooms, 0);
        if(openN==rooms.size()) return true;
        else return false;
    }
    void helper(vector<vector<int>>& rooms, int now) {
        for(int key : rooms[now]) {
            if(visited[key]) continue;

            openN++;
            visited[key]=1;
            helper(rooms, key);
        }
    }
};
