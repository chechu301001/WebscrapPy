import pandas as pd
from selenium import webdriver
from bs4 import BeautifulSoup
import requests

url = 'https://mixbutton.com/mixing-articles/music-note-to-frequency-chart/'
driver = webdriver.Chrome(executable_path='C:/Users/admin/Downloads/chromedriver_win32/chromedriver.exe.exe')
driver.get('https://pages.mtu.edu/~suits/notefreqs.html')