// LeetCode 1331. Rank Transform of an Array
// 想知道 arr[i] 在 arr 裡對應的 rank 排名（小到大）
// 另外，相同的數，rank 要相同。後面再繼續接著排下去（不用避開）
class Solution {
public:
    vector<int> arrayRankTransform(vector<int>& arr) {
        set<int> arr2(arr.begin(), arr.end()); // C++ set 會自己 sort 好
        unordered_map<int, int> rank(arr2.size()); // 宣告 Hash Map 對照表
        int R = 1; // Rank 從 1 開始排名
        for(int num : arr2){ // arr2 是 sorted set，逐一取出，標上排名
            rank.insert({num, R++}); // 標完排名R後，R++供下一筆使用
        } // num 這個數字，對應排名 R
        for(int i=0; i<arr.size(); i++){ // 將每一格，更新成「對應的rank」
            arr[i] = rank[arr[i]]; // 用 rank[] 查到排名，再塞回去
        }
        return arr;
    }
};
