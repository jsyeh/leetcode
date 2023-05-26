/*
// Definition for a Node.
class Node {
public:
    int val;
    vector<Node*> children;

    Node() {}

    Node(int _val) {
        val = _val;
    }

    Node(int _val, vector<Node*> _children) {
        val = _val;
        children = _children;
    }
};
*/

class Solution {
public:
    vector<vector<int>> levelOrder(Node* root) {
        vector<vector<int>> ans;
        levelOrder(root, 0, ans);
        return ans;
    }
    void levelOrder(Node* root, int level, vector<vector<int>>& ans) {
        if(root==nullptr) return;

        if(ans.size()<=level) {
            vector<int> temp;
            temp.push_back(root->val);
            ans.push_back(temp);
        } else {
            ans[level].push_back(root->val);
        }
        for(Node * child : root->children) {
            levelOrder(child, level+1, ans);
        }
    }
};
