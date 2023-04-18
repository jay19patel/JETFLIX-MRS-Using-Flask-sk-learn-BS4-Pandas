import pandas as pd 
df = pd.read_csv('Data_analysis/tmdb_5000_movies.csv')

# -------- Titles : Columns -------
# 'budget', 'genres', 'homepage', 'id', 'keywords', 'original_language',
# 'original_title', 'overview', 'popularity', 'production_companies',   
# 'production_countries', 'release_date', 'revenue', 'runtime',
# 'spoken_languages', 'status', 'tagline', 'title', 'vote_average',     
# 'vote_count'


Movies = df[['id','title','overview','genres','keywords','original_language','tagline','popularity']]
# print(df[['title']])
# Movies.dropna(inplace=True) # delete Null values row 
# print(Movies.isnull().sum())


# create Keybord List 

import ast
def convert(text):
    L = []
    # ast is convert string to dict
    for i in ast.literal_eval(text):
        L.append(i['name']) 
    return L 

#  delet un nessesory data and get only useful data in list
Movies['genres'] = Movies['genres'].apply(convert) 
Movies['keywords'] = Movies['keywords'].apply(convert) 

# delete space in genres
Movies['genres'] = Movies['genres'].apply(lambda x :[i.replace(" ","") for i in x]) 
Movies['keywords'] = Movies['keywords'].apply(lambda x :[i.replace(" ","") for i in x]) 


#  murge both list and make one tag column
Movies['mytags'] = Movies['genres'] + Movies['keywords'] 

my_df = Movies[['id','title','mytags']] # add overview here 
my_df['mytags'] = my_df['mytags'].apply(lambda x:" ".join(x)).apply(lambda x:x.lower())
# print(my_df['mytags'][0])





# Netureal Langue function using NLTK 
# Natural Language Toolkit
#   normla to convert root word 
# import nltk
from nltk.stem.porter import PorterStemmer
ps = PorterStemmer()

def mynltk(text):
    y = []
    for i in text.split():
        y.append(ps.stem(i))
    return " ".join(y)

# print(ps.stem('salmankhan'))
my_df['mytags'] = my_df['mytags'].apply(mynltk)
# print(my_df['mytags'][0])

# Without NL :
# action adventure fantasy sciencefiction cultureclash future spacewar spacecolony society spacetravel futuristic romance space alien tribe alienplanet cgi marine soldier battle loveaffair antiwar powerrelations mindandsoul 3d

# With NL 
# action adventur fantasi sciencefict cultureclash futur spacewar spacecoloni societi spacetravel futurist romanc space alien tribe alienplanet cgi marin soldier battl loveaffair antiwar powerrel mindandsoul 3d

from sklearn.feature_extraction.text import CountVectorizer
cv = CountVectorizer(max_features=5000,stop_words='english')
vector =cv.fit_transform(my_df['mytags']).toarray()
# print(vector[0])

from sklearn.metrics.pairwise import cosine_similarity

sim = cosine_similarity(vector)
# print(sim.shape) #(4803, 4803)
# print(sim[0]) 


def recommend(m_name):
    movie_index = my_df[my_df['title'] == m_name].index[0]
    dist = sim[movie_index]
    movie_name = sorted(list(enumerate(sim[movie_index])),reverse=True,key=lambda x:x[1])[1:6]
    for i in movie_name:
        print(my_df.iloc[i[0]].title)

recommend('Spectre')


