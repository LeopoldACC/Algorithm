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
    vector<string> res;
    vector<string> binaryTreePaths(TreeNode* root) {
        if(root==nullptr) return res;
        dfs(root,{root});
        return res;
    }
    void dfs(TreeNode* root,vector<TreeNode*> path)
    {
        if(root->left==nullptr && root->right==nullptr)
        {
            string tmp;
            tmp+=to_string(path[0]->val);
            if(path.size()==1)
            {
                res.push_back(tmp);
                return ;
            }
            for(int i=1;i<path.size();i++)
            {
                tmp+="->";
                tmp+=to_string(path[i]->val);
            }
            res.push_back(tmp);
        }
        if(root->left!=nullptr)
        {
            path.push_back(root->left);
            dfs(root->left,path);
            path.pop_back();
        }
        if(root->right!=nullptr)
        {
            path.push_back(root->right);
            dfs(root->right,path);
        }
    }
};
