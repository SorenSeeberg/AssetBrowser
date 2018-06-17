from flask import Flask

VERSION = '0.1'
app = Flask(__name__)


@app.route("/")
def index():
    return f'Asset Browser API v. {VERSION}'


@app.route("/action", methods=["POST"])
def action():
    pass


if __name__ == '__main__':

    request = {
        'groupAuth': 'blabablabl2342352342',
        'userAuth': 'sdlasdf982349872',
        'action': {
            'previews': {
                'searchTerm': 'old rocks'
            }
        }
    }

    app.run()
