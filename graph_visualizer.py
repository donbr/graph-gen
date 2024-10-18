import networkx as nx
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

@staticmethod
def visualize_graph(G, filename="improved_knowledge_graph.png"):
    # Use spring layout for all nodes with adjusted parameters
    pos = nx.spring_layout(G, k=1.2, iterations=100)  # Increased k and iterations for better spread

    # Ensure all nodes are in the layout
    for node in G.nodes():
        if node not in pos:
            pos[node] = (0, 0)  # Default position if not placed by layout algorithm

    labels = nx.get_edge_attributes(G, 'label')
    color_map = [G.nodes[node].get("color", "gray") for node in G.nodes()]

    plt.figure(figsize=(24, 20))  # Increased figure size for better spacing
    plt.subplots_adjust(left=0.05, right=0.95, top=0.95, bottom=0.05)  # Adjust margins

    nx.draw(G, pos, with_labels=True, node_color=color_map, node_size=4000,  # Increased node size
            font_size=10, font_weight='bold', arrows=True, arrowsize=20,  # Increased font and arrow size
            edge_color='gray', width=1.0)  # Increased edge width

    # Draw edge labels with increased font size and slight offset
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels, font_color='red', font_size=8,
                                 bbox=dict(alpha=0.2, pad=0.5), label_pos=0.6)  # Added bbox and adjusted label position

    legend_elements = [
        mpatches.Patch(color='lightblue', label='Ontology Classes'),
        mpatches.Patch(color='lightgreen', label='Domain Elements'),
        mpatches.Patch(color='lightyellow', label='LLMs and Models'),
        mpatches.Patch(color='lightcoral', label='RAG Process')
    ]
    plt.legend(handles=legend_elements, loc='upper right', fontsize=12, bbox_to_anchor=(1, 1))

    plt.title("Knowledge Graph for RAG Model Study", fontsize=20, pad=20)
    
    plt.axis('off')  # Turn off the axis
    plt.tight_layout(pad=2.0)  # Added tight_layout with padding
    plt.savefig(filename, dpi=300, bbox_inches='tight', pad_inches=0.5)
    # plt.show()