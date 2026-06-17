from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return '''
    <html>
    <head><title>Daniyal CI/CD Pipeline</title></head>
    <body style="font-family:Arial;text-align:center;padding:50px;background:#0d1117;color:white;">
        <h1 style="color:#00d4aa;"> Daniyal's CI/CD Pipeline</h1>
        <p style="font-size:18px;">Automatically deployed using GitHub Actions + Docker + AWS EC2</p>
        <hr style="border-color:#00d4aa;width:50%;">
        <h2 style="color:#00d4aa;"> DecodeLabs Project 3 — Complete!</h2>
        <p>Pipeline Stages: Code → Build → Test → Push → Deploy</p>
        <p style="color:#888;">Deployed by: Daniyal Hussain | Batch 2026</p>
    </body>
    </html>
    '''

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
