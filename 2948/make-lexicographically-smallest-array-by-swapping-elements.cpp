// LeetCode 2948. Make Lexicographically Smallest Array by Swapping Elements
// Solutions 裡 I AM WHO 的解釋示意圖非常好，讓我們容易了解題意及解法，在能交換的情況下，讓 nums 儘量「小到大」
// 任2個數「數值的距離<=limit」便可交換、超過範圍就不能互換位置，所以 nums 便可用 limit 來分群
class Solution {
public:
    vector<int> lexicographicallySmallestArray(vector<int>& nums, int limit) {
        int N = nums.size();
        vector<pair<int,int>> table(N);
        for(int i=0; i<N; i++){ // 建出對照表，左邊是「值」，右邊是「原本對應的index」位置
            table[i] = {nums[i], i}; // 把「值」和「原本位置index」塞在一起
        }
        sort(table.begin(), table.end()); // 照左邊的「值」小到大排序好，右邊的 index 很重要
        vector<vector<pair<int,int>>> groups(1, vector<pair<int,int>>());
        groups[groups.size()-1].push_back(table[0]); // 將 table[i] 分群，先把「最小的」table[0]放新的一群
        for(int i=1; i<N; i++) { // 每項與前一項比較
            if(table[i].first - table[i-1].first > limit) { // 兩相鄰的「值」差太遠，要分開2群
                groups.push_back(vector<pair<int,int>>()); // 開「新的」空白群，後面再慢慢塞
            }
            groups[groups.size()-1].push_back(table[i]); // 把 table[i] 塞入「最後的那群」
        }
        vector<int> ans(N); // 最後要放答案囉！要照 index 的位置，放好
        for(auto part : groups) { // 把每一群拿來看
            vector<int> index;
            for(auto p : part) {
                index.push_back(p.second);
            } // 這一群裡，每個元素 p 的 index 拿出來，小到大排好
            sort(index.begin(), index.end());
            for(int i=0; i<index.size(); i++) {
                ans[index[i]] = part[i].first;
            } // 把 part[i] 的值，放入「照index小到大排好」的那個位置
        }
        return ans;
    }
};
