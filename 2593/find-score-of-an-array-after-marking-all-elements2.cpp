// LeetCode 2593. Find Score of an Array After Marking All Elements
// 每次挑「最小」數，刪掉它及2個的鄰居，重覆做到結束。問「挑」了哪些數（加起來總和）
// C++ 再寫一次，換用 sort() 的方法，配合 pair 來塞「複合資料」，速度就變快了10倍。
// 還不知道為什麼會快那麼多。可能是原本的程式裡，有「耗時過多」浪費的地方吧。
// 程式碼也變簡單很多。我比較喜歡「簡單清爽」的程式 <3
class Solution { 
public:
    long long findScore(vector<int>& nums) {
        int N = nums.size(); // 總共 N 個數
        vector<pair<int,int>> sorted(N); // 複合資料，裡面有 nums[index]，及index
        for (int i=0; i<N; i++) { // 把原始 nums[i] 及 index 塞入 sorted 陣列
            sorted[i] = make_pair(nums[i], i);
        }
        sort(sorted.begin(), sorted.end()); // 並且真的「從小到大排好
        
        long long int ans = 0;
        // 原始 nums[index] 如果變成 -1 對應「此數被刪掉了」
        for (int i=0; i<N; i++) {
            int now = sorted[i].first; // 目前最小的數的值
            int index = sorted[i].second; // 對應原本 nums[index] 的 index
            if(nums[index]==-1) continue; //  -1 對應「此數被刪掉了」，換下一個

            ans += now; // 沒有刪掉，那就拿來用
            nums[index] = -1; // 並標示「已刪除」
            if(index-1>=0) nums[index-1] = -1; // 原始位置的左邊，標示「已刪除」
            if(index+1<N) nums[index+1] = -1; // 原始位置的左邊，標示「已刪除」
        }
        return ans;
    }
};
