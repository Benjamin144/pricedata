from bs4 import BeautifulSoup
import requests

# simulates data from a website that sells PC systems and components
# search for Laptops with specific specifications and their latest prices


# request is requsting infomation from the website:
# https://www.cyberpowersystem.co.uk/category/laptops/
# Targeting what looks like cards elements to home in on
# info needed to identify product data
# rendering this program in the terminal window
# using a series of formatting to prettify the data results


html_text = requests.get(
    'https://www.cyberpowersystem.co.uk/category/laptops/').text
soup = BeautifulSoup(html_text, 'lxml')
syst_name = soup.find('h2', class_='g-sys-name').text
syst_spec = soup.find('ul', class_='g-sys-spec').text.replace(' ', '')
syst_price = soup.find('p', class_='g-sys-price').text.replace(' ', '')
print(f'''
System Name: {syst_name}
System Specification: {syst_spec}
System Price: {syst_price}
''')

# syst = soup.find('ul', class_='g-sys-spec')
