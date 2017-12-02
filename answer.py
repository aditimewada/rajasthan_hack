import requests
import json
import sys

# str string
query = sys.argv[1]
# for(data in query):
#     string = string+ "+"

# print("------"+string)
url = 'https://api.duckduckgo.com/?q='+ query +'&format=json&pretty=1'
resp = requests.get(url)
res = json.loads(resp.text)
result = res.get('RelatedTopics')
cell = result[0]
print(cell.get('Text'))