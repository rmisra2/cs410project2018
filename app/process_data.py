import json
import os

infile = './../dataset/review.json'
infile_restaurants = './../dataset/business.json'

# TODO: make sure data folder exists
outfile = './../data/reviews.json'
outfile_restaurants = './../data/restaurants.json'

dirname = os.path.dirname(__file__)

infile_filename = os.path.join(dirname, infile)
outfile_filename = os.path.join(dirname, outfile)

infile_restaurants_filename = os.path.join(dirname, infile_restaurants)
outfile_restaurants_filename = os.path.join(dirname, outfile_restaurants)

BUSINESS_CATEGORIES = ['Restaurants', 'Food']

def parse_reviews_dataset(n=-1):
    """
    creates a json file of all yelp dataset reviews with necessary attributes
    param n: specifies the number of reviews to parse. if left unchanged, it will parse all reviews
    """
    reviews = []

    if n > 0:
        outfile = './../data/reviews_{}.json'.format(n)
        outfile_filename = os.path.join(dirname, outfile)
        c = 0

    with open(infile_filename) as f:
        for line in f:
            review_data = json.loads(line)
            review = {
                'review_id': review_data.get('review_id'),
                'user_id': review_data.get('user_id'),
                'business_id': review_data.get('business_id'),
                'text': review_data.get('text')
            }
            reviews.append(review)

            if n > 0:
                c += 1
                if c > n:
                    break

    with open(outfile_filename, 'w') as outf:
        json.dump(reviews, outf)

def group_reviews_by_users(reviews):
    """
    given a list of reviews, this will group them by user
    - param reviews: list of reviews
    - returns a dict where:
        key: user_id
        value: list of user_id's reviews
    """
    user_reviews = {}
    for review in reviews:
        user_id = review.get('user_id')
        if user_id not in user_reviews:
            user_reviews[user_id] = []
        review_without_user_id = {
            'review_id': review.get('review_id'),
            'business_id': review.get('business_id'),
            'text': review.get('text')
        }
        user_reviews[user_id].append(review_without_user_id)
    return user_reviews

def create_combined_user_reviews(reviews):
    """
    combines all a user's reviews into one combined string
    - param reviews: list of reviews
    - returns a dict where:
        key: user_id
        value: a string which is all the reviews for that user_id combined
    """
    user_reviews = group_reviews_by_users(reviews)
    user_combined_reviews = {}
    for user_id, reviews in user_reviews.items():
        combined_reviews = ''.join([r.get('text') for r in reviews])
        user_combined_reviews[user_id] = combined_reviews
    return user_combined_reviews

def parse_business_dataset(n=-1):
    """
    creates a json file of all yelp dataset restaurants with necessary attributes
    param n: specifies the number of restaurants to parse. if left unchanged, it will parse all restaurants
    """
    restaurants = []

    if n > 0:
        c = 0

    with open(infile_restaurants_filename) as f:
        for line in f:
            restaurant_data = json.loads(line)
            restaurant = {
                'business_id': restaurant_data.get('business_id'),
                'name': restaurant_data.get('name'),
                'stars': restaurant_data.get('stars')
            }

            restaurant_categories = restaurant_data.get('categories')
            if any(c for c in restaurant_categories if c in BUSINESS_CATEGORIES):
                restaurants.append(restaurant)

            if n > 0:
                c += 1
                if c > n:
                    break

    outfile_restaurants = './../data/restaurants_{}.json'.format(len(restaurants))
    outfile_restaurants_filename = os.path.join(dirname, outfile_restaurants)

    with open(outfile_restaurants_filename, 'w') as outf:
        json.dump(restaurants, outf)
