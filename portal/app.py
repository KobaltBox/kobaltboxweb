from flask import Flask
from flask import render_template

#Changes to static file paths because of how flask and unity deal with js...

app = Flask(__name__,
            static_url_path='', 
            static_folder='static',
            template_folder='templates')

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/blog')
def blog():
    return render_template('blog.html')

@app.route('/2dshooter')
def shooterdemo():
    return render_template('2dshooter.html')

if __name__ == '__main__':
    app.run(debug=True)