from bs4 import BeautifulSoup

import requests
import os
# using flask_restful
from flask import Flask, jsonify, request
from flask_restful import Resource, Api

# creating the flask app
app = Flask(__name__)
# creating an API object
api = Api(app)


# making a class for a particular resource
# the get, post methods correspond to get and post requests
# they are automatically mapped by flask_restful.
# other methods include put, delete, etc.
class Hello(Resource):

    # corresponds to the GET request.
    # this function is called whenever there
    # is a GET request for this resource
    def get(self):
        URL = "https://newsonair.gov.in/"

        HEADERS = ({'User-Agent':
                        'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 \
                        (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36', \
                    'Accept-Language': 'en-US, en;q=0.5'})

        webpage = requests.get(URL, headers=HEADERS)
        soup = BeautifulSoup(webpage.content, "html.parser")
        out=[]
        for i in soup.find_all('audio'):
            url = i['src']
            filename = os.path.basename(url)
            category = filename.split('-')[0]
            subcategory = "-".join(filename.split('-')[1:-1])

            out.append({'url':url, 'path':filename, 'category':category,'subcategory': subcategory})
        return jsonify(out)


# adding the defined resources along with their corresponding urls
# api.add_resource(Hello, '/')
api.add_resource(Hello, '/all')

# driver function
if __name__ == '__main__':
    app.run(debug=True)

# dom = etree.HTML(str(soup))
# for i in dom.xpath('//*[@id="wrapper"]/div[3]/div[2]/div/div[2]'):
#     print(str(i))
