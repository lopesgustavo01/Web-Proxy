import requests
from flask import render_template, Flask



r = requests.post('https://pt.wikipedia.org/wiki/Wiki')
print(r.text)

app = Flask(__name__)

@app.route('/')
def index():
    return render_template(r.text)

if __name__ == '__main__':
    app.run(debug=True)