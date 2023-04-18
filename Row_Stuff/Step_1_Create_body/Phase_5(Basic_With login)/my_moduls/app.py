
import pandas as pd
from my_moduls.ml_model import Analysis_Movies
class Data_analysis():
    def find_by_genre(find_genre,df_path):
        df = pd.read_csv(df_path)
        # print(action_df.head(1))
        # find_genre = "Action"
        df['rating'] = df['rating'].fillna(0)
        #df.isnull().sum()
        movies_data = []
        Movies = df[['movie_id', 'movie_name', 'rating', 'genre']]
        sorted_data = Movies.sort_values(by='rating', ascending=False)[0:6]
        return sorted_data.values.tolist()
    
    def find_by_name(name):
        top_5_names =  Analysis_Movies.MainDef(name)
        return top_5_names
    

# Data_analysis.find_by_genre("Action",'CSV/action.csv')