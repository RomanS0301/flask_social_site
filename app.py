from flask import Flask, render_template
from config import config
from dotenv import load_dotenv

app = Flask(__name__)
app.config.from_object(config['development'])  # Или 'testing' или 'production'
load_dotenv()


@app.route('/')
def index():  # put application's code here
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
