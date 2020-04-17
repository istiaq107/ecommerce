
import json
from bottle import Bottle, template, static_file, request, response, redirect, HTTPError
import urllib.parse
import requests


app = Bottle()

#registered email : adnaan525@gmail.com
apiKey = "bdd10a7a-924d-4dd2-94f3-691af64d1dd3"

@app.route('/')
def mainPage():
    return template("index")

@app.route('/calculateCost', method = "post")
def calc():
    url = "https://digitalapi.auspost.com.au/postage/parcel/domestic/calculate.json?"
    params = {
        "from_postcode": request.forms.get("from_postcode"),
        "to_postcode": request.forms.get("to_postcode"),
        "length":"50",
        "width":"40",
        "height":"10",
        "weight":"2",
        "service_code":"AUS_PARCEL_REGULAR"}
    generatedTail = urllib.parse.urlencode(params)
    jsonData = requests.get(url+generatedTail, headers = {"AUTH-Key":apiKey})
    print(jsonData.text)
    template("index.tpl", "hello")


if __name__ == '__main__':
    app.run(debug=True, port=8010)