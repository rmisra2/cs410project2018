import json
import os

BUSINESS_CATEGORIES = ['Restaurants', 'Food']

def parse_reviews_dataset(n=-1):
    """
    creates a json file of all yelp dataset reviews with necessary attributes
    param n: specifies the number of reviews to parse. if left unchanged, it will parse all reviews
    """
    reviews = []

    if n > 0:
        c = 0

    dirname = os.path.dirname(__file__)

    infile_reviews = './../dataset/review.json'
    infile_reviews_filename = os.path.join(dirname, infile_reviews)

    with open(infile_reviews_filename) as f:
        for line in f:
            review_data = json.loads(line)
            review = {
                'review_id': review_data.get('review_id'),
                'user_id': review_data.get('user_id'),
                'business_id': review_data.get('business_id'),
                'text': review_data.get('text'),
                'stars': review_data.get('stars')
            }
            reviews.append(review)

            if n > 0:
                c += 1
                if c > n:
                    break

    outfile_reviews = './../data/reviews_{}.json'.format(n) if n > 0 else './../data/reviews.json'
    outfile_reviews_filename = os.path.join(dirname, outfile_reviews)

    with open(outfile_reviews_filename, 'w') as outf:
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
    restaurants = {}

    if n > 0:
        c = 0

    dirname = os.path.dirname(__file__)

    infile_restaurants = './../dataset/business.json'
    infile_restaurants_filename = os.path.join(dirname, infile_restaurants)

    with open(infile_restaurants_filename) as f:
        for line in f:
            restaurant_data = json.loads(line)
            restaurant = {
                'name': restaurant_data.get('name'),
                'stars': restaurant_data.get('stars'),
                'review_count': restaurant_data.get('review_count')
            }

            restaurant_id = restaurant_data.get('business_id')
            restaurant_categories = restaurant_data.get('categories')
            if any(c for c in restaurant_categories if c in BUSINESS_CATEGORIES):
                restaurants[restaurant_id] = restaurant

            if n > 0:
                c += 1
                if c > n:
                    break

    outfile_restaurants = './../data/restaurants_{}.json'.format(len(restaurants))
    outfile_restaurants_filename = os.path.join(dirname, outfile_restaurants)

    with open(outfile_restaurants_filename, 'w') as outf:
        json.dump(restaurants, outf)
