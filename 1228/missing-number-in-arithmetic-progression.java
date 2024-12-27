// LeetCode 1228. Missing Number In Arithmetic Progression
// 找到「等差級數」中，缺的那個數
class Solution {
    public int missingNumber(int[] arr) {
        int diff = arr[1] - arr[0], diff2 = arr[2] - arr[1];
        if(Math.abs(diff)<Math.abs(diff2)) return arr[1] + diff;
        if(Math.abs(diff2)<Math.abs(diff)) return arr[0] + diff2;
        for(int i=2; i<arr.length; i++) {
            if(arr[i] - arr[i-1] != diff) return arr[i-1] + diff;
        }
        return arr[arr.length-1] + diff;
    }
}
