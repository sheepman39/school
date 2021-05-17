import requests
import json

# this project was inspired by this repo
# https://github.com/corollari/linusrants
api_endpoint = "http://text-processing.com/api/sentiment/" 
results = []

for line in open("./tkinter/text.txt", 'r'):

    result = requests.post(api_endpoint, data={"text": line})

    # The odds that each word is negative or positive
    negativity = json.loads(result.text)["probability"]["neg"]
    positivity = json.loads(result.text)["probability"]["pos"]
    neutrality = json.loads(result.text)["probability"]["neutral"]

    # final analysis
    end_result = json.loads(result.text)["label"]
    results.append({
        "text": line,
        "result": end_result,
        "hate": negativity,
        "like": positivity,
        "neutral": neutrality,
    })

open("./tkinter/results.json", 'w').write(json.dumps(results))
