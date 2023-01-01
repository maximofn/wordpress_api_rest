import requests
import base64
from credentials import PASSWORD, url, USER_NAME
from wordpress_json import wordpress_json
from utils import timedate
import json

class domain():
    def __init__(self, url):
        self.url = url
        self.url_pages = url + "wp-json/wp/v2/pages?per_page=100"
        self.url_pages_simplified = url + "wp-json/wp/v2/pages"
        self.url_posts = url + "wp-json/wp/v2/posts?per_page=100"
        self.url_posts_simplified = url + "wp-json/wp/v2/posts"
        self.url_media = url + "wp-json/wp/v2/media?per_page=100"
        self.url_media_simplified = url + "wp-json/wp/v2/media"
        self.url_categories = url + "wp-json/wp/v2/categories?per_page=100"
        self.url_categories_simplified = url + "wp-json/wp/v2/categories"
        self.url_tags = url + "wp-json/wp/v2/tags?per_page=100"
        self.url_tags_simplified = url + "wp-json/wp/v2/tags"
        pass

    def get_credetial_header(self):
        credentials = USER_NAME + ':' + PASSWORD
        token = base64.b64encode(credentials.encode())
        header = {'Authorization': 'Basic ' + token.decode('utf-8')}
        return header

    def get_pages(self):
        request = requests.get(self.url_pages)
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
    
    def get_json_page(self, id):
        request = requests.get(self.url_pages_simplified + f"/{id}")
        request_json = request.json()
        return request_json
    
    def get_last_page(self):
        pages = self.get_pages()
        return pages[-1]
    
    def get_posts(self):
        request = requests.get(self.url_posts)
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
    
    def get_json_post(self, id):

        request = requests.get(self.url_posts_simplified + f"/{id}")
        request_json = request.json()
        return request_json
    
    def get_last_post(self):
        posts = self.get_posts()
        return posts[-1]
    
    def to_serializable(self, obj):
        if isinstance(obj, (list, tuple)):
            return [self.to_serializable(item) for item in obj]
        elif isinstance(obj, dict):
            return {key: self.to_serializable(value) for key, value in obj.items()}
        elif hasattr(obj, "__dict__"):
            return {key: self.to_serializable(value) for key, value in obj.__dict__.items()}
        else:
            return obj

    def upload_post(self, \
            post_id, post_title, post_slug, post_content, post_excerpt, post_categories, post_tags, \
            domain_url, image_url, image_width, image_height, image_type, \
            author_id=1, author_name = 'Maximo FN', author_description = 'Web de Maximo FN', \
            image_id=0, \
            post_comment_status = 'closed', post_ping_status = 'closed', post_sticky = False, \
            post_template = '', post_format = 'standard', post_meta = [], post_time_to_read = 0, \
            robots = 'index, follow', post_language = 'es_ES'
        ):
        date = timedate()
        wp_json_ = wordpress_json(post_id=post_id, post_title=post_title, post_slug=post_slug, 
            post_content=post_content, post_excerpt=post_excerpt, post_categories=post_categories, 
            post_tags=post_tags, domain_url=domain_url, image_url=image_url, image_width=image_width, 
            image_height=image_height, image_type=image_type, date=date['page_date'], date_modified=date['page_date_modified'], 
            date_gmt=date['page_date'], author_id=author_id, author_name=author_name, 
            author_description=author_description, image_id=image_id, post_comment_status=post_comment_status, 
            post_ping_status=post_ping_status, post_sticky=post_sticky, post_template=post_template, 
            post_format=post_format, post_meta=post_meta, post_time_to_read=post_time_to_read, robots=robots, 
            post_language=post_language)
        wp_json_ = json.dumps(self.to_serializable(wp_json_))
        header = self.get_credetial_header()
        response = requests.post(self.url_posts_simplified, json=wp_json_, headers=header).json()
        if 'id' in response:
            return response['id']
        else:
            return 0
    
    def get_medios(self):
        request = requests.get(self.url_media)
        request_json = request.json()

        medios = []
        for i in range(len(request_json)):
            dictionary = {
                "id": request_json[i]["id"],
                "title": request_json[i]["title"]["rendered"],
            }
            medios.append(dictionary)

        return medios
    
    def get_json_medio(self, id):
        request = requests.get(self.url_media_simplified + f"/{id}")
        request_json = request.json()
        return request_json
    
    def get_last_medio(self):
        last_page = self.get_last_page()
        return last_page[-1]
    
    def get_categories(self):
        request = requests.get(self.url_categories)
        request_json = request.json()

        categories = []
        for i in range(len(request_json)):
            dictionary = {
                "id": request_json[i]["id"],
                "name": request_json[i]["name"],
            }
            categories.append(dictionary)

        return categories
    
    def get_json_category(self, id):
        request = requests.get(self.url_categories_simplified + f"/{id}")
        request_json = request.json()
        return request_json

    def get_last_category(self):
        last_category = self.get_last_category()
        return last_category[-1]
    
    def get_tags(self):
        request = requests.get(self.url_tags)
        request_json = request.json()

        tags = []
        for i in range(len(request_json)):
            dictionary = {
                "id": request_json[i]["id"],
                "name": request_json[i]["name"],
            }
            tags.append(dictionary)

        return tags
    
    def get_json_tag(self, id):
        request = requests.get(self.url_tags_simplified + f"/{id}")
        request_json = request.json()
        return request_json

    def get_last_tag(self):
        last_tag = self.get_last_tag()
        return last_tag[-1]
