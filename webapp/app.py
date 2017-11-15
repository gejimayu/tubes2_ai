from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/predicio', methods=['POST'])
def predicio():
    return request.form.get('text')


if __name__ == '__main__':
    app.run()
