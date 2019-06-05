from flask import Flask
import os
import subprocess

app = Flask(__name__)

@app.route("/")
def hello():
    body = "<h1 style='color:blue'>Flipotronics environment variables</h1>"
    for k, v in os.environ.items(): 
    	body += k + "=" + v + "<br/>"
    out =  subprocess.Popen(['gpio', 'readall'],  stdout=subprocess.PIPE, 
           stderr=subprocess.STDOUT)
    stdout,stderr = out.communicate()
    body +="<br/><h2>GPIO status</h2>"
    body += stdout.decode("utf-8") 
    return body

if __name__ == "__main__":
    app.run(host='0.0.0.0')
