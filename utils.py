import requests
from datetime import date, datetime, timedelta
import time
from credentials import PASSWORD, url, USER_NAME

url_pages = url + "wp-json/wp/v2/pages"
url_posts = url + "wp-json/wp/v2/posts"

def get_pages():
    request = requests.get(url_pages)
    request_json = request.json()
    
    pages = []
    for i in range(len(request_json)):
        dictionary = {
            "id": request_json[i]["id"],
            "title": request_json[i]["title"]["rendered"],
        }
        pages.append(dictionary)
    pages.sort(key=lambda x: x["id"])

    return pages

def get_posts():
    request = requests.get(url_posts)
    request_json = request.json()
    
    posts = []
    for i in range(len(request_json)):
        dictionary = {
            "id": request_json[i]["id"],
            "title": request_json[i]["title"]["rendered"],
        }
        posts.append(dictionary)
    posts.sort(key=lambda x: x["id"])

    return posts

def get_last_page():
    pages = get_pages()
    return pages[-1]

def get_last_post():
    posts = get_posts()
    return posts[-1]

def get_last_id_page():
    last_page = get_last_page()
    return last_page["id"]

def get_last_id_post():
    last_post = get_last_post()
    return last_post["id"]

def timedate(hours_delta = 5, time_delta = 0):
    today = date.today()
    now = datetime.now() - timedelta(hours=hours_delta)
    if now.hour + hours_delta > 23:
        today = today - timedelta(days=1)
    page_date = f'{today}T{now.hour:02d}:{now.minute:02d}:{now.second:02d}'
    time.sleep(time_delta)
    now = datetime.now()
    page_date_modified = f'{today}T{now.hour:02d}:{now.minute:02d}:{now.second:02d}'
    time.sleep(time_delta)
    now = datetime.now()
    page_date_modified_gmt = f'{today}T{now.hour:02d}:{now.minute:02d}:{now.second:02d}'
    return page_date, page_date_modified, page_date_modified_gmt