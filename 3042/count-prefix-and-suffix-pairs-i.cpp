// LeetCode 3042. Count Prefix and Suffix Pairs I
// 左邊 words[i] 是不是 右邊 words[j] 的prefix兼postfix (剛好是字首、也是字尾)
class Solution {
public:
    int countPrefixSuffixPairs(vector<string>& words) {
        int ans = 0, N = words.size();
        for(int i=0; i<N; i++) { // 左邊 words[i]
            for(int j=i+1; j<N; j++) { // 右邊 words[j]
                int L1 = words[i].length(), L2 = words[j].length(), d = L2-L1; // 兩字串的長度
                if(L1 > L2) continue; // 長度不對, 換下一組 (需要左邊較短、右邊較長)
                int bad = 0; // 我想試試「一個個字母」慢慢比較
                for(int k=0; k<L1; k++) { // 針對 words[i] 的每個字母, 都去比較
                    if(words[i][k] != words[j][k] || words[i][k] != words[j][d+k]){
                        bad = 1;
                        break;
                    }
                }
                if(bad==0) ans++;
            }
        }
        return ans;
    }
};
