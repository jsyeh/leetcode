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
    HashMap<Long,Integer>map = new HashMap<>();
    Stack<Long> stack = new Stack<>(); //prefix sum
    int ans = 0;

    public int pathSum(TreeNode root, int targetSum) {
        //buildPrefixSum(root, 0);
        travel(root, targetSum, 0);
        return ans;
    }
    void travel(TreeNode root, long targetSum, long sum) {
        if(root==null) return;
        long now = sum + root.val;
        stack.push(now);

        if(now==targetSum) ans++;
        long diff = now-targetSum;
        if(map.containsKey(diff)){
            ans += map.get(diff);
        }
        if(map.containsKey(now)){
            map.put(now, map.get(now)+1);
        }else map.put(now, 1); //加

        travel(root.left, targetSum, now);
        travel(root.right, targetSum, now);
        map.put(now, map.get(now)-1);//減

        stack.pop();
    }
/*    void buildPrefixSum(TreeNode root, int sum) {
        if(root==null) return;
        root.val += sum; //糟! int 不夠裝 20億，要改用long 吧! 要換資料結栟
        if(root.left!=null) buildPrefixSum(root.left, root.val);
        if(root.right!=null) buildPrefixSum(root.right, root.val);
    }*/
}//case 127/128: [1000000000,1000000000,null,294967296,null,1000000000,null,1000000000,null,1000000000] 0
