from flask import Flask

VERSION = '0.1'
app = Flask(__name__)


@app.route("/")
def index():
    return f'Asset Browser Server v. {VERSION}'


@app.route("/previews")
def images():
    pass


if __name__ == '__main__':
    app.run()
