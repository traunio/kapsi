from flask import Flask, render_template, g, redirect, url_for
from puoliintumisajat.decay_webapp import decay_webapp
from vuorotiheys.vuorotiheys import vuorotiheys

app = Flask(__name__)

app.url_map.strict_slashes = False

app.register_blueprint(decay_webapp, url_prefix='/atomit')
app.register_blueprint(vuorotiheys, url_prefix='/vuoro')

@app.route('/')
@app.route('/index.html')
def homepage():
    return render_template('homepage.html')

@app.errorhandler(404)
def page_not_found(error):
    return "Ei löytynyt sivua", 404
    

@app.teardown_appcontext
def close_connection(exception=None):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

if __name__ == '__main__':
    app.run()

