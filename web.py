from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def hello():
    body = "<h1 style='color:blue'>Flipotronics environment variables</h1>"
    for k, v in os.environ.items(): 
    	body += k + "=" + v + "<br/>"

    return body

if __name__ == "__main__":
    app.run(host='0.0.0.0')