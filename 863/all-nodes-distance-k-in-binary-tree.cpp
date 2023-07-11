/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
//想法：往下的做法很簡單，就downK(root, k)
//但是往上比較麻煩，需要有個 path 才知道要怎麼往下走，就用函式呼叫函式。
//因為 return value 麻煩，用 C++/Java 實作
class Solution {
public:
    vector<int> ans;
    //可以先用 stack (function呼叫),找到 target 的距離
    vector<int> distanceK(TreeNode* root, TreeNode* target, int k) {
        if(root==nullptr) return ans; //遇到空字串時，就結束（但題目至少有1點）
        targetDistance(root, target, k);
        return ans;
    }

    int targetDistance(TreeNode* root, TreeNode* target, int k) {
        //if(k<0) return -1; 
        if(root==nullptr) return -1; //-1表示沒有target
        if(root==target) {
            downK(root, k);
            return 0; //0表示與 target 距離 0
        }
        int left = targetDistance(root->left, target, k);
        int right = targetDistance(root->right, target, k);
//printf("root->val:%d\n", root->val);
//printf("left:%d right:%d\n", left, right);
        //我沒有照顧到root (只有照顧到k=1的root) 所以要改程式
        //if((left==0||right==0)&&k==1){ //小孩剛好是target,那就要加本身
        if(k!=0 && (left==k-1 || right==k-1)){ //剛好 root 本身就是上行k-th節點
        //小心k=0的狀況
            ans.push_back(root->val);
            return -1; //有把本身加進去，那就不用再算了
        }
        if(left!=-1){ //left裡面有
            downK(root->right, k-2-left); //換另一邊真的探索
            return left+1;
        } 
        if(right!=-1){ //right裡面有
            downK(root->left, k-2-right); //換另一邊真的探索
            return right+1;//這裡之前寫錯成left+1所以有bug
        }

        return -1;
    }

    void downK(TreeNode* root, int k) { //很明確的，要把距離k的點都加入ans
        if(root==nullptr) return; //空node, return
        if(k<0) return; //不合理，return

        if(k==0) {
            ans.push_back(root->val);
            return;
        }
        //以下是k>0 要繼續 downK()
        downK(root->left, k-1);
        downK(root->right, k-1);
    }
};
//case 39/57: [0,null,1,null,2,null,3,4]
//2
//2 我沒有照顧到root (只有照顧到k=1的root) 所以要改程式
