import pandas as pd
import requests
from bs4 import BeautifulSoup
from datetime import date



def get_gold(site):
    source = requests.get(site).text
    soup = BeautifulSoup(source,'lxml')
    c1 = soup.find('strong',id = "el")
    c = 0
    for j in c1:
        if c == 1:
            m = str(j.strip().replace(",",""))
        c = c + 1
    return(int(m))

def get_silver(site):
    source = requests.get(site).text
    soup = BeautifulSoup(source,'lxml')
    c1 = soup.find('strong',id = "el")
    c = 0
    for j in c1:
        if c == 1:
            m = str(j.strip().replace(",",""))
        c = c + 1
    return(float(m))

def get_date():
    today = date.today()
    return(today)

def get_covid_country(country):
    site = "https://www.worldometers.info/coronavirus/country/" + country

    source = requests.get(site).text
    soup = BeautifulSoup(source,'lxml')
    c1 = soup.find('div',class_='maincounter-number')
    k = c1.text
    k = str(k.strip().replace(',',''))
    return (int(k))

def get_sensex():
    site = "https://www.moneycontrol.com/indian-indices/sensex-4.html"
    source = requests.get(site).text
    soup = BeautifulSoup(source,'lxml')
    k1 = soup.find('span',class_='lastprice')
    k = str(k1.text).strip()
    return(float(k))

def get_gas(city):

    site = "https://www.goodreturns.in/petrol-price.html#Daily+Petrol+Prices+Revision+in+India"
    source = requests.get(site).text
    soup = BeautifulSoup(source,'lxml')
    c1 = soup.find('table')
    for j in c1:
        k = j.find('a')
        if(k != -1):
            r =str(k).split(">")
            try:
                m = (r[1][:-3])
            except:
                m = "not a city"
            if city == m:
                rr = str(j).split("₹ ")
                rr = str(rr[-1].split("<")[0])
                return(float(rr))
                

    


###      -------------------initalize-------------------------
#df = pd.DataFrame({"Date": [get_date()],"Sensex" : [get_sensex()],"Currency" : [0],"Gold" :[ get_gold("https://www.goodreturns.in/gold-rates/")],"Gasoline": [get_gas("Mumbai")],"Silver": [get_silver("https://www.goodreturns.in/silver-rates/")]})




df1 = pd.read_csv("dataset.csv")
df = pd.DataFrame(df1)
    #print(df)

new = [{"Date": get_date(),"Sensex" : get_sensex(),"Currency" : 0,"Gold" : get_gold("https://www.goodreturns.in/gold-rates/"),"Gasoline": get_gas("Mumbai"),"Silver": get_silver("https://www.goodreturns.in/silver-rates/")}]
df = df.append(new,ignore_index=True,sort=False)
df.to_csv("dataset.csv",index=False)

