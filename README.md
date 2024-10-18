# Knowledge Graph App Documentation

## Overview

Welcome to the **Knowledge Graph App**, where substance meets structure. This tool focuses on defining relationships in a graph that’s optimized for retrieval-augmented generation (RAG) models, but with a twist of keeping things AI-friendly and not just about visuals. So yes, you might be tempted to say, **"We Don't Need Pretty Pictures... But We Have Them Anyway!"** 😎

This app is built for the people who need their data structured and their relationships clear — whether you're a developer, data scientist, or AI enthusiast. And while we aren’t just about the visuals, rest assured that when you *do* need a pretty picture, we’ve got you covered.

### TL;DR: How to Install and Run It

1. **Clone the repository:**

   ```bash
   git clone https://github.com/donbr/graph-gen.git
   cd graph-gen
   ```

2. **Install the required libraries:**

   ```bash
   pip install -r requirements.txt
   ```

3. **Run the app:**

   ```bash
   python main.py
   ```

   This will generate the knowledge graph, save it to a GML file, and create a visual representation in PNG format.

## Key Components

### 1. **Graph Definition**
The backbone of this app is the structure—the knowledge graph itself. Built using NetworkX, it defines nodes and edges based on concepts from a RAG model study (see citation below). Nodes represent language models (e.g., GPT-3.5, GPT-4), biomedical domains, and performance metrics (e.g., accuracy, readability). The relationships between these are what drive the value of the graph, and that’s where the magic happens.

#### Key Features:
- **Node Creation:** Nodes include key RAG model components like language models, the biomedical domain, and various performance metrics.
- **Edge Relationships:** Edges are clearly labeled to make the graph intuitive. These edges describe relationships like "uses," "evaluates," and "includes."

### 2. **Graph Visualization**
We get it—sometimes you need a good visualization. While this app separates the core graph structure from the visual component, we’ve included a slick, customizable way to render the graph when needed. And trust us, it's not just pretty—it’s functional.

#### Visualization Features:
- **Customizable Layout:** We use a spring layout to ensure optimal spacing and clarity in relationships.
- **Node and Edge Styling:** Color-coded nodes and labeled edges make it easy to see what's happening at a glance. Ontology classes, domain elements, and LLMs each have their own color scheme.
- **Legend and Labels:** A built-in legend and edge labels ensure that even the most complex relationships are easy to understand.

### 3. **AI-Friendly Format**
This app was built with AI models in mind. The structure is clean, the relationships are clear, and it's ready to be processed by language models like GPT or other machine learning algorithms. No clutter, just well-defined nodes and edges that make AI-driven discovery and reasoning easier.

## Folder Structure

```
├── .gitignore                 # Ignored files
├── README.md                  # Documentation
├── gml_utils.py               # Helper functions for loading and saving graphs
├── graph_visualizer.py        # Functions for visualizing the graph
├── main.py                    # Main execution script
├── rag_graph.py               # Core graph definition
├── requirements.txt           # Required libraries (NetworkX, Matplotlib)
```

### Graph Definition (`rag_graph.py`)
The core of the app! This file defines the relationships between the various nodes in a RAG model study, such as language models (GPT-3.5, GPT-4) and performance metrics (accuracy, relevance, etc.). The structure is clear, efficient, and optimized for data processing.

### Visualization (`graph_visualizer.py`)
When it’s time to show off your graph, this file brings the relationships to life. Using Matplotlib, it generates clean, professional visualizations that make even the most complex graphs easy to interpret. So while we say, "We don’t need pretty pictures," we know that sometimes you do. 😉

### Utility Functions (`gml_utils.py`)
This file is all about keeping your graph reusable. It provides functions to save the graph in GML format and load it when you need it. This ensures you can easily move between different tasks, whether it's editing the graph, visualizing it, or running AI models on it.

## Example Workflow

1. **Define the Graph:**
   - Use the `RAGGraph.create_graph()` function to define the graph structure, with nodes like GPT-4, biomedical domains, and performance metrics.
   
2. **Save the Graph:**
   - Save the graph to a GML file using `save_graph()`. This makes it reusable and easily shareable.

3. **Visualize the Graph:**
   - If needed, generate a visual representation using `visualize_graph()`. It’s designed to be flexible, clear, and informative—no unnecessary frills, just what you need to understand the relationships.

4. **Integrate with AI Models:**
   - The graph is designed to be interpreted by language models like GPT, making it ideal for machine learning or AI applications.

## Citation

This knowledge graph app is based on the article: *"Improving accuracy of GPT-3/4 results on biomedical data using a retrieval-augmented language model"*. Full study available at: [PLoS Digital Health](https://journals.plos.org/digitalhealth/article?id=10.1371/journal.pdig.0000568).

---

**And that’s it!** A simple, clear tool to create meaningful relationships in a graph, built for both humans and AI alike. With or without visuals, the data shines on its own—but if you ever need that extra "wow" factor, we’ve got some pretty pictures for you too.


### Citation

If you use this project, please cite it and the following paper:

- **Improving accuracy of GPT-3/4 results on biomedical data using a retrieval-augmented language model**  
  DOI: [10.1371/journal.pdig.0000568](https://journals.plos.org/digitalhealth/article?id=10.1371/journal.pdig.0000568)

Here’s the BibTeX entry for the paper:

```bibtex
@article{rag_model_2024,
  title={Improving accuracy of GPT-3/4 results on biomedical data using a retrieval-augmented language model},
  author={Author(s) Name(s)},
  journal={PLOS Digital Health},
  year={2024},
  volume={2},
  number={10},
  pages={e0000568},
  doi={10.1371/journal.pdig.0000568}
}
