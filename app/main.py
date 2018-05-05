import networkx as nx
import os, json
import community
from similarity_graph import create_similarity_graph
from process_data import group_reviews_by_users
from clustering import convert_similarity_graph_to_nx_graph
from reverse_index import create_adjusted_reviews_for_restaurants

NUM_REVIEWS = 200

dirname = os.path.dirname(__file__)
reviews_file = './../data/reviews_{}.json'.format(NUM_REVIEWS)
reviews_filename = os.path.join(dirname, reviews_file)

def create_partition():
    with open(reviews_filename) as rf:
        reviews = json.load(rf)
        grouped_user_reviews = group_reviews_by_users(reviews)
        similarity_graph = create_similarity_graph(grouped_user_reviews)
        graph = convert_similarity_graph_to_nx_graph(similarity_graph, 0.1)
        partition = community.best_partition(graph)

        partition_file = './../data/partition_{}'.format(NUM_REVIEWS)
        partition_filename = os.path.join(dirname, partition_file)
        with open(partition_filename, 'w') as pf:
            json.dump(partition, pf)

