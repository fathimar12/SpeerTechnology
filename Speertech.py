from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import requests
from bs4 import BeautifulSoup
import csv

s=Service('C:\\Users\\fashi\\Desktop\\chromedriver_win32\\chromedriver.exe')
browser = webdriver.Chrome(service=s)
init = 0
num = 0

#This function is to get the input from user between 1 to 20
def begin():
 while True:
    try:
        n = int(input("Enter an integer 1-20: "))
    except ValueError:
        print("Please enter a valid integer 1-20")
        continue
    if n >= 1 and n <= 20:
        print(f'You entered: {n}')
        init = n
        for i in range(0,init):
         geturl()
        break
    else:
        print('The integer must be in the range 1-20')

#This function is to launch the webpage, get all the embedded links and store to a CSV.
def geturl():
 reqs = requests.get(url="https://en.wikipedia.org/wiki/Main_Page")
 soup = BeautifulSoup(reqs.text, 'html.parser')
 urls = []
 for link in soup.find_all('a'):
    if not link in urls:
     urls.append(link.get('href'))
 #print(urls)
     outfile = open('C:/Users/fashi/urls2.csv', 'a')
     out = csv.writer(outfile)
     out.writerows(map(lambda x: [x], urls))
     outfile.close()
 print("Total number of URL's present: " + str(len(urls)))

begin()