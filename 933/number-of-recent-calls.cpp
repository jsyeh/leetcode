// LeetCode 933. Number of Recent Calls
// 電腦網路，有個指令 ping 可看有沒有回應，範圍是3秒內。現在照時間ping
// 問現在t時間，有幾個 ping 還在 3 秒內。
class RecentCounter {
public:
    queue<int> Q;
    RecentCounter() {
        
    }
    
    int ping(int t) {
        Q.push(t);
        while (t-Q.front()>3000) {
            Q.pop();
        }
        return Q.size();
    }
};

/**
 * Your RecentCounter object will be instantiated and called as such:
 * RecentCounter* obj = new RecentCounter();
 * int param_1 = obj->ping(t);
 */
