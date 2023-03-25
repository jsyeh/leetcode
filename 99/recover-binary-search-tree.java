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
    ArrayList<TreeNode> array;
    public void recoverTree(TreeNode root) {
        //找到左邊最大的、右邊最小的, 再看是不是要改。
        //Solution 2: 把BST壓平,再看是不是遞增,便能找到錯誤的2個
        //TreeNode [] line; //配上 DFS 也就是函式呼叫函式, In-order 的方式, 便能得到陣列的值
        array = new ArrayList<TreeNode>();
        inOrder(root);

        TreeNode error1 = null, error2 = null;
        int error=0;
        for(int i=1; i<array.size(); i++){
            if(array.get(i-1).val > array.get(i).val){
                if(error==0){//第一次出錯, 記得左邊
                    error1 = array.get(i-1);
                    error2 = array.get(i); //有時候只會出錯(相鄰出錯), 所以順手記得右邊的值
                } else { //第二次的右邊
                    error2 = array.get(i);
                }
                error++;//出錯的點,是第一次的左邊、第二次的右邊
            }
        }
        int temp = error1.val;
        error1.val = error2.val;
        error2.val = temp;
    }
    void inOrder(TreeNode root) {
        if(root.left!=null) inOrder(root.left);
        array.add(root);
        if(root.right!=null) inOrder(root.right);
    }
}
