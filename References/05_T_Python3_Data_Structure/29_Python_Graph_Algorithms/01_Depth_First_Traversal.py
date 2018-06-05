

"""

Python - Graph Algorithms

Graphs are very useful data structures in solving many important mathematical challenges. For example computer network topology or analysing molecular structures of chemical compounds. They are also used in city traffic or route planning and even in human languages and their grammar. All these applications have a common challenge of traversing the graph using their edges and ensuring that all nodes of the graphs are visited. There are two common established methods to do this traversal which is described below.

Depth First Traversal :
Also called depth first search (DFS),this algorithm traverses a graph in a depth ward motion and uses a stack to remember to get the next vertex to start a search, when a dead end occurs in any iteration. We implement DFS for a graph in python using the set data types as they provide the required functionalities to keep track of visited and unvisited nodes.

"""

class graph:
    
    def __init__(self,gdict=None):
        if gdict is None:
            gdict = {}
        self.gdict = gdict
# Check for the visisted and unvisited nodes
def dfs(graph, start, visited = None):
    if visited is None:
        visited = set()
    visited.add(start)
    print(start)
    for next in graph[start] - visited:
        dfs(graph, next, visited)
    return visited

gdict = { "a" : set(["b","c"]),
                "b" : set(["a", "d"]),
                "c" : set(["a", "d"]),
                "d" : set(["e"]),
                "e" : set(["a"])
                }


dfs(gdict, 'a')


"""

When the above code is executed, it produces the following result −

a b d e c


"""
