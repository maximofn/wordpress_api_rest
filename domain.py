import requests

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
