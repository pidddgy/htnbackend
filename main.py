#!python3
from flask import Flask
import urllib.request
import json
app = Flask(__name__)

# foodname -> string
# blacklist -> comma seperated list of strings e.g. "apple,banna,orange"

APP_ID = "08c67c26"
APP_KEY = "d22fafacab5449e1405a9937b7a0a7ba"
allergies = []

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

        # print(ingred)
        for x in ingred:
            # print(x["text"])
            ingredients.append(x["text"])

    bad = blacklist.split(",")

    cnt = {}
    test = []
    res = dict()
    for i in bad:
        a = 0
        for j in ingredients:
            a += j.lower().count(i)
        
        cnt[i] = a
        print("count of "+i+" is "+str(a))
        test.append("count of "+i+" is "+str(a))

        res[i] = a/100
            

    # print(contents)
    res = str(res)
    res = res.replace("\'", "\"")

    return res




@app.route('/updRestrictions/<string:newStr>')
def updRestrictions(newStr):
    print(newStr)
    allergies.append(newStr)
    return "allergies is now "+newStr

@app.route('/queryRestrictions')
def queryRestrictions():
    print("hello")
    print("returning "+allergies[-1])
    print(allergies[-1])
    return allergies[-1]





if(__name__ == "__main__"):
    app.run(host='0.0.0.0', port = 42069, debug = True)

'''
{
  "title": "milk and cheeese and steak,
  "ingr": [
    "1 cup of milk",
    "1 cup of cheese",
    "steak"
  ]
}

"https://api.edamam.com/api/nutrition-details?app_id=88cc2994&app_key=1efc24b560a4cbf7dcd13aa43e88f85b"
curl -d @recipe.json -H "Content-Type: application/json" "https://api.edamam.com/api/nutrition-details?app_id=b8fa8ec0&app_key=2e99e135530eaed01cb9620b24c1f1c0"

'''