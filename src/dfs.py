graph = {
    1: [2, 3],
    2: [2, 3, 4],
    3: [3],
    4: [3, 2, 5],
    5: [1]
}

class DFS():
    def __init__(self, graph):
        self.graph = graph
        self.visited = set()

    def is_visited(self, node):
        for entry in self.visited:
            if node == entry: return True
        return False

    def dfs(self, start, end):
        if self.is_visited(start): return False
        self.visited.add(start)
        if start == end: return True
        for node in self.graph[start]:
            if self.dfs(node, end): return True
        return False
    
AD = DFS(graph)
print(AD.dfs(1, 5))