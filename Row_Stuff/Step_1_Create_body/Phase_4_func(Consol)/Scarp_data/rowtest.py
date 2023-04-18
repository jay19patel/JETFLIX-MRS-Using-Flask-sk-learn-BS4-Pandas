import csv
import requests
from bs4 import BeautifulSoup
import time

color_set = ['BLACK', 'RED', 'GREEN', 'YELLOW', 'BLUE', 'MAGENTA', 'CYAN', 'WHITE']
no_of_lines, val, real_cnt = 100, 1, 0
headers = {
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/42.0.2311.135 Safari/537.36 Edge/12.246"}
target = 20
filename = "TopMoviesOfAllTime.csv"
start_index = 0  # last accessed movie is at 6379



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


def getActorsImages(link):
    req = requests.get(link, headers)
    soup = BeautifulSoup(req.text, 'html.parser')
    movie_actors_image = []
    cnt_actor = 5
    movie_actor = soup.findAll('div', attrs={'data-testid': 'title-cast-item'})
    for link in movie_actor:
        if cnt_actor >= 1:
            actor_image_link = "https://www.imdb.com" + str(link.find('a')['href'])
            req1 = requests.get(actor_image_link, headers)
            soup1 = BeautifulSoup(req1.text, 'html.parser')
            actor_image = soup1.find('div', attrs={'class': 'poster-hero-container'}).find('img')['src']
            movie_actors_image.append(actor_image)
            cnt_actor -= 1
    return movie_actors_image


def getPoster(link):
    req = requests.get(link, headers)
    soup = BeautifulSoup(req.text, 'html.parser')
    movie_poster_page_link = "https://www.imdb.com" + str(
        soup.find('div', attrs={'class': 'sc-910a7330-2 bmKajB'}).find('a', attrs={
            'class': 'ipc-lockup-overlay ipc-focusable'})['href'])
    req = requests.get(movie_poster_page_link, headers)
    soup = BeautifulSoup(req.text, 'html.parser')
    movie_poster = str(soup.find('div', attrs={'class': 'media-viewer'}).find('div', attrs={
        'class': 'sc-7c0a9e7c-2 bkptFa'}).img['src'])
    return movie_poster

def page_content_fetch(row, way):
    if way == "continous":
        global val, real_cnt
        left_pane = row.find('div', attrs={'class': 'lister-item-image float-left'})
        right_pane = row.find('div', attrs={'class': 'lister-item-content'})
        try:
            movie_id = left_pane.a.find('img', attrs={'class', 'loadlate'})['data-tconst']
            movie_link = "https://www.imdb.com/" + left_pane.find('a').attrs['href'] + "?ref_=adv_li_i"
            movie_poster = getPoster(movie_link)
            movie_name = right_pane.find('h3', attrs={'class': 'lister-item-header'}).find('a').text
            movie_year = right_pane.find('h3', attrs={'class': 'lister-item-header'}).find('span', attrs={
                'class': 'lister-item-year text-muted unbold'}).text[-5:-1]
            movie_genre = right_pane.find('p', attrs={'class': 'text-muted'}).find('span', attrs={
                'class': 'genre'}).text.strip()
            movie_rating = right_pane.find('div', attrs={'class': 'ratings-bar'}).find('strong').text
            movie_description = right_pane.findAll('p')[1].get_text(strip=True).replace(
                "...                See full summary\/xa0»", '.').replace("...See full summary»", '.')
            movie_director = right_pane.findAll('p')[2].a.text.strip()
            movie_actors = getActorsName(movie_link)
            movie_actors_image = getActorsImages(movie_link)
            writer_csv(
                [movie_id, movie_link, movie_poster, movie_name, movie_year, movie_genre, movie_rating,
                 movie_description, movie_director, movie_actors, movie_actors_image])
            real_cnt += 1
        finally:
            return
    elif way == "non-continous":
        left_pane = row.find('div', attrs={'class': 'lister-item-image ribbonize'})
        right_pane = row.find('div', attrs={'class': 'lister-item-content'})
        try:
            movie_id = left_pane.a.find('img', attrs={'class', 'loadlate'})['data-tconst']
            # print(movie_id)
            movie_link = "https://www.imdb.com/" + left_pane.find('a').attrs['href'] + "?ref_=adv_li_i"
            # print(movie_link)
            movie_poster = getPoster(movie_link)
            # print(movie_poster)
            movie_name = right_pane.find('h3', attrs={'class': 'lister-item-header'}).find('a').text
            # print(movie_name)
            movie_year = right_pane.find('h3', attrs={'class': 'lister-item-header'}).find('span', attrs={
                'class': 'lister-item-year text-muted unbold'}).text[-5:-1]
            # print(movie_year)
            movie_genre = right_pane.find('p', attrs={'class': 'text-muted'}).find('span', attrs={
                'class': 'genre'}).text.strip()
            # print(movie_genre)
            movie_rating = right_pane.find('div', attrs={'class': 'ipl-rating-widget'}).find('span', attrs={'class': 'ipl-rating-star__rating'}).text
            # print(movie_rating)
            movie_description = right_pane.findAll('p')[1].get_text(strip=True).replace(
                "...                See full summary\/xa0»", '.').replace("...See full summary»", '.')
            # print(movie_description)
            movie_director = right_pane.findAll('p')[2].a.text.strip()
            # print(movie_director)
            movie_actors = getActorsName(movie_link)
            # print(movie_actors)
            movie_actors_image = getActorsImages(movie_link)
            # print(movie_actors_image)
            # print("--------------------------------------------------------------------------------------------------------------------------------------------------")
            writer_csv(
                [movie_id, movie_link, movie_poster, movie_name, movie_year, movie_genre, movie_rating,
                 movie_description, movie_director, movie_actors, movie_actors_image])
        finally:
            return


def extract(way):
    if way == "continous":
        for i in range(start_index, target, 50):
            start = time.time()
            url = "https://www.imdb.com/search/title/?title_type=feature&year=2009-12-31,2023-01-01&sort=num_votes,desc&start=" + str(
                i) + "&ref_=adv_nxt"
            req = requests.get(url, headers)
            soup = BeautifulSoup(req.text, 'html.parser')
            movie_data = soup.findAll('div', attrs={'class': 'lister-item mode-advanced'})
            for row in movie_data:
                page_content_fetch(row, way)
            end = time.time()
            hrs, rest = divmod(end - start, 3600)
            mins, secs = divmod(rest, 60)
    elif way == "non-continous":
        url = "https://www.imdb.com/list/ls085268948/?sort=moviemeter,asc&st_dt=&mode=detail&page=1"
        req = requests.get(url, headers)
        soup = BeautifulSoup(req.text, 'html.parser')
        movie_data = soup.findAll('div', attrs={'class': 'lister-item mode-detail'})
        for row in movie_data:
            page_content_fetch(row, way)



