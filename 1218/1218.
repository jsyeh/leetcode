//想法：邊巡邊比對，如果有個 HashMap<Integer,Integer> map 
// 可在 map.containsKey(arr[i]-diff) 就更新它，同時看 map.containsKey(arri])值是否更大
class Solution {
    HashMap<Integer,Integer> map = new HashMap<>(); //之前出現的值，對應最長的等差級數
    public int longestSubsequence(int[] arr, int diff) {
        int ans = 0;
        for(int i=0; i<arr.length; i++){
            int len = 1;
            if(map.containsKey(arr[i]) && map.get(arr[i])>len) {
                len = map.get(arr[i]);
            }
            if(map.containsKey(arr[i]-diff) && map.get(arr[i]-diff)+1>len) {
                len = map.get(arr[i]-diff)+1;
            }
            map.put(arr[i], len);
            if(len>ans) ans = len;
        }
        return ans;
    }
}
