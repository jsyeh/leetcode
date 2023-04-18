class Solution {
public:
    vector<vector<int>> intervalIntersection(vector<vector<int>>& firstList, vector<vector<int>>& secondList) {
        vector<vector<int>> ans;
        int i=0, j=0;
        while(i<firstList.size() && j<secondList.size()){
            vector<int> list1 = firstList[i];
            vector<int> list2 = secondList[j];

            if(list1[1]<list2[0]) i++; //第一個太慢了
            else if(list2[1]<list1[0]) j++; //第二個太慢了
            else{ //有重疊
                int a[] = {list1[0], list1[1], list2[0], list2[1]};
                sort(a, a+4);
                vector<int> temp;
                temp.push_back(a[1]);
                temp.push_back(a[2]);
                ans.push_back(temp);
                if(list1[1]<list2[1]) i++;
                else j++;
            }
        }
        return ans;
    }
};
