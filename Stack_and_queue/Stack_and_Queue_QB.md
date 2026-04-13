# Stack and Queue - Real Life Problem Based DSA (Python with Solutions)

## Instructions

* Real-world applications
* Optimized solutions
* Mentioned complexity

---

## Stack (LIFO)

### 1. Browser Back/Forward Navigation

```python
class BrowserHistory:
    def __init__(self, homepage: str):
        self.back_stack = []
        self.forward_stack = []
        self.current = homepage

    def visit(self, url: str):
        self.back_stack.append(self.current)
        self.current = url
        self.forward_stack.clear()

    def back(self, steps: int) -> str:
        while steps > 0 and self.back_stack:
            self.forward_stack.append(self.current)
            self.current = self.back_stack.pop()
            steps -= 1
        return self.current

    def forward(self, steps: int) -> str:
        while steps > 0 and self.forward_stack:
            self.back_stack.append(self.current)
            self.current = self.forward_stack.pop()
            steps -= 1
        return self.current
```

---

### 2. Undo/Redo Text Editor

```python
class TextEditor:
    def __init__(self):
        self.text = ""
        self.undo_stack = []
        self.redo_stack = []

    def write(self, word):
        self.undo_stack.append(self.text)
        self.text += word
        self.redo_stack.clear()

    def undo(self):
        if self.undo_stack:
            self.redo_stack.append(self.text)
            self.text = self.undo_stack.pop()

    def redo(self):
        if self.redo_stack:
            self.undo_stack.append(self.text)
            self.text = self.redo_stack.pop()
```

---

### 3. Expression Validation

```python
def validate_code(code: str) -> bool:
    stack = []
    pairs = {')': '(', '}': '{', ']': '['}

    for ch in code:
        if ch in '({[':
            stack.append(ch)
        elif ch in pairs:
            if not stack or stack.pop() != pairs[ch]:
                return False
    return not stack
```

---

### 4. Function Call Stack Simulation

```python
def simulate_call_stack(calls):
    stack = []
    for call in calls:
        if call.startswith("call"):
            stack.append(call)
        elif call == "return" and stack:
            stack.pop()
    return stack
```

---

### 5. Stock Span

```python
def stock_span(prices):
    stack = []
    span = [0] * len(prices)

    for i in range(len(prices)):
        while stack and prices[stack[-1]] <= prices[i]:
            stack.pop()
        span[i] = i + 1 if not stack else i - stack[-1]
        stack.append(i)
    return span
```

---

## Queue (FIFO)

### 6. Ticket Booking System

```python
from collections import deque

class TicketQueue:
    def __init__(self):
        self.q = deque()

    def join(self, person):
        self.q.append(person)

    def serve(self):
        return self.q.popleft() if self.q else None
```

---

### 7. Round Robin Scheduling

```python
from collections import deque

def round_robin(tasks, quantum):
    q = deque(tasks)
    result = []

    while q:
        name, time = q.popleft()
        if time > quantum:
            result.append((name, quantum))
            q.append((name, time - quantum))
        else:
            result.append((name, time))
    return result
```

---

### 8. Printer Queue

```python
from collections import deque

class PrinterQueue:
    def __init__(self):
        self.q = deque()

    def add_job(self, job):
        self.q.append(job)

    def print_job(self):
        return self.q.popleft() if self.q else None
```

---

### 9. Call Center

```python
from collections import deque

class CallCenter:
    def __init__(self):
        self.q = deque()

    def receive_call(self, customer):
        self.q.append(customer)

    def handle_call(self):
        return self.q.popleft() if self.q else None
```

---

### 10. Shortest Path (BFS)

```python
from collections import deque

def shortest_path(grid):
    rows, cols = len(grid), len(grid[0])
    q = deque([(0, 0, 0)])
    visited = set([(0, 0)])

    directions = [(1,0),(-1,0),(0,1),(0,-1)]

    while q:
        r, c, d = q.popleft()
        if (r, c) == (rows-1, cols-1):
            return d
        for dr, dc in directions:
            nr, nc = r+dr, c+dc
            if 0 <= nr < rows and 0 <= nc < cols and (nr,nc) not in visited and grid[nr][nc] == 0:
                visited.add((nr,nc))
                q.append((nr,nc,d+1))
    return -1
```

---

## Bonus: Sliding Window

```python
from collections import deque

def sliding_window_processing(data, k):
    q = deque()
    res = []

    for i in range(len(data)):
        while q and q[0] <= i - k:
            q.popleft()
        while q and data[q[-1]] < data[i]:
            q.pop()
        q.append(i)
        if i >= k - 1:
            res.append(data[q[0]])
    return res
```

---

## Complexity Summary

* Stack ops → O(1)
* Queue ops → O(1)
* BFS → O(n*m)
* Sliding Window → O(n)

---

**Now this is interview + real-world ready 🚀**
