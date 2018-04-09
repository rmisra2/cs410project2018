import json

infile = 'dataset/review.json'

# TODO: make sure data folder exists
outfile = 'data/reviews.json'

def parse_reviews_dataset(n=-1):
    """
    creates a json file of all yelp dataset reviews with necessary attributes
    n specifies the number of reviews to parse. if left unchanged, it will parse all reviews
    """
    reviews = []

    if n > 0:
        outfile = 'data/reviews_{}.json'.format(n)
        c = 0

    with open(infile) as f:
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

    with open(outfile, 'w') as outf:
        json.dump(reviews, outf)

def group_reviews_by_users(reviews):
    """
    given a list of reviews, this will group them by user
    returns a dict where the key is the user_id and the value is a list of their reviews
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


# parse_reviews_dataset(1000)
