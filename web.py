from flask import Flask
import os
import subprocess

app = Flask(__name__)

@app.route("/")
def hello():
    body = "<h1 style='color:blue'>Flipotronics environment variables</h1>"
    for k, v in os.environ.items(): 
    	body += k + "=" + v + "<br/>"
    body +=  subprocess.run(['gpio', 'readll'], stdout=subprocess.PIPE)
    return body

if __name__ == "__main__":
    app.run(host='0.0.0.0')
