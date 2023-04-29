/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    public int diameterOfBinaryTree(TreeNode root) {
        length(root);
        return ans;
    }
    int ans=0;
    int length(TreeNode root) {
        if(root==null) return 0; // or -1
        int right = length(root.right);
        int left = length(root.left);
        if(right+left>ans) ans = right + left;
        
        if(right>left) return right+1;
        else return left+1;
    }
}
