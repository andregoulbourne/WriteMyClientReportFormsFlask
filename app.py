from flask import Flask, render_template
from flask_cors import CORS

from util.flask_helper_util import FlaskHelperUtil

app = Flask(__name__, template_folder="static")
CORS(app, origins=["http://localhost:4200", "https://127.0.0.1:8081", "https://localhost:8081"])
from route.summary_route import summary_bp
app.register_blueprint(summary_bp)

@app.route('/')
def home():
    s = FlaskHelperUtil(app)
    return s.attach_scripts(render_template('index.html'))

if __name__ == '__main__':
    app.run(debug=True, port=8081)#flask number is 5000, but using 8081 because I am used to java and 8081 is the default port for java applications