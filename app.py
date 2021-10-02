from flask import Flask, Blueprint, render_template


# creating the Flask application
app = Flask(__name__, template_folder='templates')


@app.route('/index')
def index():
    return render_template('index.html')



if __name__ == "__main__":
 app.run()