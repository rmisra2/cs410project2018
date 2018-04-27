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

# # what `create_combined_user_reviews` would return
# {
#     id1: 'text',
#     id2: 'texttt',
#     id3: 'skjdhfs',
#     id4: 'review',
# }

# {
#     id1: [{ id2: 0.3 }, { id3: 0.2 }, { id4: 0.4 }],
#     id1: [{ id2: 0.2 }, { id3: 0.4 }, { id4: 0.7 }],
#     id1: [{ id2: 0.5 }, { id3: 0.5 }, { id4: 0.3 }],
#     id1: [{ id2: 0.7 }, { id3: 0.1 }, { id4: 0.5 }]
# }
def create_sim_graph(user_combined_reviews):
    """
    creates a similarity graph by generating similarity score for
    every user pair
    - param reviews: return value from 'create_combined_user_reviews'
    - returns a dict where:
        key: user_id
        value: array of dictionaries where the key = every user but user_id and
        value = their respective similarity score per
    """
    user_dict = {}
    for user, review in user_combined_reviews.items():
        user_dict[user] = []
        for other,others_review in user_combined_reviews.items():
            if other != user:
                other_dict = {}
                similarity_score = similarity(review,others_review)
                other_dict[other] = similarity_score
                user_dict[user].append(other_dict)
    return user_dict

#testing:
#dict = {'id1':'i hate this restaurant', 'id2': 'i really like the food at this restaurant', 'id3': ' this restaurant had decent food and lighting', 'id4': 'though the lighting and food was fine at this restaurant, this place was smelly', 'id5':' restaurant unrelated similarity to the least'}
