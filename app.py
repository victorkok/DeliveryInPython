from flask import Flask, Blueprint, render_template


# creating the Flask application
app = Flask(__name__, template_folder='templates')


@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/contatos')
def contatos():
    return render_template('contact-us.html')

if __name__ == "__main__":
 app.run()