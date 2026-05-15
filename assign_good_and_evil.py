from dsc40graph import UndirectedGraph

def assign_good_and_evil(graph):
    labels = {}

    def dfs(node, label):
        # If already labeled, check consistency
        if node in labels:
            return labels[node] == label

        labels[node] = label

        opposite = 'evil' if label == 'good' else 'good'

        for neighbor in graph.neighbors(node):
            if not dfs(neighbor, opposite):
                return False

        return True

    for node in graph.nodes:
        if node not in labels:
            if not dfs(node, 'good'):
                return None

    return labels