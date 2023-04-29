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
class Solution {
public:
    TreeNode* sortedArrayToBST(vector<int>& nums) {
        return genTree(nums, 0, nums.size());
    }
    TreeNode * genTree(vector<int>&nums, int i, int j) {
        if(i>=j) return nullptr;

        int mid = (i+j)/2;
        TreeNode * ans = new TreeNode(nums[mid]);
        ans->left = genTree(nums, i, mid);
        ans->right = genTree(nums, mid+1, j);
        return ans;
    }
};
