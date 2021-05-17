import requests
import json

api_endpoint="http://text-processing.com/api/sentiment/" #API Documentation: http://text-processing.com/docs/sentiment.html
analyzed=[]

for line in open("./tkinter/text.txt", 'r'):
    
    result=requests.post(api_endpoint, data={"text":line})
    
    # The odds that each word is negative or positive
    negativity=json.loads(result.text)["probability"]["neg"]
    positivity=json.loads(result.text)["probability"]["pos"]
    neutrality=json.loads(result.text)["probability"]["neutral"]

    # final analysis
    end_result = json.loads(result.text)["label"]
    analyzed.append({"text":line, "hate":negativity, "like":positivity, "neutral":neutrality, "result":end_result})

  
open("./tkinter/data.json", 'w').write(json.dumps(analyzed))