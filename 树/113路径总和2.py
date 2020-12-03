class Solution:
    def pathSum(self, root: TreeNode, target: int) -> List[List[int]]:
        res = []
        def dfs(root,sums,path):
            if not root:
                return 
            if not root.left and not root.right and root.val+sums==target:
                res.append(path+[root.val])
                return 
            dfs(root.left,sums+root.val,path+[root.val])
            dfs(root.right,sums+root.val,path+[root.val])
        dfs(root,0,[])
        return res