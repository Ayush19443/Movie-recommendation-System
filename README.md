# Movie-recommendation-System
## INTRODUCTION
•	A recommendation System is a type of information filtering system which attempts to predict the preferences of a user, and make suggests based on these preferences.
•	For any given product, there are sometimes thousands of options to choose from.
•	Recommender system help to personalize a platform and help the user find something they like.
•	The Movie Recommendation System recommends the same movie to users with similar demographic features.
## PROBLEM STATEMENT AND MOTIVATION
•	One key reason why we need a recommender system in modern society is that people have too much options to use from, due to the prevalence of Internet.
•	Also, there has been explosive growth in the amount of available digital information and growth in the number of visitors to the Internet.
•	If we take the example of Netflix, it has large collection of movies.
•	Although, the amount of available information increased, now people had to invest a large amount of time selecting the items that they actually want to see.
•	Here comes the role of a Recommender System.
## METHODOLOGY FOLLOWED
There are various types of Movie Recommendation System.
•	CONTENT BASED MOVIE RECOMMENDATION SYSTEM
o	The Algorithm recommends movies that are similar to the ones’ that a user has liked in the past.
o	Using this type of recommender system, if a user watches one movie, similar movies are recommended.
•	COLLABORATIVE FILTERING MOVIE REOMMENDATION SYSTEM
o	This filtering Strategy is based on the combination of the user’s behavior and comparing and contrasting that with other user’s behavior in the database.
o	For example, if user A watches M1, M2 and M3 and user B watches M1, M3, M4, we recommend M1 and M3 to a similar user C.
For building the model, I have used Content Based Filtering.
•	Count Vectorizer is a great tool provided by the Scikit-learn library.
•	It is used to transform a given text into a vector on the basis of frequency of each word that occur in the entire text.
•	Count Vectorizer creates a matrix in which each unique word is represented by a column of the matrix and each text sample from the document is a row in the matrix.
•	Cosine Similarity is computed from the data we have about the items.
•	When a user searches a movie, then our model tries to find similar movies based on lead actors, the director, genre of the film etc. and suggests the movies to the user.
•	Cosine Similarity is a matric used to determine how similar two entities are irrespective of their size.
•	The cosine similarity is beneficial because even if the two similar data are far apart by the Euclidean distance because of the size, they could still have a smaller angle between them.
 
## TECHNOLOGY USED
•	Python: It supports multiple programming paradigms, including Procedural, Object-Oriented, and functional programming.
It is very easy to code in Python and anyone can learn python basics in short period of time.

•	Jupyter Notebook: It is an open-source web application that allows you to create and combine code, comments, multimedia and visualization in an interactive document-called notebook.

•	Flask: Flask is a small and lightweight python web framework that provides useful tools and features that make creating web applications in Python easier.

•	HTML: HTML is the standard markup language for documents designed to be displayed in a web Browser. It can be assisted by technologies such as CSS and JavaScript.
## DATASET
•	IMBD 5000 Movie Dataset
https://www.kaggle.com/carolzhangdc/imdb-5000-movie-dataset

•	Movies Dataset
https://www.kaggle.com/rounakbanik/the-movies-dataset
## ISSUES IN RECOMMENDATION SYSTEM
•	Cold Start: Cold Start problem when too little rating data is available in the initial state.
•	Stability vs Plasticity: When consumers have rated so many items, their preference in the established user profiles are difficult to change.
•	Privacy: The more the system know, the more precise the recommendations can get.
