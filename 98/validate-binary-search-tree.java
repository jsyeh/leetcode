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
    public boolean isValidBST(TreeNode root) {
        TreeNode left = root, right = root;
        while(left.left!=null){
            left = left.left;
        }
        while(right.right!=null){
            right = right.right;
        }
        if(left!=root && left.val>=root.val) return false;
        if(root!=right && root.val>=right.val) return false;
        if(left!=right && left.val>=right.val) return false;

        return isValidBST(root, left, right);
    }
    boolean isValidBST(TreeNode root, TreeNode left, TreeNode right) {
        if(root.val==left.val && root!=left) return false;
        if(root.val==right.val && root!=right) return false;

        if(root.val<=left.val && root!=left) return false;
        if(right.val<=root.val && root!=right) return false;
        //if(root==left) return true;
        //if(root==right) return true;
        //if(root.val<=left.val || right.val<=root.val) return false;

        boolean ans=true;
        if(root.left!=null) ans = isValidBST(root.left, left, root);
        if(ans==false) return false;
        if(root.right!=null) ans = isValidBST(root.right, root, right);
        if(ans==false) return false;
        return ans;

    }
}//Case3: [2,2,2]
//Case4: [1,1]
//Case5: [0,null,-1]
//Case6: [0]
//Case7: [32,26,47,19,null,null,56,null,27]
