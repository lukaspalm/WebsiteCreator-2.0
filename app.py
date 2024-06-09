from flask import Flask, render_template, make_response, request


app = Flask(__name__)


@app.route('/')
def index():
    resp = make_response(render_template('index.html'))
    resp.set_cookie('site-pieces', '{}')
    return resp

@app.route('/create')
def create():
    return render_template('create.html')

@app.route('/add')
def add():
    id = request.args.get('id')
    if id:
        print("Adding item with id: " + str(id))
        return "Adding item with id: " + str(id)
    else:
        return "No id provided", 400


if __name__ == '__main__':
    app.run(port=1337, debug=True)
