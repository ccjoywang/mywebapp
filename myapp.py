# ----------------------0. import -----------------
from flask import Flask, render_template
# ----------------------1. create app -----------------
app = Flask(__name__)

# ----------------------2. routers -----------------
@app.route('/')
def index():
    return render_template('index.html')


@app.route('/foo')
def foo():
    return render_template('foo.html')


@app.route('/bar')
def bar():
    return render_template('bar.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')


@app.route('/post')
def post():
    return render_template('post.html')


@app.route('/about')
def about():
    return render_template('about.html')

# ----------------------3. start Server -----------------


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
