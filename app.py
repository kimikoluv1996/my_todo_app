from flask import Flask

item = dict(task="", completed=False)
items = list()

app = Flask(__name__)

@app.route('/')

def return_html():
    return "Hello World"

if __name__ == "__main__":
    app.run()