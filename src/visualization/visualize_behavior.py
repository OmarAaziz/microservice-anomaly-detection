import matplotlib.pyplot as plt
import networkx as nx

def create_graph():
    """
    Create a directed graph representing the microservice ecosystem with normal
    and malicious behavior paths.
    """
    # Initialize a directed graph
    G = nx.DiGraph()

    # Define nodes for the ecosystem
    nodes = {
        "Microservice Cluster": "normal",
        "Attack Simulator": "malicious",
        "Logs": "normal",
        "Dataset": "normal",
        "Machine Learning Models": "normal",
        "Detection System": "normal",
        "API Gateway": "normal",
        "Service Mesh": "normal",
        "Pods": "normal",
        "Kubernetes Control Plane": "normal",
        "Malicious Behavior": "malicious",
        "Normal Behavior": "normal"
    }

    # Add nodes to the graph
    G.add_nodes_from(nodes.keys())

    # Define relationships between nodes (edges)
    edges = [
        # Normal behavior flow
        ("Microservice Cluster", "Pods"),
        ("Pods", "Kubernetes Control Plane"),
        ("API Gateway", "Microservice Cluster"),
        ("Service Mesh", "Microservice Cluster"),
        ("Microservice Cluster", "Logs"),
        ("Logs", "Dataset"),
        ("Dataset", "Machine Learning Models"),
        ("Machine Learning Models", "Detection System"),
        ("Detection System", "Normal Behavior"),
        
        # Malicious behavior flow
        ("Attack Simulator", "Malicious Behavior"),
        ("Attack Simulator", "Microservice Cluster"),
        ("Attack Simulator", "Logs"),
        ("Malicious Behavior", "Detection System")
    ]

    # Add edges to the graph
    G.add_edges_from(edges)

    return G, nodes, edges

def visualize_graph(G, nodes, edges):
    """
    Visualize the graph with color-coded nodes and edges to represent normal
    and malicious behavior.
    """
    # Define node colors based on behavior
    node_colors = [
        "red" if nodes[node] == "malicious" else "green"
        for node in G.nodes()
    ]

    # Define edge styles based on behavior
    normal_edges = [edge for edge in edges if "Malicious Behavior" not in edge]
    malicious_edges = [edge for edge in edges if "Malicious Behavior" in edge]

    # Draw the graph
    plt.figure(figsize=(14, 10))
    pos = nx.spring_layout(G, seed=42)  # Layout for positioning nodes

    # Draw normal behavior
    nx.draw_networkx_nodes(G, pos, nodelist=nodes.keys(), node_size=2000, node_color=node_colors)
    nx.draw_networkx_edges(G, pos, edgelist=normal_edges, edge_color="blue", arrows=True)
    nx.draw_networkx_edges(G, pos, edgelist=malicious_edges, edge_color="red", style="dashed", arrows=True)

    # Add labels
    nx.draw_networkx_labels(G, pos, font_size=10, font_family="sans-serif")

    # Add a legend
    plt.scatter([], [], c="green", label="Normal Node")
    plt.scatter([], [], c="red", label="Malicious Node")
    plt.plot([], [], c="blue", label="Normal Edge")
    plt.plot([], [], c="red", linestyle="dashed", label="Malicious Edge")
    plt.legend(loc="upper left", fontsize=10)

    # Add title
    plt.title("Microservice Ecosystem: Normal vs Malicious Behavior", fontsize=16)
    plt.axis("off")  # Hide the axes

    # Show the plot
    plt.show()

if __name__ == "__main__":
    # Create the graph
    G, nodes, edges = create_graph()

    # Visualize the graph
    visualize_graph(G, nodes, edges)

