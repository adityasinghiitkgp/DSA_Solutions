
def solve(d,node):
    if not node:
        return
    if node.val in d:
        return d[node.val]
    root=Node(node.val)
    if node.val not in d:
        d[node.val]=root
    for i in node.neighbors:
        root.neighbors.append(solve(d,i))
    return root
class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        d={}
        return solve(d,node)