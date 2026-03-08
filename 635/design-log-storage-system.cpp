// LeetCode 635. Design Log Storage System
// 使用 C++ 的 set() 它是 ordered 可善用 lower_bound() upper_bound() 及 for迴圈，找答案
class LogSystem {
public:
    set<pair<string,int>> log;
    LogSystem() {
        
    }
    
    void put(int id, string timestamp) {
        log.insert(pair(timestamp,id)); // insert() 插入 ordered set()
    }
    unordered_map<string,int> len { // 快速對照表，了解「到 timestamp 幾個字母」
        {"Year",4},{"Month",7},{"Day",10},{"Hour",13},{"Minute",16},{"Second",19}
    };
    string genQuery(string timestamp, string granularity) {
        string ans = timestamp.substr(0, len[granularity]);
        //cout << "genQuery() " << ans << endl;
        return ans;
    }
    vector<int> retrieve(string start, string end, string granularity) {
        
        auto itStart = log.lower_bound({genQuery(start, granularity),0});
        auto itEnd = log.upper_bound({genQuery(end, granularity)+"z", 501});
        vector<int> ans;
        for (auto it = itStart; it != itEnd; it++) {
            ans.push_back(it->second);
        }

        return ans;
    }
};

/**
 * Your LogSystem object will be instantiated and called as such:
 * LogSystem* obj = new LogSystem();
 * obj->put(id,timestamp);
 * vector<int> param_2 = obj->retrieve(start,end,granularity);
 */
