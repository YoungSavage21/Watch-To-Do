import requests
import json

headers = {
        "accept": "application/json",
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJkMmRlNjMzNzFmYjZlN2UzZTVlNmY5MmNjNWQ2OGMwNCIsInN1YiI6IjY0ZDAwYjBiMzAzYzg1MDExZGQ0M2Y2ZiIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.N-NqU3VCNq4e7zV_i-DenutCn1lKGRQacrlzjpe9SZw"
    }

def search_result(s, p):
    url = f"https://api.themoviedb.org/3/search/movie?query={s}&include_adult=false&language=en-US&page={p}"
    response = requests.get(url, headers=headers)
    data = json.loads(response.text)
    return data

def get_detail(q):
    url = "https://api.themoviedb.org/3/movie/" + q + "?language=en-US"
    response = requests.get(url, headers=headers)
    results = json.loads(response.text)
    return results

def get_top_rated():
    url = "https://api.themoviedb.org/3/movie/top_rated?language=en-US&page=1"
    response = requests.get(url, headers=headers)
    results = json.loads(response.text)
    return results["results"]

def get_upcoming():
    url = "https://api.themoviedb.org/3/movie/upcoming?language=en-US&page=1"
    response = requests.get(url, headers=headers)
    results = json.loads(response.text)
    return results["results"]

def get_trending():
    url = "https://api.themoviedb.org/3/trending/movie/day?language=en-US"
    response = requests.get(url, headers=headers)
    results = json.loads(response.text)
    return results["results"]

def get_popular():
    url = "https://api.themoviedb.org/3/movie/popular?language=en-US&page=1"
    response = requests.get(url, headers=headers)
    results = json.loads(response.text)
    return results["results"]

def get_now_playing():
    url = "https://api.themoviedb.org/3/movie/now_playing?language=en-US&page=1"
    response = requests.get(url, headers=headers)
    results = json.loads(response.text)
    return results["results"]

def insert_list(detail, li):
    
    if len(detail['genres']) >= 2:
        genres = detail['genres'][0]['name'] + ", " + detail['genres'][1]['name']
    elif len(detail['genres']) == 1:
        genres = detail['genres'][0]['name']
    else:
        genres = "No data"

    if not detail['release_date']:
        detail['release_date'] = "No data"

    li.execute("INSERT or REPLACE INTO list (movie_id, title, year, name, rating) VALUES (?, ?, ?, ?, ?)", detail['id'], detail['title'], detail['release_date'], genres , detail['vote_average'])
   


