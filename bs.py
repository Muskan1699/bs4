from bs4 import BeautifulSoup
import requests

#Taking the website as input from user
url=raw_input("Enter website ")

#Adding http so make it a url
r=requests.get("http://"+url)

#For taking all the text from website
data=r.text

#For parsing the data
soup=BeautifulSoup(data)

#For loop for anchor tag
for link in soup.find_all('a'):
	print link.get('href')
	#For printing all the links
