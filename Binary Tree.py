#Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if not root or not p or not q:
            return None
        if p == root or q == root:
            return root
        stack = [root]
        node = root
        number = 0
        stackp = []
        stackq = []
        while(number<2):
            while(node and node.left):
                if node.left == p:
                    number += 1
                    stack.append(node.left)
                    stackp = stack[:]
                elif node.left == q:
                    number +=1
                    stack.append(node.left)
                    stackq = stack[:]
                else:
                    node = node.left
                    stack.append(node)
            node = stack.pop()
            if node.right:
                if node.right == p:
                    number += 1
                    stack.append(node.right)
                    stackp = stack[:]
                elif node.right == q:
                    number +=1
                    stack.append(node.right)
                    stackq = stack[:]
                else:
                    stackp.append(node.right)
            node = node.right

        for i in range(len(stackp)):
             print(stackp[i].val)
        print "x"
        for i in range(len(stackq)):
             print(stackq[i].val)

root = TreeNode(1)
node = TreeNode(2)
root.left = node
p = node
node = TreeNode(3)
root.right = node

newnode = TreeNode(4)
node.right = newnode
q = newnode
solution = Solution()
print(solution.lowestCommonAncestor(root,p,q))

