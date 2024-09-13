// LeetCode 1310. XOR Queries of a Subarray
// queries[i] 有範圍left,right，把 arr[left]...arr[right] 算出 XOR 的結果
// 可仿效 preSum 的方法，把 preXor 算出來，再用「扣除」的概念，就可快速推算出答案
class Solution {
public:
    vector<int> xorQueries(vector<int>& arr, vector<vector<int>>& queries) {
        vector<int> preXor;
        preXor.push_back(0); //凡事從0開始
        // 建出 Xor 表格，對應arr[0]... arr[i] 的 Xor 結果
        int i=0;
        for(int num : arr) {
            preXor.push_back(preXor[i] ^ arr[i]);
            i++;
        }

        vector<int> ans;
        for(auto query : queries) { // query[0] 左界 ... query[1] 右界
            int left = query[0], right = query[1];
            ans.push_back(preXor[right+1] ^ preXor[left]);
            // 多了 preXor[0], 所以 [left...right] 對應到 [left+1...right+1]
            // 要扣除的時候，就 preXor[right+1] 扣除 preXor[left]
        }
        return ans;
    }
};
