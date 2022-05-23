from bs4 import BeautifulSoup

with open('index.html', 'r') as html_file:
    content = html_file.read()

    soup = BeautifulSoup(content, 'lxml')
    feature_promos = soup.find_all('div', class_='feature')
    for feature in feature_promos:
        feature_promos = feature.h4.text
        feature_price = feature.a.text

        print(feature_promos)
        print(feature_price)
