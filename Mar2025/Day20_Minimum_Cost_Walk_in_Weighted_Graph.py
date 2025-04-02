# There is an undirected weighted graph with n vertices labeled from 0 to n - 1.

# You are given the integer n and an array edges, where edges[i] = [ui, vi, wi] indicates that there is an edge between vertices ui and vi with a weight of wi.

# A walk on a graph is a sequence of vertices and edges. The walk starts and ends with a vertex, and each edge connects the vertex that comes before it and the vertex that comes after it. It's important to note that a walk may visit the same edge or vertex more than once.

# The cost of a walk starting at node u and ending at node v is defined as the bitwise AND of the weights of the edges traversed during the walk. In other words, if the sequence of edge weights encountered during the walk is w0, w1, w2, ..., wk, then the cost is calculated as w0 & w1 & w2 & ... & wk, where & denotes the bitwise AND operator.

# You are also given a 2D array query, where query[i] = [si, ti]. For each query, you need to find the minimum cost of the walk starting at vertex si and ending at vertex ti. If there exists no such walk, the answer is -1.

# Return the array answer, where answer[i] denotes the minimum cost of a walk for query i.

 

# Example 1:

# Input: n = 5, edges = [[0,1,7],[1,3,7],[1,2,1]], query = [[0,3],[3,4]]

# Output: [1,-1]

# Explanation:


# To achieve the cost of 1 in the first query, we need to move on the following edges: 0->1 (weight 7), 1->2 (weight 1), 2->1 (weight 1), 1->3 (weight 7).

# In the second query, there is no walk between nodes 3 and 4, so the answer is -1.

# Example 2:

# Input: n = 3, edges = [[0,2,7],[0,1,15],[1,2,6],[1,2,1]], query = [[1,2]]

# Output: [0]

# Explanation:


# To achieve the cost of 0 in the first query, we need to move on the following edges: 1->2 (weight 1), 2->1 (weight 6), 1->2 (weight 1).

 

import defaultdict
class Solution(object):
    def minimumCost(self, n, edges, query):

        # Step 1: Construct Graph
        graph = defaultdict(list)
        for u, v, w in edges:
            graph[u].append((v, w))
            graph[v].append((u, w))
        
        # Step 2: Find connected components and minimum AND value
        component = [-1] * n  # Stores the component id of each node
        min_and_value = {}  # Stores the min AND value for each component
        comp_id = 0
        
        def bfs(start):
            queue = deque([start])
            component[start] = comp_id
            visited = set([start])
            min_and = (1 << 30) - 1  # Large value for AND operation
            
            while queue:
                node = queue.popleft()
                for neighbor, weight in graph[node]:
                    min_and &= weight  # Track minimum AND value in the component
                    if neighbor not in visited:
                        visited.add(neighbor)
                        queue.append(neighbor)
                        component[neighbor] = comp_id

            min_and_value[comp_id] = min_and  # Store min AND for the component

        # Step 3: Identify Components
        for node in range(n):
            if component[node] == -1:  # If unvisited
                bfs(node)
                comp_id += 1  # Move to the next component id

        # Step 4: Answer Queries
        result = []
        for si, ti in query:
            if component[si] != component[ti]:  # If nodes are in different components
                result.append(-1)
            else:
                result.append(min_and_value[component[si]])  # Retrieve precomputed AND value

        return result

        


s = Solution()
n = 5
edges = [[0,1,7],[1,3,7],[1,2,1]]
query = [[0,3],[3,4]]
print(s.minimumCost(n,edges,query))  
