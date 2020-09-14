global graph
graph = {
        1: [2, 3, 4],
        2: [5],
        3: [5],
        4: [],
        5: [6, 7],
        6: [],
        7: [3]
}


def iterative_bfs(v):
    visited = [v]
    queue = [v]
    while queue:
        v = queue.pop(0)
        for w in graph[v]:
            if w not in visited:
                visited.append(w)
                queue.append(w)
    return visited


if __name__ == "__main__":

    print(iterative_bfs(1))
