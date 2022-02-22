# @author: Berke Altıparmak
# You may use, distribute and modify this code under the
# terms of the Beerware license, which unfortunately won't be
# written for another century.
# ----------------------------------------------------------------------------
# "THE BEER-WARE LICENSE" (Revision 42):
# <berkealtiparmak@outlook.com> wrote this file.  As long as you retain this notice you
# can do whatever you want with this stuff. If we meet some day, and you think
# this stuff is worth it, you can buy me a beer in return.   Berke Altıparmak
# ----------------------------------------------------------------------------
#


import csv
import pandas as pd
from nsetools import Nse
from pprint import pprint
from selenium import webdriver
from threading import Timer
import time
from datetime import date
import matplotlib.pyplot as plt

today = date.today()
browser = webdriver.Chrome()
browser.get("https://tr.investing.com/currencies/usd-try")
while True:
    time.sleep(5)
    dollar = browser.find_element_by_xpath("/html/body/div[5]/section/div[4]/div[1]/div[1]/div[1]/div[1]/div[2]/span[1]").text
    zaman = browser.find_element_by_xpath("/html/body/div[5]/section/div[4]/div[1]/div[1]/div[1]/div[2]/span[2]").text
    lastdate = str(dollar + "  @  " + zaman + "  @  " + str(today))
    print(dollar + "  @  " + zaman + "  @  " + str(today))
    #with open('dollarvalueslast.csv','a',newline='') as f:
     #   writer = csv.writer(f)
      #  writer.writerow([lastdate])

t = Timer(60.0)
t.start(browser.refresh())

