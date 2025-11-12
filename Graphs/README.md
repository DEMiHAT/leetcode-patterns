
# 🕸️ Graphs: Network Topology & Connectivity

> **System Level:** Modeling non-linear relationships, shortest-path routing, and cycle detection in complex networks.

---

## 🧠 The Engineering Context

Graphs are the backbone of modern system architecture. Whether it's **dependency resolution** (npm/pip), **social networks** (LinkedIn 2nd connections), or **routing algorithms** (Google Maps), graphs model entities ($V$) and their relationships ($E$).

**Key Engineering Challenges:**
* **Traversal Strategy:** Choosing between Breadth-First (Layer-wise) and Depth-First (Recursive) based on the objective.
* **Cycle Detection:** Preventing infinite loops in directed dependencies (Deadlocks).
* **Connectivity:** Determining if disparate system components can communicate (Union-Find).

---

## 📟 Data Representation Strategies

How we store the graph dictates the Time/Space complexity of the algorithm.

| Representation | Space | Edge Lookup | Use Case |
| :--- | :--- | :--- | :--- |
| **Adjacency List** | $O(V + E)$ | $O(K)$ | **Most Common.** Sparse graphs (Social networks, Web). |
| **Adjacency Matrix** | $O(V^2)$ | $O(1)$ | Dense graphs. Checking specific connection instantly. |
| **Edge List** | $O(E)$ | $O(E)$ | Kruskal's Algorithm (MST). |

**The Standard: Adjacency List (HashMap)**
```text
Graph: {
  "A": ["B", "C"],
  "B": ["D"],
  "C": ["D"],
  "D": []
}
````

-----

## 🛠️ Core Algorithmic Paradigms

### 1\. Breadth-First Search (BFS) - "The Ripple"

**Use Case:** Shortest Path in Unweighted Graphs, Level-order traversal.

  * **Data Structure:** Queue (FIFO).
  * **Logic:** Explore neighbors, then neighbors of neighbors. Guarantees the shortest path in terms of "hops."

### 2\. Depth-First Search (DFS) - "The Maze Runner"

**Use Case:** Cycle Detection, Path Existence, Topological Sort.

  * **Data Structure:** Stack (LIFO) or Recursion.
  * **Logic:** Go as deep as possible, hit a wall, backtrack. Essential for solving maze/puzzle problems.

### 3\. Union-Find (Disjoint Set Union)

**Use Case:** Dynamic Connectivity, Minimum Spanning Tree.

  * **Logic:** Near-constant time ($O(\alpha(N))$) operations to `union()` two sets and `find()` if two nodes share a root parent.
  * **Optimization:** Path Compression + Union by Rank.

### 4\. Topological Sort (DAGs)

**Use Case:** Build systems, Course Scheduling, Task resolution.

  * **Logic:** Linear ordering of vertices such that for every edge $u \to v$, vertex $u$ comes before $v$. (Kahn's Algorithm).

-----

## 📉 Shortest Path Compendium

When distance matters, standard BFS fails.

| Algorithm | Constraints | Complexity | Application |
| :--- | :--- | :--- | :--- |
| **BFS** | Unweighted edges | $O(V+E)$ | Peer-to-peer hop count. |
| **Dijkstra** | Non-negative weights | $O(E \log V)$ | GPS Routing. Standard priority queue approach. |
| **Bellman-Ford** | Negative weights allowed | $O(VE)$ | Forex arbitrage detection. |
| \**A* (A-Star)\*\* | Heuristic based | $O(E)$ (avg) | Video game pathfinding. |

-----

## 💻 Universal BFS Blueprint

This template solves 80% of "Shortest Path" or "Level Order" problems.

```python
from collections import deque

def bfs_generic(graph, start_node):
    queue = deque([start_node])
    visited = set([start_node])
    level = 0
    
    while queue:
        # Process level by level
        for _ in range(len(queue)):
            node = queue.popleft()
            
            # 1. PROCESS NODE (e.g., check if target)
            if node == TARGET: return level
            
            # 2. EXPAND NEIGHBORS
            for neighbor in graph[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
        
        level += 1
    return -1
```

-----

## ⚡ Optimization & Safety Checklist

  - [ ] **Disconnected Graphs:** Did you loop through *all* nodes `0 to N` to handle isolated components? (e.g., `for i in range(n): if i not in visited: dfs(i)`).
  - [ ] **Bidirectional Edges:** In undirected graphs, ensure you add the edge `u -> v` AND `v -> u`.
  - [ ] **Cycle Prevention:** ALWAYS use a `visited` set. Infinite loops in graphs cause Stack Overflow instantly.
  - [ ] **Matrix as Graph:** Remember that a 2D Grid (`grid[r][c]`) is implicitly a graph where neighbors are `(r+1, c), (r-1, c)...`.

<!-- end list -->

```
```
