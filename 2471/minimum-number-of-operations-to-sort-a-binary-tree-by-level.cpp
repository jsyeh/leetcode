// LeetCode 2471. Minimum Number of Operations to Sort a Binary Tree by Level
// 每次可在「同一層」挑2個 node 交換 val值。要交換幾次，才能「每一層」都排序好？
class Solution {
public: // 程式的寫法，與 Python 版類似。可參考 Python 版的註解
    void helper(TreeNode* root, int level, vector<vector<pair<int,int>>>& levelArray) {
        if(root==nullptr) return;
        if(levelArray.size()<=level) levelArray.push_back(vector<pair<int,int>>{});
        int index = levelArray[level].size();
        levelArray[level].push_back(make_pair(root->val, index));
        helper(root->left, level+1, levelArray);
        helper(root->right, level+1, levelArray);
    }
    int minimumOperations(TreeNode* root) {
        vector<vector<pair<int,int>>> levelArray;
        helper(root, 0, levelArray);
        int ans = 0;
        for(auto array : levelArray) {
            sort(array.begin(), array.end());
            for(int i=0; i<array.size(); i++) {
                while(array[i].second != i) {
                    int i2 = array[i].second;
                    swap(array[i], array[i2]);
                    ans++;
                }
            }
        }
        return ans;
    }
};
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */

