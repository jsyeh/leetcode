// LeetCode 3263. Convert Doubly Linked List to Array I
// 把 Doubly Linked List 變成陣列
class Solution {
public:
	vector<int> toArray(Node *head){
        vector<int> ans;
        while(head != nullptr) {
            ans.push_back(head->val);
            head = head->next;
        }
        return ans;
    }
};
/**
 * Definition for doubly-linked list.
 * class Node {
 *     int val;
 *     Node* prev;
 *     Node* next;
 *     Node() : val(0), next(nullptr), prev(nullptr) {}
 *     Node(int x) : val(x), next(nullptr), prev(nullptr) {}
 *     Node(int x, Node *prev, Node *next) : val(x), next(next), prev(prev) {}
 * };
 */

