import networkx as nx 

#create an empty graph
G = nx.Graph()

# add node one at a time
G.add_node(1)

# or from an iterable container
G.add_nodes_from([2,3])

# can also add node attributes if its a 2-tuple (node, node_attribute_dict)
container = [(4, {"color": "red"}), (5, {"color": "green"})]
G.add_nodes_from(container)

# nodes from one graph can be added into another
H = nx.path_graph(10)
G.add_nodes_from(H)

# Graph H could also be used as a node in graph G. This allows for graphs of graphs, 
# files or functions...
G.add_node(H)

# graphs can also be grown by adding edges one at a time 
G.add_edge(1,2)
e = (2,3)
G.add_edge(*e) # unpack tuple

# or by adding a list of edges
container = [(1,2), (1,3)]
G.add_edges_from(container)

# clear existing nodes and edges
G.clear()

# networkx quietly ignores any nodes/edges that already exist
G.add_edges_from([(1,2), (1,3)])
G.add_node(1)
G.add_edge(1, 2)
G.add_node("spam")        # adds node "spam"
G.add_nodes_from("spam")  # adds 4 nodes: 's', 'p', 'a', 'm'
G.add_edge(3, 'm')

print(G.number_of_nodes())
print(G.number_of_edges())

# examine the elements of a graph using nodes edges adj and degree
print(list(G.nodes))
print(list(G.edges))
print(list(G.adj[1]))
print(G.degree[1])

# you can use an nbunch to report edges or degree from a subset of nodes
print(G.edges([2, 'm']))
print(G.degree([2, 3]))

# can access nodes and edges as either attributes or callables. attributes are convinient for 
# modifying node/edge data
G.nodes["spam"]["color"] = "blue"
G.edges[(1, 2)]["weight"] = 10

# callables are more useful for inspecting attributes
print(G.edges(data=True))
print(G.nodes(data="color"))

# you can remove edges and nodes in a similar fashion to adding them...
G.remove_node(2)
G.remove_nodes_from("spam")

print(list(G.nodes))
print(list(G.edges))