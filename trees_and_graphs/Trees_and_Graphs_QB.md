# Trees and Graphs – Real-Life DSA Questions with Answers (Python)

## 🌳 Trees (Questions + Answers)

### 1. File System Explorer

**Question:** Design a system to represent folders and files and print all file paths.

```python
class Node:
    def __init__(self, name):
        self.name = name
        self.children = []

def print_paths(node, path=""):
    path += "/" + node.name
    if not node.children:
        print(path)
    for child in node.children:
        print_paths(child, path)
```

### 2. Company Organizational Chart

**Question:** Find all employees under a manager.

```python
class Employee:
    def __init__(self, name):
        self.name = name
        self.subordinates = []

def get_all(emp):
    result = [emp.name]
    for sub in emp.subordinates:
        result.extend(get_all(sub))
    return result
```

### 3. Expression Evaluation

**Question:** Evaluate an expression tree.

```python
def evaluate(root):
    if not root.left and not root.right:
        return int(root.data)
    l = evaluate(root.left)
    r = evaluate(root.right)
    return eval(f"{l}{root.data}{r}")
```

### 4. Search in BST

**Question:** Search product by price.

```python
def search(root, key):
    if not root or root.data == key:
        return root
    if key < root.data:
        return search(root.left, key)
    return search(root.right, key)
```

### 5. Minimum in BST

**Question:** Find lowest price.

```python
def find_min(root):
    while root.left:
        root = root.left
    return root.data
```

### 6. DOM Traversal

**Question:** Extract elements of type.

```python
def find_tag(node, tag):
    result = []
    if node.name == tag:
        result.append(node)
    for child in node.children:
        result.extend(find_tag(child, tag))
    return result
```

### 7. Family Tree

**Question:** Find descendants.

```python
def descendants(node):
    result = []
    for child in node.children:
        result.append(child.name)
        result.extend(descendants(child))
    return result
```

### 8. Folder Size

**Question:** Calculate total size.

```python
def total_size(node):
    if not node.children:
        return node.size
    return sum(total_size(c) for c in node.children)
```

### 9. Level Order Traversal

**Question:** Print level-wise.

```python
from collections import deque

def level_order(root):
    q = deque([root])
    while q:
        node = q.popleft()
        print(node.data)
        if node.left: q.append(node.left)
        if node.right: q.append(node.right)
```

### 10. Decision Tree

**Question:** Simulate decision making.

```python
def decide(node, value):
    if not node.left and not node.right:
        return node.data
    if value < node.data:
        return decide(node.left, value)
    return decide(node.right, value)
```

---

## 🌐 Graphs (Questions + Answers)

### 1. Social Network

**Question:** Find friends.

```python
def friends(graph, user):
    return graph.get(user, [])
```

### 2. Shortest Path

**Question:** Find shortest route.

```python
from collections import deque

def shortest_path(graph, start, end):
    q = deque([(start, [start])])
    visited = set()
    while q:
        node, path = q.popleft()
        if node == end:
            return path
        for n in graph[node]:
            if n not in visited:
                visited.add(n)
                q.append((n, path + [n]))
```

### 3. Cycle Detection

**Question:** Detect loop.

```python
def has_cycle(graph, node, visited, parent):
    visited.add(node)
    for n in graph[node]:
        if n not in visited:
            if has_cycle(graph, n, visited, node):
                return True
        elif parent != n:
            return True
    return False
```

### 4. Web Crawler

**Question:** Visit all pages.

```python
def dfs(graph, node, visited=set()):
    visited.add(node)
    print(node)
    for n in graph[node]:
        if n not in visited:
            dfs(graph, n, visited)
```

### 5. Movie Recommendation

**Question:** Recommend via connections.

```python
def recommend(graph, user):
    rec = set()
    for f in graph[user]:
        rec.update(graph[f])
    rec.discard(user)
    return rec
```

### 6. Flight Route

**Question:** Check route exists.

```python
def route_exists(graph, start, end, visited=set()):
    if start == end:
        return True
    visited.add(start)
    for n in graph[start]:
        if n not in visited:
            if route_exists(graph, n, end, visited):
                return True
    return False
```

### 7. Friend Suggestions

**Question:** Suggest mutual friends.

```python
def suggestions(graph, user):
    sug = set()
    for f in graph[user]:
        sug.update(graph[f])
    return sug - set(graph[user]) - {user}
```

### 8. Network Connectivity

**Question:** Check connected.

```python
def is_connected(graph, start):
    visited = set()
    dfs(graph, start, visited)
    return len(visited) == len(graph)
```

### 9. Task Scheduling

**Question:** Find execution order.

```python
def topo_sort(graph):
    visited, stack = set(), []
    def dfs(v):
        visited.add(v)
        for n in graph[v]:
            if n not in visited:
                dfs(n)
        stack.append(v)
    for v in graph:
        if v not in visited:
            dfs(v)
    return stack[::-1]
```

### 10. Isolated Nodes

**Question:** Find nodes with no edges.

```python
def isolated(graph):
    return [n for n in graph if not graph[n]]
```
