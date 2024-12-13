// LeetCode 2593. Find Score of an Array After Marking All Elements
class Solution { // 每次挑「最小」數，刪掉它及2個的鄰居，重覆做到結束。問「挑」了哪些數（加起來總和）
public:
    long long findScore(vector<int>& nums) {
        long long int ans = 0;
        int N = nums.size(), remains = nums.size(); // 總共 N 個數，減到結束為止
        priority_queue<vector<int>> heap; // 數很多，不能暴力2層for迴圈。需巧妙用 heap 資料結構
        for (int i=0; i<N; i++) { // nums[i] 先塞入 priority queue 裡
            heap.push(vector<int>{-nums[i], -i});
        } // 因 C++ 的 priority_queue 會先取大，所以加「負號」
        while (remains>0) { // remains 對應：現在 nums 裡，剩幾個數「還沒被刪除」
            auto now = heap.top(); // 待刪的數
            heap.pop(); // 真的刪掉
            while (nums[-now[1]]==-1) { // 「已刪除」的數，nums[index]會 設 -1
                now = heap.top(); // 剛剛挑的數「已刪除」，只好再挑1個數
                heap.pop();
            } // 離開 while 迴圈時，now 必定是「最小」的「未挑過的數」
            ans += - now[0]; // 將數字加到ans裡（用「負號」還原）
            int i2 = - now[1]; // 挑出來的數，對應的 index（用「負號」還原）
            nums[i2] = -1; // 已刪掉的數，nums[index] 設 -1 
            remains--; // 挑走，就用掉1個數
            if (i2+1<N && nums[i2+1]!=-1) { // 右邊那個數，還沒被刪除
                nums[i2+1] = -1; // 設成「已刪除」-1
                remains--; // 再少1個數
            }
            if (i2-1>=0 && nums[i2-1]!=-1) { // 左邊那個數，還沒被刪除
                nums[i2-1] = -1; // 設成「已刪除」-1
                remains--; // 再少1個數
            }
        }
        return ans;
    }
};
