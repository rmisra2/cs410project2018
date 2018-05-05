def create_adjusted_reviews_for_restaurants(reviews, restaurants, clusters):
    """
    modifies the input restaurants by adding a 'stars_by_clusters' attribute,
    which is a dictionary where:
        - key: cluster group
        - value: average stars (rating) of the business for that cluster group

    param reviews - list of processed reviews
    param restaurants - dict of restaurants where:
                            - key: restaurant's business_id
                            - value: dict containing data of restaurant (name, average rating)
    param clusters - dict of clustered users where:
                        - key: user_id
                        - value: the cluster the user belongs in
    """

    # initial pass adds all reviews into their respective stars_by_cluster
    for review in reviews:
        user_id = review.get('user_id')
        business_id = review.get('business_id')
        stars = review.get('stars')

        cluster = clusters[user_id]

        restaurant = restaurants.get(business_id)
        if restaurant is None:
            # reviewed business is not in our set of restaurants
            # NOTE: this means that the review might not be for a restaurant
            # TODO: decide whether to include these
            restaurant = {}
        if 'stars_by_cluster' not in restaurant:
            restaurant['stars_by_cluster'] = {}
        if cluster not in restaurant['stars_by_cluster']:
            restaurant['stars_by_cluster'][cluster] = []
        restaurant['stars_by_cluster'][cluster].append(stars)

    # second pass resets the stars_by_cluster's values to the average
    for restaurant_id, restaurant_data in restaurants.items():
        for cluster, stars in restaurant_data['stars_by_cluster']:
            cluster_stars = restaurant_data['stars_by_cluster'][cluster]
            average_stars = sum(cluster_stars, 0.0) / len(cluster_stars)
            restaurant_data['stars_by_cluster'][cluster] = average_stars

    return restaurants
