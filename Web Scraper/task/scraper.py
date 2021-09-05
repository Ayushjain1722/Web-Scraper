import os
import requests
import urllib.request
from bs4 import BeautifulSoup
import string

# url = input()

############### Task 1 ##########################
# r = requests.get(url)
# if r.status_code != requests.codes.ok or "content" not in r.json() or r.json()['content'] == "":
#     print("Invalid quote resource!")
# else:
#     print(r.json()['content'])

############## Task 2 ###########################
# response = requests.get(url, headers={'Accept-Language': 'en-US;q=0.5'})
# webURL = urllib.request.urlopen(url)
# data = webURL.read()
# soup = BeautifulSoup(data, 'html.parser')
#
# respData = {'title': None,
#             'description': None
#             }
# if 'imdb' not in url or 'title' not in url:
#     print('Invalid movie page!')
# else:
#     try:
#         respData['title'] = soup.title.contents[0]
#         respData['description'] = soup.find('meta', {'name': 'description'})['content']
#         print(respData)
#     except:
#         print('Invalid movie page!')


################### Task 3 ######################
# response = requests.get(url)
# if response.status_code != 200:
#     print('The URL returned ', response.status_code)
# else:
#     page_content = response.content
#     file = open('source.html', 'wb')
#     file.write(page_content)
#     file.close()
#     print('Content saved.')

################ Task 4 #########################

# try:
#     url = "https://www.nature.com/nature/articles?sort=PubDate&year=2020&page=3"
#     response = requests.get(url, headers={'Accept-Language': 'en-US;q=0.5'})
#     webURL = urllib.request.urlopen(url)
#     data = webURL.read()
#     soup = BeautifulSoup(data, 'html.parser')
#
#     article_types = soup.find_all('span', {'data-test': 'article.type'})
#     # print(article_types)
#     indexes = []
#     index = 0
#     for article_type in article_types:
#         if article_type.span.text == "News":
#             indexes.append(index)
#         index += 1
#
#     article_links = soup.find_all('a', {'data-track-action': 'view article'})
#     new_url = 'https://www.nature.com'
#
#     for index in indexes:
#         article_url = new_url + article_links[index]['href']
#         article_html = requests.get(article_url).text
#         soup_article = BeautifulSoup(article_html, 'html.parser')
#         article_title = str(soup_article.title.text)
#         for special_char in string.punctuation:
#             article_title = article_title.replace(special_char, '')
#         article_title = article_title.strip().translate(str.maketrans(' ', '_'))
#         f = open(article_title + '.txt', 'w', encoding='utf=8')
#         article_body = soup_article.find('div', {'class': 'c-article-body'}).text.strip()
#         f.write(article_body)
#         f.close()
# except:
#     print('Invalid URL!')
#
# print('Process completed.')

####################### Task 5 ##################

no_of_pages = int(input())
type_of_article = input()
url = "https://www.nature.com/nature/articles"
# try:
for i in range(1, no_of_pages + 1):
    os.mkdir('Page_' + str(i))
    url = "https://www.nature.com/nature/articles?page=" + str(i)
    response = requests.get(url, headers={'Accept-Language': 'en-US;q=0.5'})
    webURL = urllib.request.urlopen(url)
    data = webURL.read()
    soup = BeautifulSoup(data, 'html.parser')

    article_types = soup.find_all('span', {'data-test': 'article.type'})
    # print(article_types)
    indexes = []
    index = 0
    for article_type in article_types:
        if article_type.span.text == type_of_article:
            indexes.append(index)
        index += 1
    article_links = soup.find_all('a', {'data-track-action': 'view article'})
    new_url = 'https://www.nature.com'

    for index in indexes:
        article_url = new_url + article_links[index]['href']
        article_html = requests.get(article_url).text
        soup_article = BeautifulSoup(article_html, 'html.parser')
        article_title = str(soup_article.title.text)
        for special_char in string.punctuation:
            article_title = article_title.replace(special_char, '')
        article_title = article_title.strip().translate(str.maketrans(' ', '_'))
        f = open('Page_' + str(i) + "/" + article_title + '.txt', 'w', encoding='utf=8')
        article_body = soup_article.find('div', {'class': 'c-article-body'}).text.strip()
        f.write(article_body)
        f.close()

print("Saved all articles.")
