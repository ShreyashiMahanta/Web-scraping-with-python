from bs4 import BeautifulSoup as bs
import csv
import time
from selenium import webdriver
import pandas as pd

#Url of the website
stars_url = "https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars"

#An array containing the headers
headers = ["Name","Distance","Mass","Radius"]
empty = []

browsers = webdriver.Chrome("./chromedriver")
browsers.get(stars_url)

def letsScrapData():
    soup = BeautifulSoup(browser.page_source,"html.parser")

with open("scraping.csv", "w") as f:
    csvWriter = csv.writer(f)
    csvWriter.writerow(headers)
    #csvWriter.writerows(final_planet_data)

