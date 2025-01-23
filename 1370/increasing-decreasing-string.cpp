// LeetCode 1370. Increasing Decreasing String
// s 要變出新字串，規則：先挑最小，再挑「不重覆」的最小，直到挑不到。
// 再挑大，再挑「不重覆」的最大，直到挑不到。重覆做。
class Solution {
public:
    string sortString(string s) {
        vector<int> freq(26); // 存放 26 個字母的出現次數
        for(char c : s) {
            freq[c-'a']++;
        }
        vector<pair<int,int>> counter;
        for(int i=0; i<26; i++) { // 建立精簡的 counter 表格數量
            if(freq[i]!=0) counter.push_back({i,freq[i]});
        }
        string ans = "";
        while(counter.size()>0) { // 持續做到 counter 用完
            for(int i=0; i<counter.size(); i++) { // 小到大
                ans += 'a'+counter[i].first;
                counter[i].second--;
                if(counter[i].second==0) { // 用完，就刪除
                    counter.erase(counter.begin()+i);
                    i--; // 補回，以便下一輪能正確拼接
                }
            }
            for(int i=counter.size()-1; i>=0; i--) { // 大到小
                ans += 'a'+counter[i].first;
                counter[i].second--;
                if(counter[i].second==0) { // 用完，就刪除
                    counter.erase(counter.begin()+i);
                }
            }
        }
        return ans;
    }
};
