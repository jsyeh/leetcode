class Solution {
    public int numRescueBoats(int[] people, int limit) {
        //題目：每個船載2人，上限limit重量，求要幾個船
        //了解題目：2分20秒
        Arrays.sort(people);
        int N = people.length;
        //for(int i=N-1; i>=0; i--){ //可能可用 map 或 binarySearch()
        //但 search完後，要怎麼把數值移出 array呢？
        //6:51使用高斯法，是不是可行? 就最大配最小，依序做下去
        //    if(people[i])
        //}
        //8:40配對法 or Two Pointers 法
        int left=0, right=N-1, ans=0;
        while(left<=right) {
            if(left==right){
                ans++;
                break;
            } else if(people[left]+people[right]<=limit){
                ans++;
                left++;
                right--;
            } else {
                ans++;
                right--;
            }
        }
        return ans;
    }
}
