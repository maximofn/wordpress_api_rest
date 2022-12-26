from domain import domain

class wordpress_json():
    def __init__(self, \
            post_id, post_title, post_slug, post_content, post_excerpt, post_categories, post_tags, \
            domain_url, \
            date, date_modified, \
            author_id=1, author_name = 'Maximo FN', \
            image_id=0, \
            post_comment_status = 'closed', post_ping_status = 'closed', post_sticky = False, \
            post_template = '', post_format = 'standard', post_meta = [], \
            robots = 'index, follow'
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
        # Domain data
        self.domain_url = domain_url
        self.domain = domain(domain_url)
        # Date data
        self.date = date
        self.date_modified = date_modified
        # Author data
        self.author_id = author_id
        self.author_name = author_name
        # Image data
        self.image_id = image_id
        # Robots data
        self.robots = robots

    def json(self):
        return {
            'id': self.post_id,
            'date': self.date,
            'date_gmt': self.date,
            'guid': f"{self.domain_url}/?p={self.post_id}",
            'modified': self.date,
            'modified_gmt': self.date_modified,
            'slug': self.post_slug,
            'status': 'publish',
            'type': 'post',
            'link': f"{self.domain_url}/{self.post_slug}",
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
            'blocksy_meta': self.json_blocksy_meta(),
            'yoast_head': self.json_yoast_head(),
            'yoast_head_json': self.yoast_head_json(),
            '_links': self.links(),
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
                'version': []
            }
        }
    
    def json_yoast_head(self):
        return f'''<!-- This site is optimized with the Yoast SEO plugin v19.13 - https://yoast.com/wordpress/plugins/seo/ -->
<title>{self.post_title} - {self.author_name}</title>
<meta name="description" content="{self.post_excerpt}" />
<meta name="robots" content="{self.robots}, max-snippet:-1, max-image-preview:large, max-video-preview:-1" />
<link rel="canonical" href="https://maximofn.com/terminal/" />
<meta property="og:locale" content="es_ES" />
<meta property="og:type" content="article" />
<meta property="og:title" content="Terminal - Maximo FN" />
<meta property="og:description" content="{self.post_excerpt}" />
<meta property="og:url" content="https://maximofn.com/terminal/" />
<meta property="og:site_name" content="Maximo FN" />
<meta property="article:published_time" content="2022-12-12T06:39:35+00:00" />
<meta property="article:modified_time" content="2022-12-12T06:39:37+00:00" />
<meta property="og:image" content="https://maximofn.com/wp-content/uploads/2022/12/terminal.jpg" />
	<meta property="og:image:width" content="1000" />
	<meta property="og:image:height" content="600" />
	<meta property="og:image:type" content="image/jpeg" />
<meta name="author" content="admin" />
<meta name="twitter:card" content="summary_large_image" />
<meta name="twitter:label1" content="Escrito por" />
	<meta name="twitter:data1" content="admin" />
	<meta name="twitter:label2" content="Tiempo de lectura" />
	<meta name="twitter:data2" content="100 minutos" />
<script type="application/ld+json" class="yoast-schema-graph">{"@context":"https://schema.org","@graph":[{"@type":"WebPage","@id":"https://maximofn.com/terminal/","url":"https://maximofn.com/terminal/","name":"Terminal - Maximo FN","isPartOf":{"@id":"https://maximofn.com/#website"},"datePublished":"2022-12-12T06:39:35+00:00","dateModified":"2022-12-12T06:39:37+00:00","author":{"@id":"https://maximofn.com/#/schema/person/0ea0528f95bec67b9271c68d5a300aed"},"description":"🟢 Siéntete como un verdadero hacker 🖥 sabiéndolo todo sobre la terminal 💻. Entra y comienza a manejar ⌨ la terminal como un profesional","breadcrumb":{"@id":"https://maximofn.com/terminal/#breadcrumb"},"inLanguage":"es","potentialAction":[{"@type":"ReadAction","target":["https://maximofn.com/terminal/"]}]},{"@type":"BreadcrumbList","@id":"https://maximofn.com/terminal/#breadcrumb","itemListElement":[{"@type":"ListItem","position":1,"name":"Portada","item":"https://maximofn.com/"},{"@type":"ListItem","position":2,"name":"Terminal"}]},{"@type":"WebSite","@id":"https://maximofn.com/#website","url":"https://maximofn.com/","name":"Maximo FN","description":"Web de Maximo FN","potentialAction":[{"@type":"SearchAction","target":{"@type":"EntryPoint","urlTemplate":"https://maximofn.com/?s={search_term_string}"},"query-input":"required name=search_term_string"}],"inLanguage":"es"},{"@type":"Person","@id":"https://maximofn.com/#/schema/person/0ea0528f95bec67b9271c68d5a300aed","name":"admin","image":{"@type":"ImageObject","inLanguage":"es","@id":"https://maximofn.com/#/schema/person/image/","url":"https://secure.gravatar.com/avatar/d42cd1341d871ab6d87a2ac338ae6f60?s=96&d=mm&r=g","contentUrl":"https://secure.gravatar.com/avatar/d42cd1341d871ab6d87a2ac338ae6f60?s=96&d=mm&r=g","caption":"admin"},"sameAs":["https://maximofn.com"]}]}</script>
<!-- / Yoast SEO plugin. -->'''
    
    def yoast_head_json(self):
        return ''

    def links(self):
        return ''