from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def show_home():
    return render_template('starter.html')


if __name__ == '__main__':
    #app.run(debug=True)
    app.run()