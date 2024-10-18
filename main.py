from rag_graph import RAGGraph
from gml_utils import save_graph, load_graph
from graph_visualizer import visualize_graph
from datetime import datetime

if __name__ == "__main__":

    # Main execution script that creates, saves, and visualizes the knowledge graph.
    # Steps:
    #     1. Create the knowledge graph.
    #     2. Save it as a GML file.
    #     3. Visualize and save it as a PNG image.

    # Create a timestamp for unique filenames
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"knowledge_graph_{timestamp}"

    # Step 1: Create graph
    graph = RAGGraph.create_graph()

    # Step 2: Save the graph to GML format
    gml_filename = f"{filename}.gml"
    save_graph(graph, gml_filename)

    # Step 3: Visualize and save the graph as a PNG image
    png_filename = f"{filename}.png"
    visualize_graph(graph, png_filename)
