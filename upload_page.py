import requests
import base64
from credentials import PASSWORD, url, USER_NAME
from utils import timedate

# Configure token and headers
url_pages = url + "wp-json/wp/v2/pages"
credentials = USER_NAME + ':' + PASSWORD
token = base64.b64encode(credentials.encode())
header = {'Authorization': 'Basic ' + token.decode('utf-8')}

def create_json(page_title, page_slug, page_body, page_read_time, page_user, page_image_icon, page_languaje):
    # id = get_last_id_page() + 1
    title = page_title
    content = page_body
    author = 1
    featured_media = 0
    parent = 0
    menu_order = 0
    comment_status = "closed"
    ping_status = "closed"
    template = ""
    meta = []

    # date 
    print("\tGet timedate")
    date, date_modified, date_modified_gmt = timedate()

    # guid
    # guid = {
    #     "rendered": f'{rendered_url}?page_id={id}',
    # }

    # excerpt
    print("\tExcerpt")
    excerpt = {
        'rendered':page_body,
        'protected':False,
    }

    # page_blocksy_meta
    print("\tPage blocksy meta")
    page_blocksy_meta = {
        'styles_descriptor': 
        {
            'styles': 
            {
                'desktop':'',
                'tablet':'',
                'mobile':''
            },
            'google_fonts':[],
            'version':5,
        },
    }

    # yoast
    print("\tYoast")
    yoast_title = f"{title} - {page_user}"
    yoast_user = page_user
    yoast_page_description = f"{page_user} website"
    yoast_image_url = page_image_icon
    yoast_read_time_units = "minutes" if page_read_time > 1 else "minute"
    yoast_name = "description"
    yoast_content = "Cuerpo"
    yoast_language = page_languaje
    yoast_in_language = page_languaje[:3]
    yoast_url = url + page_slug + "/"
    yoast_site_name = "Maximo FN"
    yoast_time_read = f'{page_read_time}'

    # yoast head
    print("\tYoast head")
    yoast_head = """
    <!-- This site is optimized with the Yoast SEO plugin v19.6.1 - https://yoast.com/wordpress/plugins/seo/ -->
    <title>%s</title>
    <meta name="description" content="%s" />
    <meta name="robots" content="noindex, follow, max-snippet:-1, max-image-preview:large, max-video-preview:-1" />
    <meta property="og:locale" content="%s" />
    <meta property="og:type" content="article" />
    <meta property="og:title" content="%s" />
    <meta property="og:description" content="%s" />
    <meta property="og:url" content="%s%s/" />
    <meta property="og:site_name" content="%s" />
    <meta property="article:modified_time" content="%s+00:00" />
    <meta property="og:image" content="%s" />
    <meta name="twitter:card" content="summary_large_image" />
    <meta name="twitter:label1" content="Tiempo de lectura" />
        <meta name="twitter:data1" content="%d %s" />
    <script type="application/ld+json" class="yoast-schema-graph">{"@context":"https://schema.org","@graph":[{"@type":"WebPage","@id":"%s%s","url":"%s%s","name":"%s","isPartOf":{"@id":"%s#website"},"datePublished":"%s+00:00","dateModified":"%s+00:00","description":"%s","breadcrumb":{"@id":"%s%s#breadcrumb"},"inLanguage":"%s","potentialAction":[{"@type":"ReadAction","target":["%s%s"]}]},{"@type":"BreadcrumbList","@id":"%s%s/#breadcrumb","itemListElement":[{"@type":"ListItem","position":1,"name":"Portada","item":"%s"},{"@type":"ListItem","position":2,"name":"%s"}]},{"@type":"WebSite","@id":"%s#website","url":"%s","name":"%s","description":"%s","potentialAction":[{"@type":"SearchAction","target":{"@type":"EntryPoint","urlTemplate":"%s?s={search_term_string}"},"query-input":"required name=search_term_string"}],"inLanguage":"%s"}]}</script>
    <!-- / Yoast SEO plugin. -->
    """ % (yoast_title, yoast_name, yoast_language, yoast_title, 
    yoast_name, url, page_title, yoast_user, date, yoast_image_url, 
    page_read_time, yoast_read_time_units,
    url, page_title, url, page_title, yoast_title, url, date, date_modified, 
    yoast_name, url, page_title, yoast_in_language, url, page_title, url, page_title,
    url, page_title, url, url, yoast_user, yoast_page_description, url,
    yoast_in_language)

    # yoast json
    print("\tYoast json")
    yoast_head_json = {
        "title":yoast_title,
        "description":yoast_content,
        "robots":
        {
            "index":"noindex",
            "follow":"follow",
            "max-snippet":"max-snippet:-1",
            "max-image-preview":"max-image-preview:large",
            "max-video-preview":"max-video-preview:-1"
        },
        "og_locale":yoast_language,
        "og_type":"article",
        "og_title":yoast_title,
        "og_description":yoast_content,
        "og_url":yoast_url,
        "og_site_name":yoast_site_name,
        "article_modified_time":f"{date_modified}+00:00",
        "twitter_card":"summary_large_image",
        "twitter_misc":
        {
            "Tiempo de lectura":yoast_time_read,
        },
        "schema":
        {
            "@context":"https://schema.org",
            "@graph":
            [
                {
                    "@type":"WebPage",
                    "@id":yoast_url,
                    "url":yoast_url,
                    "name":yoast_title,
                    "isPartOf":
                    {
                        f"@id":"{url}#website"
                    },
                    "datePublished":f"{date}+00:00",
                    "dateModified":f"{date_modified}+00:00",
                    "description":yoast_content,
                    "breadcrumb":
                    {
                        "@id":f"{yoast_url}#breadcrumb"
                    },
                    "inLanguage":yoast_in_language,
                    "potentialAction":
                    [
                        {
                            "@type":"ReadAction",
                            "target":
                            [
                                yoast_url,
                            ]
                        }
                    ]
                },
                {
                    "@type":"BreadcrumbList",
                    "@id":f"{yoast_url}#breadcrumb",
                    "itemListElement":
                    [
                        {
                            "@type":"ListItem",
                            "position":1,
                            "name":"Portada",
                            "item":f"{url}"
                        },
                        {
                            "@type":"ListItem",
                            "position":2,
                            "name":"Test"
                        }
                    ]
                },
                {
                    "@type":"WebSite",
                    "@id":f"{url}#website",
                    "url":f"{url}",
                    "name":yoast_site_name,
                    "description":f"Web de {yoast_site_name}",
                    "potentialAction":
                    [
                        {
                            "@type":"SearchAction",
                            "target":
                            {
                                "@type":"EntryPoint",
                                "urlTemplate":f"url"+"?s={search_term_string}"
                            },
                            "query-input":"required name=search_term_string"
                        }
                    ],
                    "inLanguage":yoast_in_language
                }
            ]
        }
    }

    # yoast json
    print("\tPost json")
    post = {
        # 'id':page_id,
        'title':title,
        'status':'publish',
        'content':content,
        'date':date,
        'date_gmt':date,
        # 'guid':guid,
        'modified':date_modified,
        'modified_gmt':date_modified_gmt,
        'slug':page_slug,
        'type':'page',
        'link':f'{url}{page_slug}/',
        'excerpt':excerpt,
        'author':author,
        'featured_media':featured_media,
        'parent':parent,
        'menu_order':menu_order,
        'comment_status':comment_status,
        'ping_status':ping_status,
        'template':template,
        'meta':meta,
        'blocksy_meta':page_blocksy_meta,
        'yoast_head':yoast_head,
        'yoast_head_json':yoast_head_json,
        # "_links":links,
    }
    return post

def upload_page(page_title, page_slug, page_body, page_read_time, page_user, page_image_icon, page_languaje):
    print("Build json")
    post = create_json(page_title, page_slug, page_body, page_read_time, page_user, page_image_icon, page_languaje)
    # print(post)
    print("Request")
    responce = requests.post(url_pages, headers=header, json=post)
    responce_json = responce.json()

    if 'id' in responce_json.keys():
        print(f"Page {page_title} uploaded")
    else:
        print(f"Error uploading page {page_title}")
        print(responce_json)
    
    return responce_json

def compare(json1, json2, atribute, subatribute = None, rendered = False):
    if subatribute:
        if rendered == False:
            if json1[atribute][subatribute] == json2[atribute][subatribute]:
                print(f"{atribute} {subatribute} {rendered} OK")
            else:
                print(f"{atribute} {subatribute} {rendered} ERROR")
        else:
            if json1[atribute][subatribute] == json2[atribute][subatribute]['rendered']:
                print(f"{atribute} {subatribute} {rendered} OK")
            else:
                print(f"{atribute} {subatribute} {rendered} ERROR")
    else:
        if rendered == False:
            if json1[atribute] == json2[atribute]:
                print(f"{atribute}, rendered = {rendered}: OK")
            else:
                print(f"{atribute}, post = {json1[atribute]}, json = {json2[atribute]} ERROR")
        else:
            if json1[atribute] == json2[atribute]['rendered']:
                print(f"{atribute} {rendered} OK")
            else:
                print(f"{atribute} {rendered} ERROR")

page_title = "Test4"
page_slug = "test4"
page_body = "<p>Cuerpo</p>\n"
page_read_time = 1
page_user = "Maximo FN"
page_image_icon = "https://maximofn.com/wp-content/uploads/2022/08/pandas-icon.png"
page_languaje = "es_ES"
post = upload_page(page_title, page_slug, page_body, page_read_time, page_user, page_image_icon, page_languaje)
id = post['id']
print(id)



# get page
url_page = url_pages + "/" + str(id)
responce = requests.get(url_page)
json = responce.json()

compare(post, json, 'title', rendered = True)
compare(post, json, 'status', rendered = False)
compare(post, json, 'content', rendered = True)
compare(post, json, 'date', rendered = False)
compare(post, json, 'date_gmt', rendered = False)
compare(post, json, 'modified', rendered = False)
compare(post, json, 'modified_gmt', rendered = False)
compare(post, json, 'slug', rendered = False)
compare(post, json, 'type', rendered = False)
compare(post, json, 'link', rendered = False)
compare(post, json, 'excerpt', rendered = False)
compare(post, json, 'author', rendered = False)
compare(post, json, 'featured_media', rendered = False)
compare(post, json, 'parent', rendered = False)
compare(post, json, 'menu_order', rendered = False)
compare(post, json, 'comment_status', rendered = False)
compare(post, json, 'ping_status', rendered = False)
compare(post, json, 'template', rendered = False)
compare(post, json, 'meta', rendered = False)
compare(post, json, 'blocksy_meta', rendered = False)
compare(post, json, 'yoast_head', rendered = False)
compare(post, json, 'yoast_head_json', rendered = False)