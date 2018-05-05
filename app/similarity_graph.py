import nltk, string
from sklearn.feature_extraction.text import TfidfVectorizer

# https://stackoverflow.com/questions/8897593/similarity-between-two-text-documents
stemmer = nltk.stem.porter.PorterStemmer()
remove_punctuation_map = dict((ord(char), None) for char in string.punctuation)

def stem_tokens(tokens):
    return [stemmer.stem(item) for item in tokens]

def normalize(text):
    return stem_tokens(nltk.word_tokenize(text.lower().translate(remove_punctuation_map)))

vectorizer = TfidfVectorizer(tokenizer=normalize, stop_words='english')

def similarity(text1, text2):
    """
    uses cosine similarity
    """
    tfidf = vectorizer.fit_transform([text1, text2])
    return ((tfidf * tfidf.T).A)[0,1]

def average_reviews_similarity(user1, user2):
    """
    calculates review text similarity for every review of one user's against the other's
    NOTE: not being used anymore since it greatly increases runtime of pipeline
    """
    similarities = []
    for u1_reviews in user1.values():
        for u2_reviews in user2.values():
            for u1_review in u1_reviews:
                for u2_review in u2_reviews:
                    review_similarity = similarity(u1_review['text'], u2_review['text'])
                    similarities.append(review_similarity)
    average = sum(similarities, 0.0) / len(similarities)
    return average

def create_similarity_graph(user_combined_reviews):
    """
    creates a similarity graph by generating a similarity score for every user pair
    - param user_reviews: return value from 'create_combined_user_reviews'
    - returns a dict where:
        key: user_id
        value: list of dicts where:
            key = other's user id
            value = their respective similarity score
    """
    similarity_graph = {}
    for curr_user_id, review in user_combined_reviews.items():
        similarity_graph[curr_user_id] = []
        for other_user_id, others_review in user_combined_reviews.items():
            if other_user_id != curr_user_id:
                similarity_graph[curr_user_id].append({
                    other_user_id: similarity(review, others_review)
                })
    return similarity_graph
