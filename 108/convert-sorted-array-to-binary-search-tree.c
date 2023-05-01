/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */

int nodeN = 0;
struct TreeNode* nodes = NULL;
// C語言，不能使用全域變數，不然多筆測資會出現問題
// 或著，要記得 reset nodeN

struct TreeNode* sortedArrayToBST3(int* nums, int left, int right){
    if(left==right) return NULL; //右不包含
    if(left+1==right){
        struct TreeNode* root = nodes + (nodeN++);
        root->val = nums[left];
        root->left=NULL;
        root->right=NULL;
        return root;
    }

    int mid = (left+right)/2;
    struct TreeNode* root = nodes + (nodeN++);
    root->val = nums[mid];
    root->left = sortedArrayToBST3(nums, left, mid);
    root->right = sortedArrayToBST3(nums, mid+1, right);
    return root;
}

struct TreeNode* sortedArrayToBST(int* nums, int numsSize){
    nodes = (struct TreeNode*)malloc(sizeof(struct TreeNode)*numsSize*2);
    nodeN = 0;
    struct TreeNode* root = sortedArrayToBST3(nums, 0, numsSize);
    return root;
}
