import nltk
from config import NUM_REVIEWS, NUM_RESTAURANTS_TO_PROCESS, SIMILARITY_THRESHOLD
from process_data import parse_reviews_dataset, parse_business_dataset

# the following line can be commented out after running it once
nltk.download('punkt')

parse_reviews_dataset(NUM_REVIEWS)
parse_business_dataset(NUM_RESTAURANTS_TO_PROCESS)
