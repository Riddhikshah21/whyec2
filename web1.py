from flask import Flask
from flask import request

import random
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!!!!"


def randomNumber(rnum):
    sumran=0
    for i in range(int(rnum)):
        sumran += random.randint(0,int(rnum))
    return sumran


@app.route("/r")
def printRandom():
    rnum = request.args.get('rnum')
    print(rnum)
    var1 =randomNumber(rnum)
    return str(var1)

if __name__ == '__name__':
    app.run()

app.run(port=5000)


