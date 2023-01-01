class wordpress_json():
    def __init__(self, \
            post_id, post_title, post_slug, post_content, post_excerpt, post_categories, post_tags, \
            domain_url, image_url, image_width, image_height, image_type, \
            date, date_modified, date_gmt, \
            author_id=1, author_name = 'Maximo FN', author_description = 'Web de Maximo FN', \
            image_id=0, \
            post_comment_status = 'closed', post_ping_status = 'closed', post_sticky = False, \
            post_template = '', post_format = 'standard', post_meta = [], post_time_to_read = 0, \
            robots = 'index, follow', post_language = 'es_ES'
        ):
        # Post data
        self.post_id = post_id
        self.post_title = post_title
        self.post_slug = post_slug
        self.post_content = post_content
        self.post_excerpt = post_excerpt
        self.post_comment_status = post_comment_status
        self.post_ping_status = post_ping_status
        self.post_sticky = post_sticky
        self.post_template = post_template
        self.post_format = post_format
        self.post_meta = post_meta
        self.post_categories = post_categories
        self.post_tags = post_tags
        self.post_language = post_language
        self.post_time_to_read = post_time_to_read
        # Domain data
        self.domain_url = domain_url
        # Date data
        self.date = date
        self.date_modified = date_modified
        self.date_gmt = date_gmt
        # Author data
        self.author_id = author_id
        self.author_name = author_name
        self.author_description = author_description
        # Image data
        self.image_id = image_id
        self.image_url = image_url
        self.image_width = image_width
        self.image_height = image_height
        self.image_type = image_type
        # Robots data
        self.robots = robots
        # Special characters
        self.special_character1 = "{"
        self.special_character2 = "}"
        self.special_character3 = "["
        self.special_character4 = "]"

    def json(self):
        return {
            'id': self.post_id,
            'date': self.date,
            'date_gmt': self.date,
            'guid': {
                'rendered':f"{self.domain_url}/?p={self.post_id}",
            },
            'modified': self.date_modified,
            'modified_gmt': self.date_modified,
            'slug': self.post_slug,
            'status': 'publish',
            'type': 'post',
            'link': f"{self.domain_url}/{self.post_slug}/",
            'title': {
                'rendered': self.post_title
            },
            'content': {
                'rendered': self.post_content,
                'protected': False
            },
            'excerpt': {
                'rendered': f'<p>{self.post_excerpt}</p>\n',
                'protected': False
            },
            'author': self.author_id,
            'featured_media': self.image_id,
            'comment_status': self.post_comment_status,
            'ping_status': self.post_ping_status,
            'sticky': self.post_sticky,
            'template': self.post_template,
            'format': self.post_format,
            'meta': self.post_meta,
            'categories': self.post_categories,
            'tags': self.post_tags,
            # 'blocksy_meta': self.json_blocksy_meta(),
            # 'yoast_head': self.json_yoast_head(),
            # 'yoast_head_json': self.yoast_head_json(),
            # '_links': self.links(),
        }
    
    def json_blocksy_meta(self):
        return {
            'styles_descriptor': {
                'styles': {
                    'desktop': '',
                    'tablet': '',
                    'mobile': ''
                },
                'google_fonts': [],
                'version': 5
            }
        }
    
    def json_yoast_head(self):
        return f'''<!-- This site is optimized with the Yoast SEO plugin v19.13 - https://yoast.com/wordpress/plugins/seo/ -->
<title>{self.post_title} - {self.author_name}</title>
<meta name="description" content="{self.post_excerpt}" />
<meta name="robots" content="{self.robots}, max-snippet:-1, max-image-preview:large, max-video-preview:-1" />
<link rel="canonical" href="{self.domain_url}/{self.post_slug}/" />
<meta property="og:locale" content="{self.post_language}" />
<meta property="og:type" content="article" />
<meta property="og:title" content="{self.post_title} - {self.author_name}" />
<meta property="og:description" content="{self.post_excerpt}" />
<meta property="og:url" content="{self.domain_url}/{self.post_slug}/" />
<meta property="og:site_name" content="{self.author_name}" />
<meta property="article:published_time" content="{self.date}+00:00" />
<meta property="article:modified_time" content="{self.date_modified}+00:00" />
<meta property="og:image" content="{self.image_url}" />
	<meta property="og:image:width" content="{self.image_width}" />
	<meta property="og:image:height" content="{self.image_height}" />
	<meta property="og:image:type" content="{self.image_type}" />
<meta name="author" content="admin" />
<meta name="twitter:card" content="summary_large_image" />
<meta name="twitter:label1" content="Escrito por" />
	<meta name="twitter:data1" content="admin" />
	<meta name="twitter:label2" content="Tiempo de lectura" />
	<meta name="twitter:data2" content="{self.post_time_to_read} minutos" />
<script type="application/ld+json" class="yoast-schema-graph">{self.special_character1}"@context":"https://schema.org","@graph":{self.special_character3}{self.special_character1}"@type":"WebPage","@id":"{self.domain_url}/{self.post_slug}/","url":"{self.domain_url}/{self.post_slug}/","name":"{self.post_title} - {self.author_name}","isPartOf":{self.special_character1}"@id":"{self.domain_url}/#website"{self.special_character2},"datePublished":"{self.date}+00:00","dateModified":"{self.date_modified}+00:00","author":{self.special_character1}"@id":"{self.domain_url}/#/schema/person/0ea0528f95bec67b9271c68d5a300aed"{self.special_character2},"description":"{self.post_excerpt}","breadcrumb":{self.special_character1}"@id":"{self.domain_url}/{self.post_slug}/#breadcrumb"{self.special_character2},"inLanguage":"{self.post_language[0:2]}","potentialAction":{self.special_character3}{self.special_character1}"@type":"ReadAction","target":{self.special_character3}"{self.domain_url}/{self.post_slug}/"{self.special_character4}{self.special_character2}{self.special_character4}{self.special_character2},{self.special_character1}"@type":"BreadcrumbList","@id":"{self.domain_url}/{self.post_slug}/#breadcrumb","itemListElement":{self.special_character3}{self.special_character1}"@type":"ListItem","position":1,"name":"Portada","item":"{self.domain_url}/"{self.special_character2},{self.special_character1}"@type":"ListItem","position":2,"name":"{self.post_title}"{self.special_character2}{self.special_character4}{self.special_character2},{self.special_character1}"@type":"WebSite","@id":"{self.domain_url}/#website","url":"{self.domain_url}/","name":"{self.author_name}","description":"Web de {self.author_name}","potentialAction":{self.special_character3}{self.special_character1}"@type":"SearchAction","target":{self.special_character1}"@type":"EntryPoint","urlTemplate":"{self.domain_url}/?s={self.special_character1}search_term_string{self.special_character2}"{self.special_character2},"query-input":"required name=search_term_string"{self.special_character2}{self.special_character4},"inLanguage":"{self.post_language[0:2]}"{self.special_character2},{self.special_character1}"@type":"Person","@id":"{self.domain_url}/#/schema/person/0ea0528f95bec67b9271c68d5a300aed","name":"admin","image":{self.special_character1}"@type":"ImageObject","inLanguage":"{self.post_language[0:2]}","@id":"{self.domain_url}/#/schema/person/image/","url":"https://secure.gravatar.com/avatar/d42cd1341d871ab6d87a2ac338ae6f60?s=96&d=mm&r=g","contentUrl":"https://secure.gravatar.com/avatar/d42cd1341d871ab6d87a2ac338ae6f60?s=96&d=mm&r=g","caption":"admin"{self.special_character2},"sameAs":{self.special_character3}"{self.domain_url}"{self.special_character4}{self.special_character2}{self.special_character4}{self.special_character2}</script>
<!-- / Yoast SEO plugin. -->'''
    
    def yoast_head_json(self):
        return {
            "title": f"{self.post_title} - {self.author_name}",
            "description": self.post_excerpt,
            "robots": {
                "index": self.robots.split(', ')[0],
                "follow": self.robots.split(', ')[1],
                "max-snippet": "max-snippet:-1",
                "max-image-preview": "max-image-preview:large",
                "max-video-preview": "max-video-preview:-1"
            },
            "canonical": f"{self.domain_url}/{self.post_slug}/",
            "og_locale": self.post_language,
            "og_type": "article",
            "og_title": f"{self.post_title} - {self.author_name}",
            "og_description": self.post_excerpt,
            "og_url": f"{self.domain_url}/{self.post_slug}/",
            "og_site_name": self.author_name,
            "article_published_time": f"{self.date}+00:00",
            "article_modified_time": f"{self.date_modified}+00:00",
            "og_image": [
                {
                    "width": self.image_width,
                    "height": self.image_height,
                    "url": self.image_url,
                    "type": self.image_type
                }
            ],
            "author": "admin",
            "twitter_card": "summary_large_image",
            "twitter_misc": {
                "Escrito por": "admin",
                "Tiempo de lectura": f"{self.post_time_to_read} minutos"
            },
            "schema": {
                "@context": "https://schema.org",
                "@graph": [
                    {
                        "@type": "WebPage",
                        "@id": f"{self.domain_url}/{self.post_slug}/",
                        "url": f"{self.domain_url}/{self.post_slug}/",
                        "name": f"{self.post_title} - {self.author_name}",
                        "isPartOf": {
                            "@id": f"{self.domain_url}/#website"
                        },
                        "datePublished": f"{self.date}+00:00",
                        "dateModified": f"{self.date_modified}+00:00",
                        "author": {
                            "@id": f"{self.domain_url}/#/schema/person/0ea0528f95bec67b9271c68d5a300aed"
                        },
                        "description": self.post_excerpt,
                        "breadcrumb": {
                            "@id": f"{self.domain_url}/{self.post_slug}/#breadcrumb"
                        },
                        "inLanguage": self.post_language[0:2],
                        "potentialAction": [
                            {
                                "@type": "ReadAction",
                                "target": [
                                    f"{self.domain_url}/{self.post_slug}/"
                                ]
                            }
                        ],
                    },
                    {
                        "@type": "BreadcrumbList",
                        "@id": f"{self.domain_url}/{self.post_slug}/#breadcrumb",
                        "itemListElement": [
                            {
                                "@type": "ListItem",
                                "position": 1,
                                "name": "Portada",
                                "item": f"{self.domain_url}/"
                            },
                            {
                                "@type": "ListItem",
                                "position": 2,
                                "name": self.post_title,
                            }
                        ]
                    },
                    {
                        "@type": "WebSite",
                        "@id": f"{self.domain_url}/#website",
                        "url": f"{self.domain_url}/",
                        "name": self.author_name,
                        "description": self.author_description,
                        "potentialAction": [
                            {
                                "@type": "SearchAction",
                                "target": {
                                    "@type": "EntryPoint",
                                    "urlTemplate": f"{self.domain_url}/?s={{search_term_string}}"
                                },
                                "query-input": "required name=search_term_string"
                            },
                        ],
                        "inLanguage": self.post_language[0:2]
                    },
                    {
                        "@type": "Person",
                        "@id": f"{self.domain_url}/#/schema/person/0ea0528f95bec67b9271c68d5a300aed",
                        "name": "admin",
                        "image": {
                            "@type": "ImageObject",
                            "inLanguage": self.post_language[0:2],
                            "@id": f"{self.domain_url}/#/schema/person/image/",
                            "url": f"https://secure.gravatar.com/avatar/d42cd1341d871ab6d87a2ac338ae6f60?s=96&d=mm&r=g",
                            "contentUrl": f"https://secure.gravatar.com/avatar/d42cd1341d871ab6d87a2ac338ae6f60?s=96&d=mm&r=g",
                            "caption": "admin"
                        },
                        "sameAs": [f"{self.domain_url}",]
                    }
                ]
            }
        }

    def links(self):
        return {
            "self": [
                {
                    "href": f"{self.domain_url}/wp-json/wp/v2/posts/{self.post_id}"
                }
            ],
            "collection": [
                {
                    "href": f"{self.domain_url}/wp-json/wp/v2/posts"
                }
            ],
            "about": [
                {
                    "href": f"{self.domain_url}/wp-json/wp/v2/types/post"
                }
            ],
            "author": [
                {
                    "embeddable": True,
                    "href": f"{self.domain_url}/wp-json/wp/v2/users/1"
                }
            ],
            "replies": [
                {
                    "embeddable": True,
                    "href": f"{self.domain_url}/wp-json/wp/v2/comments?post={self.post_id}"
                }
            ],
            "version-history": [
                {
                    "count": None,#2,
                    "href": None,#f"{self.domain_url}/wp-json/wp/v2/posts/{self.post_id}/revisions"
                }
            ],
            "predecessor-version": [
                {
                    "id": None,#785,
                    "href": None,#f"{self.domain_url}/wp-json/wp/v2/posts/{self.post_id}/revisions/785"
                }
            ],
            "wp:featuredmedia": [
                {
                    "embeddable": True,
                    "href": f"{self.domain_url}/wp-json/wp/v2/media/{self.image_id}"
                }
            ],
            "wp:attachment": [
                {
                    "href": f"{self.domain_url}/wp-json/wp/v2/media?parent={self.post_id}"
                }
            ],
            "wp:term": [
                {
                    "taxonomy": "category",
                    "embeddable": True,
                    "href": f"{self.domain_url}/wp-json/wp/v2/categories?post={self.post_id}"
                },
                {
                    "taxonomy": "post_tag",
                    "embeddable": True,
                    "href": f"{self.domain_url}/wp-json/wp/v2/tags?post={self.post_id}"
                }
            ],
            "curies": [
                {
                    "name": "wp",
                    "href": f"https://api.w.org/{self.special_character1}rel{self.special_character2}",
                    "templated": True
                }
            ]
        }