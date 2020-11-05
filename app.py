import os
from flask import Flask, request, json
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# any method
# any URL
@app.route('/')
@app.route('/<path>', methods=['GET', 'POST', 'PUT','HEAD','DELETE']) 
def api_gh_msg(path):
    """
    Flask lets you get all the methods only when mentioned explicitly 
    or by the default would be GET method
    WebHook connector that get gets the details which GitHub posts.
    (Still working on it)
    Returns:
        dictionary: JSON that is sent to the above route by GitHub to subscribed events.
    """
    print(request.method)
    headers = request.headers
    # parameters = request.args #returns ImmutableMultiDict([])
    # print("parameters: ", parameters)
    url = request.url
    print("Url: ", url)
    print("\nheaders: ", headers)



    # if request.headers['Content-type'] == 'application/json':
    #    with open('data.json', 'w', encoding='utf-8') as f:
    #        json.dump(request.json, f, ensure_ascii=False, indent=4)
    #    return json.dumps(request.json) 

if __name__ =='__main__':
    app.run(debug=True)