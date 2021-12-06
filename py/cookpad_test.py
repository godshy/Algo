import sys
import urllib 
import requests, json
try:
      inputs = sys.argv[1]
      # print(inputs)
except:
      IndexError  
      print('pls input a recipe')   

url = requests.get("https://static.cookpad.com/hr/screen/categories.json")
text = url.text

data = json.loads(text)
# for i in data['subcategories']:

meat = data['subcategories'][0]
sub_meat = meat['subcategories']
seafood = data['subcategories'][1]
sub_seafood = seafood['subcategories']

for i in sub_meat:
      try:
            for j in i['subcategories']:
                  if j['name'] == inputs:
                        print(j['recipes'])
      except KeyError:
            if inputs == 'chiken':
                  print(i['recipes'])
for j in sub_seafood:
      try:
            for k in j['subcategories']:
                  if k['name'] == inputs:
                        print(k['recipes'])
      except KeyError:
            if inputs == 'shrimp':
                  print(j['recipes'])

