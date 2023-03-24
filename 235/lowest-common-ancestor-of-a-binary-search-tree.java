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
        ArrayList<TreeNode> path1 = new ArrayList<TreeNode>();
        ArrayList<TreeNode> path2 = new ArrayList<TreeNode>();

        binarySearch(root, p, path1);
        binarySearch(root, q, path2);
        TreeNode ans = root;
        for(int i=0; i<path1.size() && i<path2.size(); i++) {
            if(path1.get(i)==path2.get(i)) ans = path2.get(i);
            if(path1.get(i)!=path2.get(i)) break;
        }
        return ans;
    }
    void binarySearch(TreeNode root, TreeNode p, ArrayList<TreeNode> path) {
        path.add(root);
        if(p.val == root.val) return;
        if(p.val < root.val) {
            binarySearch(root.left, p, path);
        }else if(p.val > root.val) {
            binarySearch(root.right, p, path);
        }
    }
}//Case4: [2,1] 1 2
