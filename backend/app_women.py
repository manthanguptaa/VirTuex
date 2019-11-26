 from flask import Flask
import for_women as for_women

app = Flask(__name__)


@app.route('/p1')
def p1():  
      for_women.run("women1.jpg")

@app.route('/p2')
def p2():  
      for_women.run("women2.jpg")

@app.route('/p3')
def p3():  
      for_women.run("women3.jpg") 


if __name__ == '__main__':
   app.run()

