// LeetCode 3264. Final Array State After K Multiplication Operations I
// 進行 k 次操作：找最小值，把它乘上 multiplier 再放回去
class Solution {
public:
    vector<int> getFinalState(vector<int>& nums, int k, int multiplier) {
        priority_queue<pair<int,int>> heap; // 使用 C++ 的 priority_queue 裡面有 nums[i],i 資訊
        for (int i=0; i<nums.size(); i++) { // 把全部的數（及它的index i ）放入 heap 裡
            heap.push(make_pair(-nums[i],-i)); // 因 priority_queue 會「取大的」，所以加「負號」找最小的
        } // 若「相同小」時，取「最左邊」的數，所以 index 也要加「負號」
        for (int kk=0; kk<k; kk++) {
            auto now = heap.top();
            int i = -now.second; // 最小的數，對應的 index i （再加回「負號」）
            nums[i] *= multiplier; // 乘上 multiplier 倍
            heap.pop(); // 取出舊的數值
            heap.push(make_pair(-nums[i],-i)); // 放回「乘上 mulitplier倍」的數值
        }
        return nums;
    }
};
