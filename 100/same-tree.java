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
    public boolean isSameTree(TreeNode p, TreeNode q) {
        if(p==q)return true;
        if(p==null && q!=null) return false;
        if(p!=null & q==null) return false;

        if(p.val!=q.val) return false;
        if(p.val==q.val){
            if(isSameTree(p.left,q.left) && isSameTree(p.right, q.right)) return true;
            else return false;
        }
        return true;
    }
}
