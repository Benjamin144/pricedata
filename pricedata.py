from bs4 import BeautifulSoup
import requests

# simulates data from a website that sells PC systems and components
# search for Laptops with specific specifications and their latest prices
# my goal is to collect data on Lap tops that are VR Ready
# Differentiating between Laptops that are not VR Ready

# request is requsting infomation from the website:
# https://www.overclockers.co.uk/gaming-laptops


html_text = requests.get(
    'https://www.cyberpowersystem.co.uk/category/laptops/').text
soup = BeautifulSoup(html_text, 'lxml')

# Targeting what looks like cards elements - use a method that will target all
# of the laptop posts by catching an element and inspecting them
