
# ALL MODULS
import pandas as pd 
from nltk.stem.porter import PorterStemmer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

class Analysis_Movies:
    def MainDef(name):
        Movies = pd.read_csv('CSV\MainCSV.csv')
        Movies= Movies.head(5000)
        Movies= Movies.drop(['Unnamed: 0'], axis=1)
        cv = CountVectorizer(max_features=5000,stop_words='english')
        vactor = cv.fit_transform(Movies['my_tag'])
        my_vactor = vactor.toarray()

        sim = cosine_similarity(my_vactor)

        movie_index = Movies['movie_id'][Movies["movie_name"] == name].index[0]
        distance = sim[movie_index]
        movies_list = sorted(list(enumerate(distance)),reverse=True,key = lambda x:x[1])[1:6]
        list_of_movies = []
        for i in movies_list:
            list_of_movies.append(Movies.iloc[i[0]].movie_name)
        return list_of_movies

# Analysis_Movies.MainDef("Ant-Man and the Wasp: Quantumania")