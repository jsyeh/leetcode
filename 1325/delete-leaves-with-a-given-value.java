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
    int modify=0;
    public TreeNode removeLeafNodes(TreeNode root, int target) {
        while(true) {
            modify = 0;
            root = removing(root, target);
            if(modify==0) break;
        }
        return root;
    }
    TreeNode removing(TreeNode root, int target) {
        if(root==null) return root;
        if(root.left==null && root.right==null) {
            if(root.val==target){
                modify++;
                return null;
            }
            else return root;
        }
        root.left = removing(root.left, target);
        root.right = removing(root.right, target);            
        return root;
    }
}
