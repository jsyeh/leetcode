/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
//這題的想法，就是把 p 的 path找出來，q 的 path找出來，再看最後重覆的root在哪裡
class Solution {
    ArrayList<TreeNode> path1 = new ArrayList<>();
    ArrayList<TreeNode> path2 = new ArrayList<>();
    public TreeNode lowestCommonAncestor(TreeNode root, TreeNode p, TreeNode q) {
        dfs(root, p, path1); //把 p 經過的 path 都存在 path1
        dfs(root, q, path2);
//for(int i=0; i<path1.size(); i++){
//    System.out.print(" path1:" + path1.get(i).val);
//} //原來會倒過來
//System.out.println();
//for(int i=0; i<path2.size(); i++){
//    System.out.print(" path2:" + path2.get(i).val);
//} //原來會倒過來
//System.out.println();
        if(path1.size()==0 || path2.size()==0) return null;
        //如果沒有路徑存在，就不能跑下面的迴圈去測試，直接提早結束
        TreeNode ans = null;
        int N1 = path1.size(), N2 = path2.size();
        for(int i=0; i<N1 && i<N2; i++) {
//System.out.println("path1:"+path1.get(i).val);
//System.out.println("path2:"+path2.get(i).val);
            if(path1.get(N1-1-i).val == path2.get(N2-1-i).val) ans = path1.get(N1-1-i);
        }
        return ans;
    }
    boolean dfs(TreeNode root, TreeNode p, ArrayList<TreeNode> path) {
        if(root==null) return false; //沒找到
        if(root.val==p.val) {
            path.add(root);
            return true; //find the node
        }
        if(dfs(root.left, p, path)) {
            path.add(root);
            return true;
        }
        if(dfs(root.right, p, path)) {
            path.add(root);
            return true;
        }
        return false;
    }
}
//case6/80: [18063,15565,null,4053,null,10384,null,15163,null,6178,null,null,411,9784,null,16557,null,1439,null,6019]
//16557
//15163 原來我的程式有打字打錯 N1 N2 寫成 N1 N1
