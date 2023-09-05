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
    Node* cloneTree(Node* root) {
        if(root==nullptr) return nullptr;
        
        Node* ans = new Node(root->val);
        vector<Node*> children;
        for(Node* child : root->children){
            children.push_back(cloneTree(child));
        }
        ans->children = children;
        return ans;
    }
};
//case 2/38: []
