import networkx as nx

def save_graph(G, filename="knowledge_graph.gml"):
    nx.write_gml(G, filename)

def load_graph(filename="knowledge_graph.gml"):
    return nx.read_gml(filename)
