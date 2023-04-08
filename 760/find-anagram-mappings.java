class Solution {
    public int[] anagramMappings(int[] nums2, int[] nums1) {
        //09:18發現寫反了，所以直接改上面的函式參數，就成功了
        //01:36
        //HashMap<Integer,Integer> map = new HashMap<Integer,Integer>();
        //map.put(key, val) key是 nums1裡的值，val是index
        //但是問題在duplicate,也就是key會重覆
        //解決方法，就改成 Integer to ArrayList<Integer>
        //03:26
        HashMap<Integer, Stack<Integer>> map = new HashMap<Integer, Stack<Integer>>();
        for(int i=0; i<nums1.length; i++){
            if(!map.containsKey(nums1[i])) {
                Stack<Integer> index = new Stack<Integer>();
                index.add(i);
                map.put(nums1[i], index);
            }else{
                Stack<Integer> index = map.get(nums1[i]);
                index.add(i);
            }
        }

        int [] ans = new int[nums1.length];
        for(int i=0; i<nums2.length; i++){
            Stack<Integer> index = map.get(nums2[i]);
            ans[i] = index.pop();
        }//07:35寫完，但答案不對
        return ans;
    }
}
