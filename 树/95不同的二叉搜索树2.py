class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        if n==0:
            return []
        def buildTrees(left,right):
            trees = []
            if left>right:
                return [None]
            for i in range(left,right+1):#对left->right进行遍历分别作为根节点建树
                left_trees = buildTrees(left,i-1)#二叉搜索树 所以左子树是由比i小的所有数构成的树的集合
                right_trees = buildTrees(i+1,right)#二叉搜索树 所以右子树是由比i大的所有数构成的树的集合
                
                for l in left_trees:#left_trees中1->i-1为根的子树都可以作为i的左子树
                    for r in right_trees:#right_trees中i+1->end 为根的子树都可以作为i的右子树
                        cur_root = TreeNode(i)#以i为根创建一颗新树
                        cur_root.left = l
                        cur_root.right = r
                        trees.append(cur_root)
            return trees
        return buildTrees(1,n)


struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
}
 
class Solution {
public:
    vector<TreeNode*> generateTrees(int n) {
        if(n==0) return {};
        return buildTree(1,n);
    }
    vector<TreeNode*> buildTree(int left,int right)
    {
        vector<TreeNode*> trees;
        if(left>right) return {nullptr};
        for(int i=left;i<=right;i++)
        {
            vector<TreeNode*> left_trees = buildTree(left,i-1);
            vector<TreeNode*> right_trees = buildTree(i+1,right);
            for(auto l:left_trees)
            {
                for(auto r:right_trees)
                {
                    TreeNode* cur_root = new TreeNode(i);
                    cur_root->left = l;
                    cur_root->right = r;
                    trees.push_back(cur_root);
                }
            }
        }
        return trees;
    }
};