class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = [neighbors if neighbors is not None else]

def cloneGraph(node):
    if not node:
        return None
    
    def DFS(node,visited,clone):
        A = Node(node.val,[])
        clone.neighbors.append(A)
        visited[node] = A
        for n in node.neighbors:
            if n in visited:
                A.neighbors.append(visited[n])
            else:
                DFS(n,visited,A)

    clone = Node(0,[])
    visited = dict()
    DFS(node,visited,clone)
    return clone.neighbors[0]

if __name__ == "__main__":
    node = Node(1)
    node.neighbors = [Node(2),Node(3)]
    print(cloneGraph(node))