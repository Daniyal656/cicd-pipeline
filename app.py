from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return '''
    <h1> Daniyal's CI/CD Pipeline</h1>
    <p>Automatically deployed using GitHub Actions + Docker + AWS EC2</p>
    <p>CI/CD  Pipeline - DecodeLabs Project 3 Complete!</p>
    '''

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
