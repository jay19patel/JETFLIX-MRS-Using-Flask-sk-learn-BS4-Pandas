import pandas as pd
import numpy as np

class CSV_Manupilation():
    def murge_all_csv():
        df1 = pd.read_csv('all_csv/Action and adventure.csv')
        df2 = pd.read_csv('all_csv/Anime.csv')
        df3 = pd.read_csv('all_csv/Bengali.csv')
        df4 = pd.read_csv('all_csv/Comedy.csv')
        df5 = pd.read_csv('all_csv/Documentary.csv')
        df6 = pd.read_csv('all_csv/Drama.csv')
        df7 = pd.read_csv('all_csv/English.csv')
        df8 = pd.read_csv('all_csv/Fantasy.csv')
        df9 = pd.read_csv('all_csv/Gujarati.csv')
        df10 = pd.read_csv('all_csv/Hindi.csv')
        df11 = pd.read_csv('all_csv/Horror.csv')
        df12 = pd.read_csv('all_csv/International.csv')
        df13 = pd.read_csv('all_csv/Kannada.csv')
        df14 = pd.read_csv('all_csv/Kids.csv')
        df15 = pd.read_csv('all_csv/Malayalam.csv')
        df16 = pd.read_csv('all_csv/Marathi.csv')
        df17 = pd.read_csv('all_csv/Music videos and concerts.csv')
        df18 = pd.read_csv('all_csv/Mystery and thrillers.csv')
        df19= pd.read_csv('all_csv/Punjabi.csv')
        df20 = pd.read_csv('all_csv/Romance.csv')
        df21 = pd.read_csv('all_csv/Tamil.csv')
        df22 = pd.read_csv('all_csv/Telugu.csv')
        main_df = pd.concat([df1,df2,df3,df4,df5,df6,df7,df8,df9,df10,df11,df12,df13,df14,df15,df16,df17,df18,df19,df20,df21,df22])
        return main_df
    
    # Get Coman Funtion for get top 5 movies using Rating
    def get_top_5(df):
        df = df.replace(to_replace="None", value=np.nan)
        df = df.dropna()
        sorted_data = df.sort_values(by='Imdb_rating', ascending=False)[0:4]
        return sorted_data

    # def Action():
    #     df = pd.read_csv('all_csv/Action and adventure.csv')
    #     top_5 = CSV_Manupilation.get_top_5(df)
    #     list_top_5 = top_5.values.tolist()
    #     # print(list_top_5)
    #     return list_top_5
    
    # def Anime():
    #     df = pd.read_csv('all_csv/Anime.csv')
    #     top_5 = CSV_Manupilation.get_top_5(df)
    #     list_top_5 = top_5.values.tolist()
    #     # print(list_top_5)
    #     return list_top_5
    
    # def Horror():
    #     df = pd.read_csv('all_csv/Horror.csv')
    #     top_5 = CSV_Manupilation.get_top_5(df)
    #     list_top_5 = top_5.values.tolist()
    #     # print(list_top_5)
    #     return list_top_5
    
    def get_gen_data(gen):
        df = pd.read_csv(f'all_csv/{gen}.csv')
        top_5 = CSV_Manupilation.get_top_5(df)
        list_top_5 = top_5.values.tolist()
        # print(list_top_5)
        return list_top_5


