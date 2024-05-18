// LeetCode 979. Distribute Coins in Binary Tree
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */
int ans = 0; // global 變數，放答案
struct CoinAndNode { // 自訂資料結構：發明一個資料結構（大家比較不熟）
    int coinN, nodeN;  // 會把下面全部的金幣、node數，一起存起來
}; //記得要加「分號」
struct CoinAndNode helper(struct TreeNode* root) {  // 自訂函式
    struct CoinAndNode all;  // 把它之下的金幣總數 及 以下node數
    if(root==NULL) {
        all.coinN = 0;
        all.nodeN = 0;
        return all;  // 終止條件
    }
    struct CoinAndNode left = helper(root->left); 
    struct CoinAndNode right = helper(root->right); 
    ans += abs(left.coinN - left.nodeN) + abs(right.coinN - right.nodeN);
    all.coinN = left.coinN + right.coinN + root->val;
    all.nodeN = left.nodeN + right.nodeN + 1;
    // 如果金幣總數 vs. node不符時，這層樓就有金幣要「移轉」。資訊也都要回傳。
    return all;
} // 這是函式的定義，不用加「分號」
int distributeCoins(struct TreeNode* root) {
    ans = 0;  //每次 LeetCode 執行時，都要把 ans 清為0
    helper(root);
    return ans;
}
