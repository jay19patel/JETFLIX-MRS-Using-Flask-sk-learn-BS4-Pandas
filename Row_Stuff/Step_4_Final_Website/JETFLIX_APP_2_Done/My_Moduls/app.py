
import pandas as pd
import numpy as np
from My_Moduls.csv_manupilation import CSV_Manupilation
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from nltk.stem.porter import PorterStemmer

class Data_analysis(): 

    def mynltk(text):
        ps = PorterStemmer()
        y = []
        for i in text.split():
            y.append(ps.stem(i))
        return " ".join(y)
    
    def find_by_name(m_name):
        df = CSV_Manupilation.murge_all_csv()
        df = df.replace(to_replace="None", value=np.nan)
        df = df.dropna()
        df = df.drop_duplicates(subset=['title'])

        df['Released_date'] = df['Released_date'].apply(str)
        df['My_Tag']= df['title']+df['genres']+df['disciption']+df['Imdb_rating']+df['Released_date']
        df['My_Tag'] = df['My_Tag'].replace('[^\w\s]', ' ', regex=True)

        df['My_Tag'] = df['My_Tag'].apply(lambda x:"".join(x)).apply(lambda x:x.lower())

        df['My_Tag'] =df['My_Tag'].apply(Data_analysis.mynltk)

        cv = CountVectorizer(max_features=5000,stop_words='english')
        vector =cv.fit_transform( df['My_Tag']).toarray()

        sim = cosine_similarity(vector)

        top_movies=[]
        movie_index = df[df['title'] == m_name].index[0]
        movie_name = sorted(list(enumerate(sim[movie_index])),reverse=True,key=lambda x:x[1])[0:7]
        for i in movie_name:
            top_movies.append(df.iloc[i[0]])
        return top_movies
    
    def this_movie(m_name):
        df = CSV_Manupilation.murge_all_csv()
        df = df.replace(to_replace="None", value=np.nan)
        df = df.dropna()
        df = df.drop_duplicates(subset=['title'])
        this_movie = df[df['title'] == m_name].values.tolist()
        return this_movie

        
# Data_analysis.this_movie("Karma")