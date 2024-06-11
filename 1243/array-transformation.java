// 有個產生(隔一天) array 的規則:
// 1. 如果左右都比你大, 你要++
// 2. 如果左右都比你小, 你要--
// 3. 頭、尾永不變動
class Solution {
    public List<Integer> transformArray(int[] arr) {
        Integer[] arr2 = new Integer[arr.length];
        arr2[0] = arr[0];
        arr2[arr.length-1] = arr[arr.length-1];
        int same = 0;
        while(same != arr.length-2) { // 如果
            same = 0; //數一數, 有幾個相同的數
            for(int i=1; i<arr.length-1; i++) {
                if(arr[i]<arr[i-1] && arr[i]<arr[i+1]) {
                    arr2[i] = arr[i] + 1;
                } else if(arr[i]>arr[i-1] && arr[i]>arr[i+1]) {
                    arr2[i] = arr[i] - 1;
                } else {
                    arr2[i] = arr[i];
                    same++;
                }
            }
            for(int i=0; i<arr.length; i++) arr[i] = arr2[i];
        }
        return Arrays.asList(arr2);
    }
}
