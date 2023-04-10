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
    int ans=0;
    public int maxDepth(TreeNode root) {
        tree(root, 1);
        return ans;
    }
    void tree(TreeNode root, int level) {
        if(root==null) return;
        if(level>ans) ans = level;
        if(root.left!=null) tree(root.left, level+1);
        if(root.right!=null) tree(root.right, level+1);
    }
}
