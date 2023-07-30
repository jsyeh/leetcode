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
//如何判斷subtree一樣？可用HashSet 把subtree變成String，看有無contains()它
//因為字串會越加越長，好像比較沒有效率，Editorial裡有講另一種作法，
// 是利用 HashMap 把 subtree 變成 unique ID, 再組合「小字串」
class Solution {
    HashMap<String,Integer> map = new HashMap<>(); // String to ID
    List<TreeNode> ans = new ArrayList<>();
    List<Integer> ansID = new ArrayList<>();
    int ID = 1;
    public List<TreeNode> findDuplicateSubtrees(TreeNode root) {
        helper(root);
        return ans;
    }
    int helper(TreeNode root) { //會 return ID
        int left=-1, right=-1;
        //if(root==null) return -1;
        if(root.left!=null) left = helper(root.left);
        if(root.right!=null) right = helper(root.right);
        String str = ""+left+","+root.val+","+right;
//System.out.println("now: "+str);
        if(!map.containsKey(str)){
            map.put(str,ID);
//System.out.println(str+":"+ID);
            return ID++;
        }else{
            int id = map.get(str);
            if(!ansID.contains(id)){
                ansID.add(id);
                ans.add(root);
//System.out.println("contain: "+str+":"+id);
            }
            return id;
        }
    }
}
//case 59/175: [0,0,0,0,null,null,0,null,null,null,0]
//裡面有一堆0, 原來我程式有寫錯 right=helper(root.right) 寫成 helper(root.left)
