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
    public boolean isSubtree(TreeNode root, TreeNode subRoot) {
        if(root==null && subRoot==null) {print(root);return true;}
        if(root==null || subRoot==null) return false;
        if(perfectSubTree(root, subRoot)) return true;

        if(isSubtree(root.left, subRoot)) {print(root);return true;}
        if(isSubtree(root.right, subRoot)) {print(root);return true;}
        return false;
    }
    boolean perfectSubTree(TreeNode root, TreeNode subRoot) {
        if(root==null && subRoot==null) {print(root);return true;}
        if(root==null || subRoot==null) return false;
        if(root.val==subRoot.val && perfectSubTree(root.left,subRoot.left) && perfectSubTree(root.right,subRoot.right)) {print(root);return true;}
        return false;
    }
    void print(TreeNode root) {
        if(root==null) System.out.println("null");
        else System.out.println(root.val);
    }
}//case 177/182: [3,4,5,1,null,2] [3,1,2]
