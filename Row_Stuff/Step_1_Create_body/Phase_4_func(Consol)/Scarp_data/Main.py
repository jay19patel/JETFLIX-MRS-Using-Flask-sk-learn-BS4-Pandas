import csv
import requests
from bs4 import BeautifulSoup
import time


filename = "TopMoviesOfAllTime.csv" 
headers = {
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/42.0.2311.135 Safari/537.36 Edge/12.246"}

def initialize_csv():
    csvwriter = csv.writer(open(filename, 'w', newline="", encoding='utf-8'))
    csvwriter.writerow(['Movie ID', 'Movie Link', 'Movie Poster', 'Movie Name', 'Movie Year', 'Movie Genre',
                        'Movie Rating', 'Movie Description', 'Movie Director', 'Movie Actors', 'Movie_Actors_Image'])
def writer_csv(record):
    csvwriter = csv.writer(open(filename, 'a', newline="", encoding='utf-8'))
    csvwriter.writerow(record)


def getActorsName(link):
    req = requests.get(link, headers)
    soup = BeautifulSoup(req.text, 'html.parser')
    movie_actors = []
    cnt_actor = 5
    movie_actor = soup.findAll('div', attrs={'data-testid': 'title-cast-item'})
    for actor in movie_actor:
        if cnt_actor >= 1:
            actor_name = actor.find('a')['aria-label']
            movie_actors.append(actor_name)
            cnt_actor -= 1
    return movie_actors