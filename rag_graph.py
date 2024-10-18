import networkx as nx

class RAGGraph:
    @staticmethod
    def create_graph():
        G = nx.DiGraph()

        # Adding nodes for key ontology classes
        nodes = {
            "Study Objective": ("ellipse", "lightblue"),
            "LLMs": ("box", "lightgreen"),
            "GPT-3.5": ("box", "lightyellow"),
            "GPT-4": ("box", "lightyellow"),
            "Prometheus": ("box", "lightyellow"),
            "RAG Model": ("box", "lightyellow"),
            "Biomedical Domain": ("ellipse", "lightblue"),
            "DLBCL": ("box", "lightgreen"),
            "Retrieval-Augmented Generation (RAG)": ("ellipse", "lightcoral"),
            "Performance Metrics": ("ellipse", "lightblue"),
            "Accuracy": ("box", "lightgreen"),
            "Relevance": ("box", "lightgreen"),
            "Readability": ("box", "lightgreen"),
            "Methodology": ("ellipse", "lightblue")
        }

        # Add nodes to the graph
        for node, (shape, color) in nodes.items():
            G.add_node(node, shape=shape, color=color)

        # Adding edges to represent relationships
        edges = [
            ("Study Objective", "LLMs", "uses"),
            ("LLMs", "GPT-3.5", "includes"),
            ("LLMs", "GPT-4", "includes"),
            ("LLMs", "Prometheus", "includes"),
            ("LLMs", "RAG Model", "includes"),
            ("RAG Model", "Retrieval-Augmented Generation (RAG)", "uses"),
            ("Biomedical Domain", "DLBCL", "focuses on"),
            ("LLMs", "Biomedical Domain", "answers questions in"),
            ("Retrieval-Augmented Generation (RAG)", "Biomedical Domain", "provides context for"),
            ("RAG Model", "Performance Metrics", "evaluated by"),
            ("Performance Metrics", "Accuracy", "measures"),
            ("Performance Metrics", "Relevance", "measures"),
            ("Performance Metrics", "Readability", "measures"),
            ("RAG Model", "Methodology", "utilizes")
        ]

        # Add edges to the graph
        for source, target, label in edges:
            G.add_edge(source, target, label=label)

        return G
