


"""

Display graph vertices
To display the graph vertices we simple find the keys of the graph dictionary. We use the keys() method.


"""

class graph:
    def __init__(self,gdict=None):
        if gdict is None:
            gdict = []
        self.gdict = gdict

# Get the keys of the dictionary
    def getVertices(self):
        return list(self.gdict.keys())

# Create the dictionary with graph elements
graph_elements = { "a" : ["b","c"],
                "b" : ["a", "d"],
                "c" : ["a", "d"],
                "d" : ["e"],
                "e" : ["d"]
                }

g = graph(graph_elements)

print(g.getVertices())


"""

When the above code is executed, it produces the following result −

['d', 'b', 'e', 'c', 'a']


"""



