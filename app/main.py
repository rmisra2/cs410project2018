import networkx as nx
import os, json
import community
from similarity_graph import create_similarity_graph
from process_data import group_reviews_by_users
from clustering import convert_similarity_graph_to_nx_graph

dirname = os.path.dirname(__file__)
reviews_file = os.path.join(dirname, './../data/reviews_100.json')

with open(reviews_file) as rf:
    reviews = json.load(rf)
    grouped_user_reviews = group_reviews_by_users(reviews)
    similarity_graph = create_similarity_graph(grouped_user_reviews)
    graph = convert_similarity_graph_to_nx_graph(similarity_graph, 0.1)
    partition = community.best_partition(graph)
    print(partition)
