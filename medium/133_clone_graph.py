class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


def cloneGraph(node):
    clones = {}

    def dfs(node):
        if node is None:
            return node
        
        if node in clones:
            return clones[node]

        clone = Node(node.val)
        clones[node] = clone

        for neighbor in node.neighbors:
            clone.neighbors.append(dfs(neighbor))

        return clone
        
    return dfs(node)


def build_graph(adj_list):
    if not adj_list:
        return None

    nodes = [Node(i + 1) for i in range(len(adj_list))]

    for i, neighbors in enumerate(adj_list):
        for neighbor_val in neighbors:
            nodes[i].neighbors.append(nodes[neighbor_val - 1])

    return nodes[0]


def graph_to_adj_list(node):
    if node is None:
        return []

    seen = {}
    stack = [node]

    while stack:
        cur = stack.pop()

        if cur.val in seen:
            continue

        seen[cur.val] = sorted(n.val for n in cur.neighbors)

        for neighbor in cur.neighbors:
            if neighbor.val not in seen:
                stack.append(neighbor)

    return [seen[i] for i in sorted(seen)]


def same_objects(original, clone):
    if original is None and clone is None:
        return True

    if original is clone:
        return False

    original_nodes = {}
    clone_nodes = {}

    stack = [original]
    while stack:
        node = stack.pop()

        if node.val in original_nodes:
            continue

        original_nodes[node.val] = node
        stack.extend(node.neighbors)

    stack = [clone]
    while stack:
        node = stack.pop()

        if node.val in clone_nodes:
            continue

        clone_nodes[node.val] = node
        stack.extend(node.neighbors)

    for val in original_nodes:
        if original_nodes[val] is clone_nodes[val]:
            return False

    return True


tests = [
    (
        [[2, 4], [1, 3], [2, 4], [1, 3]],
        [[2, 4], [1, 3], [2, 4], [1, 3]]
    ),

    (
        [[]],
        [[]]
    ),

    (
        [],
        []
    ),

    (
        [[2], [1]],
        [[2], [1]]
    ),

    (
        [[2, 3], [1, 3], [1, 2]],
        [[2, 3], [1, 3], [1, 2]]
    ),

    (
        [[2], [1, 3], [2, 4], [3]],
        [[2], [1, 3], [2, 4], [3]]
    ),
]


for adj_list, expected in tests:
    original = build_graph(adj_list)
    cloned = cloneGraph(original)

    result = graph_to_adj_list(cloned)

    print("input:", adj_list)
    print("result:", result)
    print("expected:", expected)
    print("structure correct:", result == expected)
    print("deep copy:", same_objects(original, cloned))
    print()