from collections import deque
# DFS:
# PreOrder: Node, Left, Right. Can be done both recursive, and iterative, using STACK.
# PostOrder: Left, Right, Node. Can be done both recursive, and iterative, using STACK.
# inOrder: Left, Node, Right. Can be done both recursive, and iterative, using STACK. Gives sort ordering.

# All above require stack space proportional to the height of the tree (which is log(N), which is a call stack
# for the recursive and a parent stack for the iterative ones.

# BFS:
# Level Order:, BFS. Iterative using Queue, space complexity is maximum nodes at a given level, as much as N/2, where N is total # of nodes in tree.
# Recursive for level order is hard.

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    #Iterative solution, using STACK to perform InOrder Traversal
    #visit each node in INCREASING order of a BST: depth-first left, root, right...)
    def inOrderIterative(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        stack = []
        allNodes = []
        if not root:
            return []
        while (root or stack):
            if root:
                stack.append(root)
                root = root.left
            else:
                root = stack.pop()
                allNodes.append(root.val)
                root = root.right
        return allNodes

    def inOrderRecursive(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root:
            return self.inOrderRecursive(root.left) + [root.val] + self.inOrderRecursive(root.right)
        else:
            return []

    def preOrderRecursive(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root:
            return [root.val] + self.preOrderRecursive(root.left) + self.preOrderRecursive(root.right)
        else:
            return []

    def preOrderIterative(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        allNodes = []
        if not root:
            return []
        stack=[root]
        while stack:
            root = stack.pop()
            if root:
                allNodes.append(root.val)
                stack.append(root.right)
                stack.append(root.left)

        return allNodes

def LevelOrderIterative(self, root):
    """
    :type root: TreeNode
    :rtype: bool
    """
    allNodes = []
    queue = deque()
    if not root:
        return allNodes
    queue.append(root)
    if queue:
        levelNodes = []
        curr = queue.popleft()
        levelNodes.append(curr.val)
        if root.left:
            queue.append(root.left)
        if root.right:
            queue.append(root.right)

def InOrderMorrisTraversal(self, root):
    #O(1) space, but connecting the right subtree of each 'ready to be traversed' node to its inorder successor, then erasing that link
    prev, curr, res = None, root, []
    while curr:
        if not curr.left:
            #This is a simple leaf node, ready to be traversed.
            res.append(root.val)
            curr = curr.right
        else:
            prev = curr.left
            while prev.right and prev.right!=curr: #Not previously 'threaded':
                prev = prev.right
            if not prev.right:
                prev.right = curr #Thread a leaf node to its next in order successor.
                curr = curr.left
            else:
                prev.right = None #Erase a previously threaded link, as this node is now ready to be traversed
                res.append(prev.node)
                curr = curr.right
    return res
