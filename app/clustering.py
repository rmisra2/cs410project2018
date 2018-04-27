import networkx as nx

def convert_similarity_graph_to_nx_graph(similarity_graph, similarity_threshold):
    ids = similarity_graph.keys()
    edges = []
    for curr_id, similarities in similarity_graph.items():
        for similarity in similarities:
            other_id = list(similarity.keys())[0]
            similarity_score = similarity[other_id]
            if similarity_score > similarity_threshold:
                edges.append((curr_id, other_id, similarity_score))
    graph = nx.Graph()
    graph.add_nodes_from(ids)
    graph.add_weighted_edges_from(edges)
    return graph

