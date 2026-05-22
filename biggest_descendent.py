def biggest_descendent(graph, root, value):
    result = {}

    def dfs(node):
        biggest = value[node]

        for neighbor in graph.neighbors(node):
            child_biggest = dfs(neighbor)
            biggest = max(biggest, child_biggest)

        result[node] = biggest
        return biggest

    dfs(root)
    return result
