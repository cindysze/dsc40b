def cluster(graph, weights, level):
    visited = set()
    clusters = []

    for node in graph.nodes():
        if node not in visited:

            component = set()
            stack = [node]

            while stack:
                curr = stack.pop()

                if curr not in visited:
                    visited.add(curr)
                    component.add(curr)

                    for neighbor in graph.neighbors(curr):

                        # only keep strong enough edges
                        if weights(curr, neighbor) >= level:
                            if neighbor not in visited:
                                stack.append(neighbor)

            clusters.append(frozenset(component))

    return frozenset(clusters)