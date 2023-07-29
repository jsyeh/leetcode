// LeetCode Problem 808. Soup Servings

//table[a][b] is the probility of prob(a,b)
double table[5000][5000] = {}; //global variable (default is 0)
// Many Discussions & Solutions said, the output is 1 if n > 4800
// After testing in Testcase, it is true. But 5000 looks beautiful

class Solution {
public:

    double soupServings(int n) {
        if(n>=5000) return 1;
        return prob(n, n); //Initially, Soap A is n, and Soap B is n
    }

    double prob(int a, int b){
    // The 3 termination conditions of the recursion
        if(a<=0 && b>0) return 1; // soup A empty first
        if(a<=0 && b<=0) return 0.5; // All empty (at the same time)
        if(b<=0 && a>0) return 0; // soup B empty first

    // Easy table-lookup if the prob(a,b) is calculated before
        if(table[a][b]!=0) return table[a][b];

    // Only 4 kinds of operations, reduce the soup by 100,75,50,25
        double type1 = prob(a-100, b);
        double type2 = prob(a-75, b-25);
        double type3 = prob(a-50, b-50);
        double type4 = prob(a-25, b-75);

    // The 4 kinds of operations with equal probability (0.25)
    // Backup the value in table[a][b] for future table-lookup
        table[a][b] = 0.25 * (type1 + type2 + type3 + type4);
        return table[a][b]; 
    }
};

