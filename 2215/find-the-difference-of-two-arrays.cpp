class Solution {
public:
    vector<vector<int>> findDifference(vector<int>& nums1, vector<int>& nums2) {
        vector<vector<int>> ans; //用來放答案的陣列

        sort(nums1.begin(), nums1.end()); //排序後，裡面可能會有重覆出現的數字相鄰
        sort(nums2.begin(), nums2.end()); //排序後，裡面可能會有重覆出現的數字相鄰

        int len1 = 1; //nums1[0]一定是要留下來的，所以len1從1開始
        for(int i=1; i<nums1.size(); i++){ //想去除重覆出現的數字
            if(nums1[i]!=nums1[i-1]) nums1[len1++] = nums1[i]; //不重覆時，才往前攞放
        }
        nums1.resize(len1);//把後面沒用到的格子刪掉

        int len2 = 1; //nums2[0]一定是要留下來的，所以len2從1開始
        for(int i=1; i<nums2.size(); i++){ //想去除重覆出現的數字
            if(nums2[i]!=nums2[i-1]) nums2[len2++] = nums2[i]; //不重覆時，才往前攞放
        }
        nums2.resize(len2);//把後面沒用到的格子刪掉

        vector<int> list1; //用來放 nums1[i] 裡獨特的數
        vector<int> list2; //用來放 nums2[i] 裡獨特的數
        
        int i1=0, i2=0;
        while(i1<nums1.size() && i2<nums2.size()) {
            if(nums1[i1]==nums2[i2]){ //太好了，兩邊都有，可以跳過
                i1++; //因為有重覆的可能，所以不能只是i++
                i2++;
            } else if(nums1[i1]<nums2[i2]) {
                //如果nums1[i1]比較小，那要加油趕上，而且nums1[i1]應是獨特的
                list1.push_back(nums1[i1]); //就把 nums1[i1] 放到 list1 裡
                i1++;
            } else if(nums2[i2]<nums1[i1]) {
                //如果nums2[i2]比較小，那要加油趕上，而且nums2[i2]應是獨特的
                list2.push_back(nums2[i2]); //就把 nums2[i2] 放到 list2 裡
                i2++;
            }
        }
        if(i1==nums1.size()){ //如果i1用到底了，那可能i2還有剩下來，把剩下來的都放到list2裡
            for(int i=i2; i<len2; i++) list2.push_back(nums2[i]);
        }else if(i2==nums2.size()) { //如果i2用到底了，那可能i1還有剩下來，把剩下來的都放到list1裡
            for(int i=i1; i<len1; i++) list1.push_back(nums1[i]);
        }
        
        ans.push_back(list1); //擺好 list1 到 ans 裡
        ans.push_back(list2); //擺好 list2 到 ans 裡

        return ans;
    }
};
