class Solution {
public:
    double average(vector<int>& salary) {
       int max = salary[0];
       int min = salary[0];
       double sum = 0;
       for(int one : salary) {
           if(one>max) max = one;
           if(one<min) min = one;
           sum += one;
       }
       return (sum-max-min)/(salary.size()-2);
    }
};
//case 20/43: [48000,59000,99000,13000,78000,45000,31000,17000,39000,37000,93000,77000,33000,28000,4000,54000,67000,6000,1000,11000]
//小心 int float/double 的問題
