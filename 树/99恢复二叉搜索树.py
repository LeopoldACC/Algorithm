# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        inorder = []
        def get_inorder(node):
            if not node:
                return
            get_inorder(node.left)
            inorder.append(node)
            get_inorder(node.right)
        get_inorder(root)

        first,second,pre = None,None,TreeNode(-float('inf'))
        #因为是二叉搜索树 中序遍历出来是单调递增的 所以我们只需要找2个不满足比前一个大的结点
        #4 2 3 1
        #第一个异常点是pre 4 第二个异常点是cur 1
        #1 5 3 4 2
        #第一个异常点是pre 5 第二个异常点是cur 2
        #first存第一个不满足的点 second存第二个不满足的点
        for i in range(len(inorder)):
            #如果没有出现过异常点，并且前一个结点比当前节点大 4 2 first=pre=4
            if not first and pre.val>inorder[i].val:
                first = pre
            #如果已经有一个异常点，并且前一个结点比当前节点大 3 1 second=cur=1
            if first and pre.val>inorder[i].val:
                second = inorder[i]
            #pre更新为当前结点作为下一个点的 前继结点
            pre = inorder[i]
        first.val,second.val = second.val,first.val

# # C++
# /**
#  * Definition for a binary tree node.
#  * struct TreeNode {
#  *     int val;
#  *     TreeNode *left;
#  *     TreeNode *right;
#  *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
#  *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
#  *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
#  * };
#  */
# class Solution {
# public:
#     void recoverTree(TreeNode* root) {
#         vector<TreeNode*> inorder;
#         get_inorder(root,inorder);
#         TreeNode* pre=nullptr;
#         TreeNode* first = nullptr;
#         TreeNode* second = nullptr;
#         for(int i=0;i<inorder.size();i++)
#         {
#             if(pre!=nullptr && first==nullptr && pre->val>inorder[i]->val) first = pre;
#             if(first!=nullptr && pre->val>inorder[i]->val) second = inorder[i];
#             pre = inorder[i];
#         }
#         int tmp = first->val;
#         first->val = second->val;
#         second->val = tmp;
#     }
#     void get_inorder(TreeNode* root,vector<TreeNode*>& inorder)
#     {
#         if(root==nullptr) return;
#         get_inorder(root->left,inorder);
#         inorder.push_back(root);
#         get_inorder(root->right,inorder);
#     }
# };