/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
    vector<string> binaryTreePaths(TreeNode* root) {
        vector<string> res;
        if(root==nullptr)return res;
        queue<TreeNode*> q;
        queue<string> path_q;
        q.push(root);
        path_q.push(to_string(root->val));
        if(root==nullptr) return res;
        while(q.size()!=0)
        {
            auto node = q.front();
            auto path = path_q.front(); 
            q.pop();
            path_q.pop();
            if(node->left==nullptr && node->right==nullptr)
            {
                res.push_back(path);
            }
            if(node->left!=nullptr)
            {
                q.push(node->left);
                path_q.push(path+"->"+to_string(node->left->val));
            }
            if(node->right!=nullptr)
            {
                q.push(node->right);
                path_q.push(path+"->"+to_string(node->right->val));
            }    
        }
        return res;
    }
};
