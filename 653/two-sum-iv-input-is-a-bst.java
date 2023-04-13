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
    TreeNode root0;
    public boolean findTarget(TreeNode root, int k) {
        root0 = root;
        return travel(root, k);
    }
    boolean findTargetFromRoot(TreeNode root, int others, TreeNode self) {
        if(root==null) return false;
        if(root.val == others && self!=root) return true;
        if(findTargetFromRoot(root.left,others,self) || findTargetFromRoot(root.right,others,self)) return true;
        return false;        
    }
    boolean travel(TreeNode root, int k) {
        if(root==null) return false;
        if(findTargetFromRoot(root0, k-root.val,root)) return true;
        if(root.left!=null && travel(root.left, k)) return true;
        if(root.right!=null && travel(root.right, k)) return true;
        return false;
    }
}//case3: [1] 2 不可以自己找到自己 1+1=2 因為自己只能用一次
