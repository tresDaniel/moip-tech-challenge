from flask import Flask

app = Flask(__name__)

@app.route("/api/")
def main_method():
    return "It works!"

if(__name__ == '__main__'):
    app.run()