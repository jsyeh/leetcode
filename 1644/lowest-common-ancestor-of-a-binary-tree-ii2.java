// LeetCode 1644. Lowest Common Ancestor of a Binary Tree II
// 想找出 TreeNode p 和 TreeNode q 的共同祖先
class Solution {
    TreeNode returnNode; // 利用 global 變數，放 「祖先是誰」
    int helper(TreeNode root, TreeNode p, TreeNode q) {
        if(root==null) return 0; // 遇到空的，就什麼都沒有(找到 0 個)
        int count = (root==p || root==q) ? 1 : 0; // 先看本身有沒有
        int count1 = helper(root.left, p, q); // 再看左半邊有沒有
        if(count1==2) return 2; // 有，直接放答案
        count += count1;

        int count2 = helper(root.right, p, q); // 再看右半邊有沒有
        if(count2==2) return 2; // 有，直接放答案
        count += count2;

        if(count==2) returnNode = root; // 現在才湊齊2個
        return count;
    }
    public TreeNode lowestCommonAncestor(TreeNode root, TreeNode p, TreeNode q) {
        if(helper(root, p, q)==2) return returnNode;
        return null;
    }
}
/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
