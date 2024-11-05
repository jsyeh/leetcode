// LeetCode 2138. Divide a String Into Groups of Size k
// 將字串切成「k個為1群」，最後不足k個時，用fill來補
class Solution {
public:
    vector<string> divideString(string s, int k, char fill) {
        vector<string> ans;
        for(int i=0; i<s.length(); i+= k) {
            if(i+k-1<s.length()) ans.push_back(s.substr(i,k));
            else { // 最後不足時，用 fill 來塞
                string now = s.substr(i, k);
                for(int a=s.length()%k; a<k; a++){
                    now += fill;
                }
                ans.push_back(now);
            }
        }
        return ans;
    }
};
