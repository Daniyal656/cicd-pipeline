from flask import Flask

app = Flask(__demoapp__)


 @app.route('/')
def home():
    return '''
   <h1> My CI/CD Pipeline </h1>
   <p> Automatically deployed using GitHub Actions + Docker + AWS EC2</p?
   <p> Pipeline triggered and working!</p>
   '''


 if__demoapp__ == '__main__:
    app.run(host='0.0.0.0', port=5000)
