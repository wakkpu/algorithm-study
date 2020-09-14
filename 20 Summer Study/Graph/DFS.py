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


def recursive_dfs(v, visited=[]):
    visited.append(v)
    for w in graph[v]:
        if w not in visited:
            visited = recursive_dfs(w, visited)
    return visited


def iterative_dfs(v):
    visited = []
    stack = [v]
    while stack:
        v = stack.pop()
        if v not in visited:
            visited.append(v)
            for w in graph[v]:
                stack.append(w)
    return visited


if __name__ == "__main__":

    print(recursive_dfs(1))
    print(iterative_dfs(1))
    print("왜 결과가 다를까?")
    print("=> iterative에서는 스택으로 구현했으므로 역순으로 접근")