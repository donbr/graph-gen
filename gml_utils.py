import networkx as nx

def save_graph(G, filename="knowledge_graph.gml"):
    """
    Save the graph object `G` to a GML file.

    Args:
        G (networkx.Graph): The knowledge graph to save.
        filename (str): The name of the GML file to save the graph to (default: 'knowledge_graph.gml').
    """
    nx.write_gml(G, filename)

def load_graph(filename="knowledge_graph.gml"):
    """
    Load a graph from a GML file.

    Args:
        filename (str): The name of the GML file to load the graph from (default: 'knowledge_graph.gml').

    Returns:
        networkx.Graph: The loaded knowledge graph.
    """
    return nx.read_gml(filename)
