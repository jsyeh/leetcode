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
class ValidMinMax {
    boolean valid;
    int min, max;
    ValidMinMax(boolean _v, int _min, int _max) {
        valid = _v;
        min = _min;
        max = _max;
    }
}
class Solution {
    public boolean isValidBST(TreeNode root) {
        ValidMinMax ans = test(root);
        if(ans.valid) return true;
        else return false;
    }
    ValidMinMax test(TreeNode root) {
        if(root.left==null && root.right==null) return new ValidMinMax(true,root.val, root.val);
        if(root.left==null){
            ValidMinMax ans1 = test(root.right);
            if(ans1.valid==false) return ans1;
            if(ans1.min<=root.val) return new ValidMinMax(false, 0, 0);
            return new ValidMinMax(true, root.val, ans1.max);
        }
        if(root.right==null){
            ValidMinMax ans1 = test(root.left);
            if(ans1.valid==false) return ans1;
            if(root.val<=ans1.max) return new ValidMinMax(false, 0, 0);
            return new ValidMinMax(true, ans1.min, root.val);
        }

        ValidMinMax ans1 = test(root.left);
        if(ans1.valid==false) return ans1;
        ValidMinMax ans2 = test(root.right);
        if(ans2.valid==false) return ans2;
        if(ans1.max<root.val && root.val<ans2.min){
            return new ValidMinMax(true, ans1.min, ans2.max);
        }
        return new ValidMinMax(false, 0, 0);
    }
}
