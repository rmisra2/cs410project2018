import networkx as nx
import os, json
from similarity_graph import create_similarity_graph
from process_data import create_combined_user_reviews
from clustering import convert_similarity_graph_to_nx_graph

dirname = os.path.dirname(__file__)
reviews_file = os.path.join(dirname, './../data/reviews_100.json')

with open(reviews_file) as rf:
    reviews = json.load(rf)
    combined_user_reviews = create_combined_user_reviews(reviews)
    similarity_graph = create_similarity_graph(combined_user_reviews)
    graph = convert_similarity_graph_to_nx_graph(similarity_graph, 0.1)
    print(nx.clustering(graph))
