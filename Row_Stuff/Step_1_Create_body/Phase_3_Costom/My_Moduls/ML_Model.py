
# ALL MODULS
import pandas as pd 
import ast
from nltk.stem.porter import PorterStemmer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity


class Analysis_Movies:
    def test():
        return " test are runing well "
    
    def convert(text):
        L = []
        for i in ast.literal_eval(text):
            L.append(i['name']) 
        return L 
    
    # get keyword and tags in one columns 
    def movies_recomandation():
        df = pd.read_csv('CSV_files/tmdb_5000_movies.csv')
        Movies = df[['id','title','overview','genres','keywords','original_language','tagline','popularity']]
        
        #  delet un nessesory data and get only useful data in list
        Movies['genres'] = Movies['genres'].apply(Analysis_Movies.convert) 
        Movies['keywords'] = Movies['keywords'].apply(Analysis_Movies.convert) 
        Movies['genres'] = Movies['genres'].apply(lambda x :[i.replace(" ","") for i in x]) 
        Movies['keywords'] = Movies['keywords'].apply(lambda x :[i.replace(" ","") for i in x]) 
       
        #  murge both list and make one tag column
        Movies['mytags'] = Movies['genres'] + Movies['keywords'] 

        my_df = Movies[['id','title','mytags']] # add overview here 
        my_df['mytags'] = my_df['mytags'].apply(lambda x:" ".join(x)).apply(lambda x:x.lower())

        return my_df # return tagcolumns for each moveies ,title and id 
    
    # get convert tagline word into Row words (loved : love,"highschool:school")
    from nltk.stem.porter import PorterStemmer
    def mynltk(text):
        ps = PorterStemmer()
        y = []
        for i in text.split():
            y.append(ps.stem(i))
        return " ".join(y)

    def convert_words_row():
        my_df= Analysis_Movies.movies_recomandation()
        my_df['mytags'] = my_df['mytags'].apply(Analysis_Movies.mynltk)
        return my_df
    
    # convert word to number formate 
    def my_ml_model():
        my_df=Analysis_Movies.convert_words_row()
        cv = CountVectorizer(max_features=5000,stop_words='english')
        vector =cv.fit_transform(my_df['mytags']).toarray()

        sim = cosine_similarity(vector)#sklearn model
        return sim

