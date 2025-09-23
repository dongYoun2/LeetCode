[Problem](https://leetcode.com/problems/accounts-merge/)


## DFS

We can use DFS to traverse the graph and find the connected components (asking 'connectivity' is a classic graph problem). Each unique email is a vertex, and an edge exists between two vertices if the two emails are in the same account (typically by linking all to the first email in that account).

[Submission](https://leetcode.com/problems/accounts-merge/submissions/1779426282/) (Runtime: 30 ms, Memory: 23.34 MB)

**Symbols**:
- $N$: # input rows (original accounts)
- $k_i$: # emails in row i
- $M=\sum_i k_i$: total email entries (with duplicates)
- $U$: # unique emails (graph vertices)

**TC**: $O(M + U log U)$
- **time for building graph**: $O(M)$
- **time for DFS traversal**: $O(V + E)$ -> $O(U + (M - N))$ -> $O(M)$ since $U \leq M$ and $N \leq M$. ($V$: # vertices, $E$: # edges)
- **time for sorting in the component**: $O(U log U)$ (total sorting cost across all components is bounded by $U log U$)
- therefore, adding these up, we get $O(M + U log U)$

**SC**: $O(M)$
- **space for graph**: $O(V + E)$ -> $O(U + (M - N))$ -> $O(M)$
- **space needed for performing DFS**: $O(V)$ -> $O(U)$
- thus, adding these up, we get $O(M + U)$ -> $O(M)$


```python
class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        # Build email graph and remember name for each email
        graph = defaultdict(set)
        email_to_name = {}

        for acc in accounts:
            name, emails = acc[0], acc[1:]

            for e in emails:
                email_to_name[e] = name
            # connect all emails in the same account with the first email
            first = emails[0]
            for e in emails[1:]:
                graph[first].add(e)
                graph[e].add(first)

        # Traverse connected components
        seen = set()
        merged = []

        for email in email_to_name:
            if email in seen:
                continue
            comp = []
            stack = [email]
            seen.add(email)
            while stack:
                curr = stack.pop()
                comp.append(curr)
                for nei in graph[curr]:
                    if nei not in seen:
                        stack.append(nei)
                        seen.add(nei)
            comp.sort()
            merged.append([email_to_name[email]] + comp)

        return merged

```



## Union Find (Disjoint Set Union)

The core idea is we give every unique email an ID, and for each account (each row in the input), we union all its emails with the first email.

**More about union-find data structure**:

Union-find helps us to:
1. **merge** two groups efficiently (union)
2. **check** whether two elements are in the same group (find/connected)

There are two tips to keep things fast in practice:
1. **Path compression** (during find)
As we walk up to the root, we make everything on the path point directly to the root. Future finds become almost $O(1)$.
2. **Union by rank/size** (during union)
Always attach the smaller tree under the larger one, so trees stay shallow.

<br>

[Submission](https://leetcode.com/problems/accounts-merge/submissions/1779477814/) (Runtime: 31 ms, Memory: 21 MB)


**TC**: $O(M + U log U)$
- **build maps (ids, names)**: $O(M)$
- **union operations**: $O((M-N)\alpha)$ (here, $\alpha$ is the inverse Ackermann function (very slow growing function), which is bounded by a **constant**)
- **find/grouping**: $O(U\alpha)$
- **sorting inside groups**: $O(U \log U)$
- **overall**: Adding these up, we get $O(M + U \log U)$

**SC**: $O(U)$
- **DSU arrays**: $O(U)$
- **maps + groups + output**: $O(U)$
- **overall**: $O(U)$


```python
class DSU:
    def __init__(self, n: int):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, x: int) -> int:
        if self.parent[x] != x:
            # path compression: flatten the tree
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, a: int, b: int) -> None:
        ra, rb = self.find(a), self.find(b)
        if ra == rb:
            return
        if self.rank[ra] < self.rank[rb]:
            ra, rb = rb, ra
        self.parent[rb] = ra
        if self.rank[ra] == self.rank[rb]:
            self.rank[ra] += 1


class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        email_to_id = {}
        email_to_name = {}
        i = 0

        # Assign id to each email and remember its name
        for acc in accounts:
            name = acc[0]
            for e in acc[1:]:
                if e not in email_to_id:
                    email_to_id[e] = i
                    email_to_name[e] = name
                    i += 1

        dsu = DSU(i)

        # Union all emails that appear in the same account
        for acc in accounts:
            first = email_to_id[acc[1]]
            for e in acc[2:]:
                dsu.union(first, email_to_id[e])

        # Group emails by their root
        groups = defaultdict(list)
        for e, idx in email_to_id.items():
            root = dsu.find(idx)
            groups[root].append(e)

        # Build results (sort emails within each group)
        res = []
        for emails in groups.values():
            emails.sort()
            res.append([email_to_name[emails[0]]] + emails)
        return res

```

There may be an error if the input is too large so that recursion stack overflows in the `find()` methd. In this case, instead of fully flattening the tree, we can halve the path with the iterative approach (below code snippet).

```python
def find(self, x: int) -> int:
    while x != self.parent[x]:
        self.parent[x] = self.parent[self.parent[x]]  # path halving
        x = self.parent[x]
    return x
```