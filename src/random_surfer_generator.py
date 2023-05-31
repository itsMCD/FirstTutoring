import random as r
import networkx as nx
import matplotlib.pyplot as plt


def generate_internet(amount_of_nodes, min_hyperlinks_per_page, max_hyperlinks_per_page):
    ''' returns the dictionary with the amount of nodes, and a list of the hyperlink connections '''
    out = {'Nodes': amount_of_nodes, 'Links': []}
    for i in range(amount_of_nodes):
        for link in range(r.randint(min_hyperlinks_per_page, max_hyperlinks_per_page)):
            out['Links'].append((i, r.randint(0, amount_of_nodes-1)))
    return out

def read_internet(file_path):
    ''' Reads a text file and generates a graph in the same data format as generate_internet '''
    with open(file_path, 'r') as file:
        lines = file.readlines()
        
        # Get the number of nodes from the first line
        amount_of_nodes = int(lines[0].strip())
        
        # Create the graph data dictionary
        graph_data = {'Nodes': amount_of_nodes, 'Links': []}
        
        # Parse the remaining lines to generate the links
        for line in lines[1:]:
            links = line.split()
            source_node = int(links[0])
            
            # Add each link to the graph data
            for i in range(1, len(links), 2):
                target_node = int(links[i])
                graph_data['Links'].append((source_node, target_node))
    
    return graph_data

def draw_internet(graph_data):
    ''' Draws the generated internet graph '''
    internet_graph = nx.DiGraph()
    
    # Add nodes to the graph
    internet_graph.add_nodes_from(range(graph_data['Nodes']))
    
    # Create a dictionary to store the count of connections between each pair of nodes
    connection_counts = {}
    
    # Add edges to the graph
    for link in graph_data['Links']:
        source_node, target_node = link
        
        # Increase the connection count between the pair of nodes
        connection_counts[(source_node, target_node)] = connection_counts.get((source_node, target_node), 0) + 1
        
        # Add multiple edges between the same pair of nodes
        for i in range(connection_counts[(source_node, target_node)]):
            internet_graph.add_edge(source_node, target_node, label=str(i+1))  # Use the label to differentiate multiple edges
    
    # Position the nodes in a circular layout
    pos = nx.circular_layout(internet_graph)
    
    # Draw the nodes
    nx.draw_networkx_nodes(internet_graph, pos, node_color='lightblue', node_size=500)
    
    # Draw the edges with labels
    nx.draw_networkx_edges(internet_graph, pos, edge_color='gray', arrows=True)
    nx.draw_networkx_edge_labels(internet_graph, pos, edge_labels=nx.get_edge_attributes(internet_graph, 'label'))
    
    # Draw node labels
    nx.draw_networkx_labels(internet_graph, pos)
    
    # Show the graph
    plt.axis('off')
    plt.show()

def main():
    web = generate_internet(10, 5, 30)
    draw_internet(web)

if __name__ == '__main__':
    main()