# IMPORTING LIBRARIES
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

#READ CSV FILE
movies=pd.read_csv("main_data.csv")

movies.head()
movies.describe

# CHECK FOR NULL VALUES
movies.isna().sum()


cv = CountVectorizer()
count_matrix = cv.fit_transform(movies['comb'])


similarity = cosine_similarity(count_matrix)

# DEFINING RECOMMEND FUNCTION
def recommend(inp):
    i = movies.loc[movies['movie_title']==inp].index[0]
    lst = list(enumerate(similarity[i]))
    lst = sorted(lst, key = lambda x:x[1] ,reverse=True)
    lst = lst[1:11] # excluding first item since it is the requested movie itself
    l = []
    l1=[]
    l2=[]
    for i in range(len(lst)):
        a = lst[i][0]
        l.append(movies['movie_title'][a])
        l1.append(movies['genres'][a])
        l2.append(movies['director_name'][a])
        
    return l,l1,l2
