#!python3
from flask import Flask
import urllib.request
import json
app = Flask(__name__)

# foodname -> string
# blacklist -> comma seperated list of strings e.g. "apple,banna,orange"

APP_ID = "08c67c26"
APP_KEY = "d22fafacab5449e1405a9937b7a0a7ba"

@app.route('/<foodname>/<blacklist>')
def f(foodname, blacklist):
    for x in blacklist:
        x = x.lower()

    foodname = foodname.replace(" ", "%20")
    # change amount of hits later maybe if need more precision
    url = "https://api.edamam.com/search?q="+foodname+"&app_id="+APP_ID+"&app_key=" + APP_KEY + "&to=100"
    print(url)
    contents = urllib.request.urlopen(url).read()
    ingredients = []
    contents = json.loads(contents)
    
    hits = contents["hits"]

    for hit in hits:
        recipe = hit["recipe"]
        ingred = recipe["ingredients"]

        print(ingred)
        for x in ingred:
            print(x["text"])
            ingredients.append(x["text"])

    bad = blacklist.split(",")

    cnt = {}
    test = []
    for i in bad:
        a = 0
        for j in ingredients:
            a += j.lower().count(i)
        
        cnt[i] = a
        print("count of "+i+" is "+str(a))
        test.append("count of "+i+" is "+str(a))
            

    # print(contents)
    return str(test)
