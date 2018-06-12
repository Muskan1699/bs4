from bs4 import BeautifulSoup
import requests

#Taking the website as input from user
url=raw_input("Enter website ")

#Adding http so make it a url
r=requests.get("http://"+url)

#For taking all the text from website
data=r.text

#For printing all the data of the website 
print data
