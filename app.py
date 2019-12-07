from flask import Flask, render_template, url_for, redirect
import json
app = Flask(__name__)

@app.route('/')
def home():
    with open('shoesamazon.json', 'r') as sa:
        print(type(sa))
        shoes = json.load(sa)
    return render_template('work.html', shoes=shoes)


if __name__ == '__main__':
    app.run(debug=True)