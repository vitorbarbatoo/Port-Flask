from flask import Flask, render_template
from waitress import serve
from app import app  # Substitua 'app' pelo nome do seu aplicativo Flask

if __name__ == '__main__':
    serve(app, host='0.0.0.0', port=8080)


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/projects')
def projects():
    return render_template('projects.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)
