/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */

class Solution {
    public TreeNode lowestCommonAncestor(TreeNode root, TreeNode p, TreeNode q) {
        ArrayList<TreeNode> path1 = binarySearch(root, p);
        ArrayList<TreeNode> path2 = binarySearch(root, q);

        TreeNode ans=null;
        for(int i=0; i<path1.size() && i<path2.size(); i++){
            TreeNode p1 = path1.get(i);
            TreeNode p2 = path2.get(i);
System.out.println(p1.val + " " + p2.val);
            if(p1.val == p2.val) ans = p1;
        }
        return ans;
    }
    ArrayList<TreeNode> binarySearch(TreeNode root, TreeNode p){
        ArrayList<TreeNode> ans = new ArrayList<TreeNode>();
        ans.add(root);
        if(root.val==p.val) return ans;
        if(root.val<p.val){
            ans.addAll(binarySearch(root.right, p));
        }else {
            ans.addAll(binarySearch(root.left, p));
        }
        return ans;
    }
}
