def networkDelayTime(times, N, K):

    import collections
    import heapq

    g = collections.defaultdict(list)

    for u, v, w in times:
        g[u].append((v, w))

    visited = set()
    distance = {i: float('inf') for i in range(1, N+1)}
    distance[K] = 0
    min_heap = [(0, K)]

    while min_heap:
        cost, node = heapq.heappop(min_heap)
        visited.add(node)

        if len(visited) == N:
            return cost

        for node2, cost2 in g[node]:
            if node2 in visited:
                continue
            if distance[node2] > cost + cost2:
                distance[node2] = cost + cost2
                heapq.heappush(min_heap, (cost + cost2, node2))
    return -1


if __name__ == "__main__":

    times = [[2, 1, 1],
             [2, 3, 1],
             [3, 4, 1]]
    N = 4
    K = 2

    print(networkDelayTime(times, N, K))
