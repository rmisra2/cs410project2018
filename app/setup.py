import nltk
from process_data import parse_reviews_dataset, parse_business_dataset

NUM_REVIEWS_TO_PROCESS = 200
NUM_RESTAURANTS_TO_PROCESS = 200

# nltk.download('punkt')
parse_reviews_dataset(NUM_REVIEWS_TO_PROCESS)
parse_business_dataset(NUM_RESTAURANTS_TO_PROCESS)
