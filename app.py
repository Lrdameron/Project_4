from flask import Flask
from predict_route import predict_bp

app = Flask(__name__)
app.register_blueprint(predict_bp)

@app.route('/')
def home():
    return 'MARYANN THIS IS A PLACEHOLDER FOR ACTUAL TEXT'

if __name__ == '__main__':
    app.run(debug=True)

