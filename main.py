from bs4 import BeautifulSoup

with open('index.html', 'r') as html_file:
    content = html_file.read()
# formatting data for better readability
    soup = BeautifulSoup(content, 'lxml')
    feature_promos = soup.find_all('div', class_='feature')
    for feature in feature_promos:
        feature_promos = feature.h4.text
        feature_price = feature.a.text.split()[-2]
# use of f string here is a 'nice have' which can be used to acquire up to
# date data when a website updates price and information

        print(f'{feature_promos} costs {feature_price}')

