import os
from flask import Flask

app = Flask(__name__, instance_relative_config=True)
app.config.from_mapping(
    SECRET_KEY='dev',
    DATABASE=os.path.join(app.instance_path, 'digestai.sqlite'),
)


from digestai import db
db.init_app(app)

from digestai import summarize
app.register_blueprint(summarize.bp)
app.add_url_rule('/', endpoint='index')

from digestai import books
app.register_blueprint(books.bp)

from digestai import images
app.register_blueprint(images.bp)

@app.route('/welcome')
def app_root():
    return "Flask app on Heroku!"

if __name__ == "__main__":
    app.run(debug=True)
