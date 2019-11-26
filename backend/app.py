from flask import Flask
import Shirt as s

app = Flask(__name__)


@app.route('/p1')
def p1():  
      s.run("559.jpg")

@app.route('/p2')
def p2():  
      s.run("544.jpg")

@app.route('/p3')
def p3():  
      s.run("548.jpg") 


if __name__ == '__main__':
   app.run(use_reloader = True)

