# set NUM_REVIEWS and NUM_RESTAURANTS to -1 to use all of them
NUM_REVIEWS = 2000
NUM_RESTAURANTS_TO_PROCESS = -1

# set the number of restaurants that have been processed
# may not be the same as NUM_RESTAURANTS_TO_PROCESS since
# the final number of restaurants may be smaller than the input size
#
# NOTE: 69047 is the total number of restaurants
NUM_RESTAURANTS = 69047

# threshold of user reviews similary needed to remain an edge in the similarity graph
SIMILARITY_THRESHOLD = 0.5
