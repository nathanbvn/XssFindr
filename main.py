import base64
import json
from bs4 import BeautifulSoup
import requests
import re
from requests import post,get


print("Welcome to XSSFinder")

url = input("Put the URL : ")
domain = url.split(".com")[0] + ".com"
headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/113.0'}
code = requests.get(url,headers=headers).text
soup = BeautifulSoup(code, "html.parser")
inputParser = soup.find_all("input",type=["text", "search"])
for inputElement in inputParser:
    # inputElement["value"] = '<script>alert("faille XSS");</script>'
    inputElement["value"] = 'ok test'
    parent_form = inputElement.find_parent("form")
    print(parent_form)
    if parent_form:
        form_action = domain + parent_form.get("action")
        form_method = parent_form.get("method")

        form_data = {inputElement.get("name"): inputElement.get("value")}

        response = requests.request(method=form_method, url=form_action, data=form_data, headers=headers)

        print(response.text)
