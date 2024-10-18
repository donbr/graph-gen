from rag_graph import RAGGraph
from gml_utils import save_graph, load_graph
from graph_visualizer import visualize_graph
from datetime import datetime

if __name__ == "__main__":
    # Create a timestamp for unique filenames
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"knowledge_graph_{timestamp}"

    # Create graph
    graph = RAGGraph.create_graph()

    # Save graph definition to GML file
    gml_filename = f"{filename}.gml"
    save_graph(graph, gml_filename)

    # Visualize and save the graph as an image
    png_filename = f"{filename}.png"
    visualize_graph(graph, png_filename)
