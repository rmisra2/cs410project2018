# Project Report and Documentation
## Overview:
The function of this tool is to filter Yelp restaurant reviews that are more relevant to a certain user based on certain user preferences. We will cluster users based on their reviews, using features identified by textual similarities in their reviews. This will be a `recommender system` that uses both content based and collaborative filtering that plays a role in the larger restaurant search process.The tool is beneficial to those who find that the average rating based on all reviews for a certain place do not match their personal preferences. For example, based on a rating on Yelp, a user walks into a restaurant X rated as 4 stars on Yelp, but actually thought the restaurant deserved 2 stars. With this tool, the user is recommended restaurants that match their own preferences over the average general public’s review. Yelp reviews are already subjective to begin with, so we hope to make use of that to enhance search results as opposed to being limited by it. There is a main `README.md` in the repo as well for setup instructions.
### Documentation of each step and packages used:
  A. The first step in this project is to download the [Yelp Dataset](https://www.yelp.com/dataset) and parse the reviews into a format we use for this project. The parsing functions are in `process_data.py` where we have 3 functions:

          1. parse_reviews_dataset(): This function parses through the entire dataset getting reviews.

          2. group_reviews_by_users(): This function takes in the input of the first function above and groups reviews by users (since we aim to find user groups based on a list of reviews passed in)

          3. create_combined_user_reviews(): This function combines all user reviews of one type into one combined string.

  B. After parsing data we needed to create a similarity graph. We first transformed the data documents into TF-IDF vectors, and then computed the cosine similarity between them. To implement this, we used the TfidfVectorizer in the Python packages of scikit-learn. We created a function called `create_similarity_graph()`, that takes in user_combined_reviews and returns a dictionary where the key is the user_id which points to an array of dictionaries with the similarity score with other users.

  C. The next step is to cluster users based on their similarity. We used the Networkx Python library along with the Community API  to convert the similarity dictionaries to a graph by connecting nodes to each user with weighted edges that represent the level of similarity between users. The functions to implement this stage are stated below:
  
          1. create_sim_graph(): First we had to convert our similarities from the previous step into a graph using the Networkx library.
          
          2. community.best_partition(): We used this function from the Community API to partition/cluster our graph since `nx.clustering()` only gives us clustering coefficients which is not helpful for the project as we need our function to indicate groups for data to be clustered in.

   D. Once we clustered our users based on their reviews’ similarities, we need a way to use that information while doing a restaurant search. Since our goal was to show a breakdown of how each clustered group rated a restaurant in addition to its overall rating, we had to create a “reverse index.” In this context, the restaurant data from the dataset only included the overall rating for each restaurant. We called what we created a “reverse index” since we go back to each restaurant and add each cluster’s average rating back into each restaurants data attributes. We can then display these results in our enhanced restaurant search. This was done by these three functions:

          1. parse_business_dataset(): parses the Yelp business data into a format we use internally. It filters out any business that doesn’t fall in the category of “restaurant” or “food.” We store all this information as a dictionary so we have constant time access to each restaurant’s data given its id. There also exists a parameter that allows the user to specify how many restaurants to process, but by default it will process all of them.

          2. create_adjusted_reviews_for_restaurants(): given the list of processed reviews, the set of all restaurants’ data, and the clustering of users, this adds each cluster’s ratings back into the restaurants’ data. It does this in two passes - the initial pass adds all reviews into their respective rating by cluster group, and the second pass resets each cluster group’s ratings to their average.

          3. adjusted_search(): given the restaurant data with the clustered group’s average ratings, this generates a formatted search result that displays each restaurant’s name, overall rating, and average rating from each cluster. There is a second parameter that allows the user to limit the number of restaurants to display.

### Team Dynamic/Project Breakdown:
Varun Munjeti: Came up with project Idea and what to do step by step. I worked on writing the code for the main pipeline and the reverse index. Also worked on portions of the report and video.

Richa Misra: Worked on creating a timeline and scheduling the scope of the project. Responsible for the “clustering” aspect of the project such as trying to implement the similarity graph in order to use the `nx.clustering()` function (which was our first approach) and testing it on sizeable review sets. Once we decided that `nx.clustering()` does not give us the output desired, we deleted our old clustering implementation. Worked on learning to implement the Community API (as recommended by our TA) and using the best_partition function and testing it with multiple review dataset sizes to see if results made sense with the scope to the project. Tested it with different similarity threshold parameters as well to see how the results would change and see which threshold value will be more valuable to the project. Helped write the documentation and conduct the video in the video presentation.

Pavani Malli: Worked on early parsing functions to gather data from the Yelp dataset in a format that was usable for our user-similarity graph libraries. I had to first figure out how the data should be structured and we decided to create a concatenated string of all of the user’s reviews. After matching each user to their associated reviews, we progressed into creating a similarity graph for them. For reference and to get started, I looked at the Cranfield dataset from MP2 to see how a ranking feature could be used. However, we decided to use TF-IDF indexing, specifically,  the TfidfVectorizer in the Python packages of scikit-learn. I also worked on creating the powerpoint and analyzing the results of our example output to see how the restaurant rating matched up with our user clusters average rating.