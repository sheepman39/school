#   a421_one_movie_recommender.py
#   A basic movie recommendation code using average for a single user and single movie.
#   This code is based on the netflix-style-recommender project shared on GitHub.
#   It was written by Nikhil22.
#   The code has been modified from its original version.
import numpy as np 

# define the movies, users, and different ratings
movies = ["Back to the Future", "Guardians of the Galaxy", "Avatar", "Indiana Jones", "2001: A Space Odyssey"]
genres = ["Action", "Adventure", "Science Fiction", "Comedy"]

#TODO 1 change these values to the names of the students in your group
users = ["Tyler", "John", "Sarah", "Matt"]

#TODO 2 paste your ratings tables here
movie_ratings =[[8,8,0,5],
                [6,6,0,7],
                [3,8,0,7],
                [0,9,0,0],
                [0,0,0,0]]
user_preferences = [[4,5,5,3],
                    [3,3,5,4],
                    [3,3,3,4],
                    [4,4,3,5]]
movie_genre = [[0.6, 0.0, 0.3, 0.1],
               [0.2, 0.3, 0.3, 0.2],
               [0.3, 0.3, 0.4, 0.0],
               [0.6, 0.2, 0.0, 0.2],
               [0.4, 0.0, 0.6, 0.0]]

# TODO Your ratings, rate the five movies in the list below
# notice how your recommendations change when you add a rating for 1 movie
your_ratings = np.zeros((5, 1))
your_ratings[0] = 4 # rating for Back to the Future
your_ratings[1] = 3 # rating for Guardians of the Galaxy
your_ratings[2] = 1 # rating for Avatar
your_ratings[3] = 3 # rating for Indiana Jones
your_ratings[4] = 4 # rating for The Matrix

# --- Normalization Process ---
# ratings, movies_features, and user_prefs are arrays which are more structured lists
ratings = np.array(movie_ratings)
movie_features = np.array(movie_genre)
user_prefs = np.array(user_preferences)

# append your ratings to the data representing everyone elses
ratings = np.append(your_ratings, ratings, axis=1)

# to check if a user has rated a movie, create a matrix that shows
# a 1 if the user rated it and a 0 if not
did_rate = (ratings != 0 ) * 1

# function to normalize the data
def normalize_ratings(ratings, did_rate):
    num_movies = ratings.shape[0]
    
    ratings_mean = np.zeros(shape = (num_movies, 1))
    ratings_norm = np.zeros(shape = ratings.shape)
    
    for i in range(num_movies): 
        # Get all the indexes where there is a 1
        idx = np.where(did_rate[i] == 1)[0]
        #  Calculate mean rating of ith movie only from user's that gave a rating
        ratings_mean[i] = np.mean(ratings[i, idx])
        ratings_norm[i, idx] = ratings[i, idx] - ratings_mean[i]
    
    return ratings_norm, ratings_mean

# use the fuction to get normalized data sets
ratings_norm, ratings_mean = normalize_ratings(ratings, did_rate)

# print the predictions in a nice way:
for index in range(len(movies)):
    # grab index (integer), which remember, are all sorted based on the prediction values 
    print("%.1f is predicted for the movie %s" % (ratings_mean[index], movies[index]))


# Single user's rating 
# change these values to compare the ratings of different users and different movies
rating = 0 # a starting rating
user = 2 # represents the third user in the list of users
movie = 0 # represents the fourth movie in the list of movies

# get the estimated rating for a specific movie and a specific user
for genre in range(len(genres)):
    rating += user_preferences[user][genre] * movie_genre[movie][genre]
print(users[user]+"'s", movies[movie], "recommended rating: ", rating) 

