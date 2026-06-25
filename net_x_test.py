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
