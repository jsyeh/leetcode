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
    int pI = 0; //in preorder[i]
    HashMap<Integer,Integer> inorderI = new HashMap<Integer,Integer>();
    public TreeNode buildTree(int[] preorder, int[] inorder) {
        for(int i=0; i<inorder.length; i++) {
            inorderI.put(inorder[i], i); //build the HashMap
        }
        return buildTree(preorder, 0, preorder.length-1);
    }

    TreeNode buildTree(int[] preorder, int left, int right){
        if(left>right) return null;
        int i = inorderI.get(preorder[pI]);
//        if(left<=i && i<=right){ } //good,有在合理範圍內
//        else return null;

        TreeNode root = new TreeNode(preorder[pI++]);
        root.left = buildTree(preorder, left, i-1);
        root.right = buildTree(preorder, i+1, right);

        return root;
    }
}
