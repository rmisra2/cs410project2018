import nltk
from process_data import parse_reviews_dataset

NUM_REVIEWS_TO_PROCESS = 12321

nltk.download('punkt')
parse_reviews_dataset(NUM_REVIEWS_TO_PROCESS)
