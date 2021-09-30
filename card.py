import requests,json,time, sys
from requests import get
from re import search
        
print('''
Card Random Numebers
''')
session = requests.Session()
number = input("Amount : ")
num = int("" + number)

class CARD():
    def CardNumber():
        return search(
        """<td height="50" align="center" valign="top"><input name="sample-citizen-id" type="text" id="sample-citizen-id" value="(.*)" o""", 
        get("http://www.kzynet.com/tools/thai_citizen_id_generator/").text).group(1)        

t = CARD()
def loop(num):
    for i in range(num):
        time.sleep(0.05)
        print(CARD.CardNumber())
loop(num)