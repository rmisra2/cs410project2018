import networkx as nx
import os, json
import community
from similarity_graph import create_similarity_graph
from process_data import group_reviews_by_users
from clustering import convert_similarity_graph_to_nx_graph
from reverse_index import create_adjusted_reviews_for_restaurants

NUM_REVIEWS = 200
NUM_RESTAURANTS = 69047

dirname = os.path.dirname(__file__)
reviews_file = './../data/reviews_{}.json'.format(NUM_REVIEWS)
reviews_filename = os.path.join(dirname, reviews_file)

restaurants_file = './../data/restaurants_{}.json'.format(NUM_RESTAURANTS)
restaurants_filename = os.path.join(dirname, restaurants_file)

# TODO: explicitly set the number of partitions?
def create_partition():
    with open(reviews_filename) as rf:
        reviews = json.load(rf)
        grouped_user_reviews = group_reviews_by_users(reviews)
        similarity_graph = create_similarity_graph(grouped_user_reviews)
        graph = convert_similarity_graph_to_nx_graph(similarity_graph, 0.1)
        partition = community.best_partition(graph)

        partition_file = './../data/partition_{}.json'.format(NUM_REVIEWS)
        partition_filename = os.path.join(dirname, partition_file)
        with open(partition_filename, 'w') as pf:
            json.dump(partition, pf)

def create_reverse_index():
    with open(reviews_filename) as rf:
        reviews = json.load(rf)

    with open(restaurants_filename) as rsf:
        restaurants = json.load(rsf)

    partition_file = './../data/partition_{}.json'.format(NUM_REVIEWS)
    partition_filename = os.path.join(dirname, partition_file)
    with open(partition_filename) as pf:
        partition = json.load(pf)

    adjusted_restaurant_reviews = create_adjusted_reviews_for_restaurants(
        reviews,
        restaurants,
        partition
    )

    adjusted_restaurants_file = './../data/adjusted_restaurants_{}.json'.format(NUM_RESTAURANTS)
    adjusted_restaurants_filename = os.path.join(dirname, adjusted_restaurants_file)
    with open(adjusted_restaurants_filename, 'w') as arf:
        json.dump(adjusted_restaurant_reviews, arf)

    adjusted_restaurants_filtered_file = './../data/adjusted_restaurants_filtered_{}.json'.format(NUM_RESTAURANTS)
    adjusted_restaurants_filtered_filename = os.path.join(dirname, adjusted_restaurants_filtered_file)
    with open(adjusted_restaurants_filtered_filename, 'w') as arff:
        adjusted_restaurant_reviews_filtered = {}
        for business_id, restaurant_data in adjusted_restaurant_reviews.items():
            if 'stars_by_cluster' in restaurant_data:
                adjusted_restaurant_reviews_filtered[business_id] = restaurant_data
        json.dump(adjusted_restaurant_reviews_filtered, arff)
