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
    //table裡，有全部的答案
    HashMap<Integer,List<TreeNode>> table = new HashMap<>();
    //快速查表 if(table.containsKey(i)) return table.get(i)
    //否則就要先算出ans後，再 table.put(i, ans); 再 return ans
    public List<TreeNode> allPossibleFBT(int n) {
//System.out.println(n); //debug時，確認 n 都是奇數
        //有個奇怪的規則：node數必須是奇數，因為每個node只有0 or 2個小孩。
        //每次在裁左半邊、右半邊時，也要是奇數、奇數去裁
        if(n%2==0) return new ArrayList<>(); //n必為奇數，遇到偶數無法計算/沒有答案

        if(table.containsKey(n)) return table.get(n); //有答案，直接回傳

        List<TreeNode> ans = new ArrayList<TreeNode>();
        if(n==1) { //最簡單的case,只有1個點
            TreeNode one = new TreeNode();
            ans.add(one);
            table.put(1, ans); //就算只有1個點，也要回收再利用
            return ans;
        } //n==1時，因根本沒有left, right 的小孩，無法用下面迴圈來切
        for(int k=1; k<n; k+=2){ //還沒算過，就慢慢算。左右都要有樹
            //每次在裁左半邊、右半邊時，也要是奇數、奇數去裁
            //左右的樹，都會是奇數哦！ 左樹有奇數k，右樹 n-1-k也是奇數，
            //加起來是n-1個點，因root也用掉1個點
            List<TreeNode> lefts = allPossibleFBT(k); //左邊奇數k個node
            List<TreeNode> rights = allPossibleFBT(n-1-k); //右邊奇數n-1-k個node
            //下面用暴力迴圈，把所有可能都接起來
            for(TreeNode left : lefts){
                for(TreeNode right : rights){
                    TreeNode tree = new TreeNode(0, left, right);
                    ans.add(tree); //做出(接出)1顆新的tree
                }
            }
        }
        table.put(n, ans);
        return ans;
    }
}
//題目只input n, 卻要建出「全部可能的」full binary tree
//可用函式呼叫函式，如果用了一個node當root,再利用for迴圈，把左邊、右邊都建出來
//但 n<=20 會讓答案太多，所以要事先記下可能的subtree 的形狀，重覆利用，省空間

