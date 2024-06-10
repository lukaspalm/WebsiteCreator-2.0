from flask import Flask, render_template, make_response, request, send_file, abort
import shutil, os, json, ast


app = Flask(__name__)
def getnavbars():
    data = []
    navbars = os.listdir('static/assets/templates/navbars/')

    for item in navbars:
        json_data = json.load(open('static/assets/templates/navbars/' + item + "/data.json", "r"))
        data.append(json_data)
    return data
            

        

elements = {
    'navbars': getnavbars()
}

@app.route('/')
def index():
    resp = make_response(render_template('index.html'))
    resp.set_cookie('site-pieces', '[]')
    return resp

@app.route('/create')
def create():
    resp = make_response(render_template('create.html'))
    resp.set_cookie('site-pieces', '[]')
    resp.set_cookie('selection', '')
    return resp
    


@app.route('/get-items')
def get_items():
    target = request.args.get('target')
    html = ""
    if target:
        if target in elements:
            print(elements[target])
            for item in elements[target]:
                itempath = item['path']
                print(itempath)
                html += f'<div class="col-xl-6 col-lg-6 col-md-6 col-12 my-3"><img src="{itempath}image.png" alt="navbar" width="100%" onclick="SelectItem(\'{itempath}\', this)" class="option-item"></div>\n'
            return html
        return f"No {target} found"
    else:
        return "No target provided", 400


@app.route('/download')
def download():
    html = ""
    pieces = ast.literal_eval(request.cookies.get('site-pieces'))
    try:
        for piece in pieces:
            html += open(piece + "code.html", 'r').read()
        with open('created-site/index.html', 'w') as file:
            base = open('static/assets/templates/base/base.html', 'r').read()
            finished = base.replace("{content}", html)
            file.write(finished)
            file.close()


        shutil.make_archive('created-site', 'zip', 'created-site')
        return send_file('created-site.zip', as_attachment=True)
    
    except FileNotFoundError as e:
        print(f"Error: {e}")


if __name__ == '__main__':
    app.run(port=1337, debug=True)
