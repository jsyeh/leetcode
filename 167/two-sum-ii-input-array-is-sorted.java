class Solution {
    public int[] twoSum(int[] numbers, int target) {
        //突然有靈感，就用map即可，但不能使用重覆的元素，所以不能用map
        //可用 binarySearch
        //2:38看到使用方法 https://docs.oracle.com/javase/7/docs/api/java/util/Arrays.html
        int [] ans = new int[2];
        for(int k=numbers.length-1; k>=0; k--){
            int prev = Arrays.binarySearch(numbers, 0, k, target - numbers[k]);
            if(prev>=0){
                ans[0] = prev+1;
                ans[1] = k+1;
                break;
            }
        }
        return ans;
    }//7:03還是寫錯，後來改用 binarySearch就成功了!
}
