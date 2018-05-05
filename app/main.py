import networkx as nx
import os, json
import community
import time
from similarity_graph import create_similarity_graph
from process_data import create_combined_user_reviews
from clustering import convert_similarity_graph_to_nx_graph
from reverse_index import create_adjusted_reviews_for_restaurants, adjusted_search

NUM_REVIEWS = 200
NUM_RESTAURANTS = 69047

dirname = os.path.dirname(__file__)

reviews_file = './../data/reviews_{}.json'.format(NUM_REVIEWS)
reviews_filename = os.path.join(dirname, reviews_file)

restaurants_file = './../data/restaurants_{}.json'.format(NUM_RESTAURANTS)
restaurants_filename = os.path.join(dirname, restaurants_file)

similarity_graph_file = './../data/similarity_graph_{}.json'.format(NUM_REVIEWS)
similarity_graph_filename = os.path.join(dirname, similarity_graph_file)

partition_file = './../data/partition_{}.json'.format(NUM_REVIEWS)
partition_filename = os.path.join(dirname, partition_file)

# TODO: explicitly set the number of partitions?
def create_partition():
    with open(reviews_filename) as rf:
        reviews = json.load(rf)

        print('grouping users')
        combined_user_reviews = create_combined_user_reviews(reviews)

        print('creating user similarity graph')
        t1 = time.process_time()
        similarity_graph = create_similarity_graph(combined_user_reviews)
        t2 = time.process_time()
        print('similarity graph time elapsed: {}'.format(t2 - t1))

        with open(similarity_graph_filename, 'w') as sgf:
            json.dump(similarity_graph, sgf)
            print('similarity graph file created: {}'.format(similarity_graph_filename))

        print('creating networkx graph')
        graph = convert_similarity_graph_to_nx_graph(similarity_graph, 0.1)

        print('clustering users')
        partition = community.best_partition(graph)

        with open(partition_filename, 'w') as pf:
            json.dump(partition, pf)
            print('partition file created: {}'.format(partition_filename))

def create_reverse_index():
    with open(reviews_filename) as rf:
        reviews = json.load(rf)

    with open(restaurants_filename) as rsf:
        restaurants = json.load(rsf)

    partition_file = './../data/partition_{}.json'.format(NUM_REVIEWS)
    partition_filename = os.path.join(dirname, partition_file)
    with open(partition_filename) as pf:
        partition = json.load(pf)

    print('creating adjusted reviews for restaurants')
    adjusted_restaurant_reviews = create_adjusted_reviews_for_restaurants(
        reviews,
        restaurants,
        partition
    )

    adjusted_restaurants_file = './../data/adjusted_restaurants_{}.json'.format(NUM_RESTAURANTS)
    adjusted_restaurants_filename = os.path.join(dirname, adjusted_restaurants_file)
    with open(adjusted_restaurants_filename, 'w') as arf:
        json.dump(adjusted_restaurant_reviews, arf)
        print('adjusted restaurants file created: {}'.format(adjusted_restaurants_filename))

    adjusted_restaurants_filtered_file = './../data/adjusted_restaurants_filtered_{}.json'.format(NUM_RESTAURANTS)
    adjusted_restaurants_filtered_filename = os.path.join(dirname, adjusted_restaurants_filtered_file)
    with open(adjusted_restaurants_filtered_filename, 'w') as arff:
        adjusted_restaurant_reviews_filtered = {}
        for business_id, restaurant_data in adjusted_restaurant_reviews.items():
            if 'stars_by_cluster' in restaurant_data:
                adjusted_restaurant_reviews_filtered[business_id] = restaurant_data
        json.dump(adjusted_restaurant_reviews_filtered, arff)
        print('adjusted restaurants filtered file created: {}'.format(adjusted_restaurants_filtered_filename))

def generate_adjusted_search():
    adjusted_restaurants_filtered_file = './../data/adjusted_restaurants_filtered_{}.json'.format(NUM_RESTAURANTS)
    adjusted_restaurants_filtered_filename = os.path.join(dirname, adjusted_restaurants_filtered_file)
    with open(adjusted_restaurants_filtered_filename) as arff:
        adjusted_reviews = json.load(arff)

    search_output_file = './../data/search_output_{}.json'.format(NUM_RESTAURANTS)
    search_output_filename = os.path.join(dirname, search_output_file)
    with open(search_output_filename, 'w') as asof:
        print('generating search results')
        output = adjusted_search(adjusted_reviews)
        for line in output:
            asof.write('{}\n'.format(line))
        print('search results file created: {}'.format(search_output_filename))


create_partition()
create_reverse_index()
generate_adjusted_search()
